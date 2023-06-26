#!/usr/bin/python3
"""
will update later
"""

import boto3
from decimal import Decimal
import json

# grant 'AmazonDynamoDBFullAccess' permission policy to the role...
# assigned to the function to allow full access to 'DynamoDB'
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tinkoko_table")

def lambda_handler(event, context):
    user_id = event["pathParameters"]["id"]
    # user_id = event["id"]

    response = table.get_item(Key={"id": user_id})

    user_data = response.get("Item")

    if not user_data:
        return {
            'statusCode': 400,
            'body': json.dumps({"message": "User not found"})
        }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'body': user_data
        })
    }
