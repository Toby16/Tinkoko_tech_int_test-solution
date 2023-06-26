#!/usr/bin/python3
"""
Task 3
Author: Baasit Ayomiposi Bolaji

Lambda function to retrieve user data from a DynamoDB table
by ID.
"""

import boto3
from decimal import Decimal
import json

# grant 'AmazonDynamoDBFullAccess' permission policy to the role...
# assigned to the function to allow full access to 'DynamoDB'
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tinkoko_table")


class DecimalEncoder(json.JSONEncoder):
    """
    Custom JSON encoder class that handles Decimal objects/raw data
    and converts them to a JSON-serializable format.

    This class is created to fix the error where
    'json.dumps()' function is unable to handle Decimal objects directly.
    """
    def default(self, o):
        # Convert Decimal objects to float for JSON serialization
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)


def lambda_handler(event, context):
    # Extract the user ID from the path parameters of the event
    user_id = event["pathParameters"]["id"]
    # user_id = event["id"]

    response = table.get_item(Key={"id": user_id})

    user_data = response.get("Item")

    if not user_data:
        # on error, return 400 status code with error message in response body
        return {
            'statusCode': 400,
            'body': json.dumps({"message": "User not found"})
        }

    # Return a 200 status code with the user data in the response body
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'body': user_data
        }, cls=DecimalEncoder)
    }
