#!/usr/bin/python3
"""
Task-2
Author: Baasit Ayomiposi Bolaji

Lambda function for creating a new product...
and storing it in DynamoDB table.
"""

import boto3
import json
import time  # to generate time when user is created
import uuid  # to generate unique id for user


# grant 'AmazonDynamoDBFullAccess' permission policy to the role...
# assigned to the function to allow full access to 'DynamoDB'
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Tinkoko_table")


def lambda_handler(event, context):
    """
    Lambda handler function for creating a new product.
    * Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.
    * Returns:
        dict: The response containing the status code and body.
    * Raises:
        KeyError: If any required field is missing in the request payload.
    """
    request_ = event

    # Prepare the product data
    product_data = {
        'id': str(uuid.uuid4()),  # Generate a unique ID for the new product
        'category': request_['category'],
        'city': request_['city'],
        'count': request_['count'],
        'country': request_['country'],
        'createdAt': str(int(time.time() * 1000)),  # Timestamp in milliseconds
        'description': request_['description'],
        'images': request_['images'],
        'price': request_['price'],
        'productName': request_['productName'],
        'quantity': request_['quantity'],
        'subCategory': request_['subCategory'],
        'sellerId': request_['sellerId'],
        'weight': request_['weight']
    }

    # Store the product data in DynamoDB
    table.put_item(Item=product_data)

    # response body to be sent back to the client
    response = {
        'id': product_data["id"],
        'category': product_data['category'],
        'city': product_data['city'],
        'count': product_data['count'],
        'country': product_data['country'],
        'createdAt': product_data['createdAt'],
        'description': product_data['description'],
        'images': product_data['images'],
        'price': product_data['price'],
        'productName': product_data['productName'],
        'quantity': product_data['quantity'],
        'subCategory': product_data['subCategory'],
        'sellerId': product_data['sellerId'],
        'weight': product_data['weight']
    }

    # Return the response with a 200 status code
    return {
        'statusCode': 200,
        'body': response
    }
