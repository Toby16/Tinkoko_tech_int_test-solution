#!/usr/bin/python3
"""
will update later
"""

import boto3
import json
import time
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("product_table")

def lambda_handler(event, context):
    """
    will update later
    """
    
    request_payload = event

    # Prepare the product data
    product_data = {
        'id': str(uuid.uuid4()),  # Generate a unique ID for the new product
        'category': request_payload['category'],
        'city': request_payload['city'],
        'count': request_payload['count'],
        'country': request_payload['country'],
        'createdAt': str(int(time.time() * 1000)),  # Timestamp in milliseconds
        'description': request_payload['description'],
        'images': request_payload['images'],
        'price': request_payload['price'],
        'productName': request_payload['productName'],
        'quantity': request_payload['quantity'],
        'subCategory': request_payload['subCategory'],
        'sellerId': request_payload['sellerId'],
        'weight': request_payload['weight']
    }

    # Store the product data in DynamoDB
    table.put_item(Item=product_data)

    # Prepare the response payload
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
