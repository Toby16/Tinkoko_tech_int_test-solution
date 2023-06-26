#!/usr/bin/python3
"""
Task-1
Author: Baasit Ayomiposi Bolaji

This module contains a Lambda function...
for creating a new user in a DynamoDB table.
"""
import boto3
import json
import time  # to generate time when user is created
import uuid  # to generate unique id for user

# grant 'AmazonDynamoDBFullAccess' permission policy to the role...
# assigned to the function to allow full access to 'DynamoDB'
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("user_table")


def lambda_handler(event, context):
    """
    Handle the Lambda function event.
    * Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.
    * Returns:
        dict: The response containing the status code and body.
    * Raises:
        KeyError: If any required field is missing in the request payload.
    """
    request_ = event  # Extract the request payload from the event object
    user_data = {
        'id': str(uuid.uuid4()),  # Assign unique id to new users
        'activateUser': request_['activateUser'],
        'createdAt': str(int(time.time() * 1000)),  # Timestamp in milliseconds
        'currency': request_['currency'],
        'lastName': request_['lastName'],
        'email': request_['email'],
        'firstName': request_['firstName'],
        'phone': request_['phone'],
        'role': request_['role'],
        'userId': request_['userName']
    }

    # store user data into DynamoDB tab;e
    table.put_item(
            Item=user_data
    )

    # response body to be sent back to the client
    response = {
        'id': user_data['id'],
        'activateUser': user_data['activateUser'],
        'createdAt': user_data['createdAt'],
        'currency': user_data['currency'],
        'lastName': user_data['lastName'],
        'email': user_data['email'],
        'firstName': user_data['firstName'],
        'phone': user_data['phone'],
        'role': user_data['role'],
        'userId': user_data['userId']
    }

    # on success return response with '200' status code
    return {
        'statusCode': 200,
        'body': response
    }
