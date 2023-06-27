#!/usr/bin/python3
"""
Task 3
Author: Baasit Ayomiposi Bolaji

Lambda function to update user data in a DynamoDB table
by id.
"""

import boto3
import json

# grant 'AmazonDynamoDBFullAccess' permission policy to the role...
# assigned to the function to allow full access to 'DynamoDB'
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tinkoko_table")


def lambda_handler(event, context):
    """
    Lambda handler function for updating existing user data in dynamodb by id.
    * Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.
    * Returns:
        dict: The response containing the status code and body.
    * Raises:
        KeyError: If any required field is missing in the request payload.
    """
    # user_id = event['id']
    user_id = event['pathParameters']['id']
    request_payload = json.loads(event['body'])

    # response = table.get_item(Key={"id": user_id})
    response = table.get_item(Key={"id": user_id})

    user_data = response.get("Item")

    # if no existing user is found,
    # return a 404 'not found' status code...
    # along with error message
    if not user_data:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'User not found'})
        }

    # Update user data with the request payload
    user_data.update(request_payload)

    # save updated data into the dynamodb database
    table.put_item(Item=user_data)

    # the desired response body
    response_body = {
        "id": user_data["id"],
        "activateUser": user_data["activateUser"],
        "createdAt": user_data["createdAt"],
        "currency": user_data["currency"],
        "lastName": user_data["lastName"],
        "email": user_data["email"],
        "firstName": user_data["firstName"],
        "phone": user_data["phone"],
        "role": user_data["role"],
        "userId": user_data["userId"],
        "photo": user_data["photo"],
        "verificationMeans": user_data["verificationMeans"],
        "idNumber": user_data["idNumber"]
    }

    # on success, return 200 'successful' status code...
    # along with desired response body in JSON serializable format
    return {
        'statusCode': 200,
        'body': json.dumps(response_body)
    }
