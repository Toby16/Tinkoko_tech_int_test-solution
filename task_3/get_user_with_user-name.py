#!/usr/bin/python3
"""
Task 3
Author: Baasit Ayomiposi Bolaji

Lambda function to retrieve user data from a DynamoDB table
by user-name.
"""

import boto3
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
    """
    Lambda handler function for retrieving user data from dynamodb by username.
    * Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.
    * Returns:
        dict: The response containing the status code and body.
    * Raises:
        KeyError: If any required field is missing in the request payload.
    """
    # Extract the user user-name from the path parameters of the event
    user_name = event['pathParameters']['user-name']
    # user_name = event['pathParameters']['userId']

    response = table.scan(FilterExpression='userId = :name', ExpressionAttributeValues={':name': user_name})
    users = response.get('Items')

    # edge case if no user is found in the dynamodb table with the queried user-name
    if not users:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'User not found'})
        }

    # on success, return 200 status code
    # and body in JSON serializable format
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(users, cls=DecimalEncoder)
    }

