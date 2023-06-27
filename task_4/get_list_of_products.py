#!/usr/bin/python3
"""

"""
import boto3
import json
from decimal import Decimal  # used to fix "'Decimal' not found" error
# for JSON serialization

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tinkoko_table')
# since I have only one table, i'll draw all necessary data...
# from that single table instead of creating a second table...
# and filling it with static data


def lambda_handler(event, context):
    """
    Lambda handler function
    for retrieving list of products from dynamodb by sellerId.
    * Args:
        event (dict): The event data passed to the Lambda function.
        context (object): The runtime information of the Lambda function.
    * Returns:
        dict: The response containing the status code and body.
    * Raises:
        KeyError: If any required field is missing in the request payload.
    """
    # taking the 'try/except' approach
    # for proper error debugging
    try:
        # Get list of products from DynamoDB
        response = table.scan(Limit=10)  # as instructed by the intreviewer
        products = response['Items']

        # Convert Decimal objects to floats to fix "'Decimal' not found" error
        for product in products:
            for key, value in product.items():
                if isinstance(value, Decimal):
                    product[key] = float(value)

        # Prepare the filtered list of products
        filtered_products = []
        for product in products:
            filtered_product = {
                'quantity': product.get('quantity', ''),
                'createdAt': product.get('createdAt', ''),
                'country': product.get('country', ''),
                'weight': product.get('weight', ''),
                'city': product.get('city', ''),
                'count': product.get('count', ''),
                'subCategory': product.get('subCategory', ''),
                'sellerId': product.get('sellerId', ''),
                'category': product.get('category', ''),
                'images': product.get('images', []),
                'description': product.get('description', ''),
                'price': product.get('price', ''),
                'id': product.get('id', ''),
                'productName': product.get('productName', '')
            }
            filtered_products.append(filtered_product)

        # Prepare response payload
        response_payload = {
            'LastEvaluatedKey': response.get('LastEvaluatedKey', None),
            'statusCode': 200,
            'length': len(filtered_products),
            'items': filtered_products
        }

        # Return the response payload with 200 'successful' status code
        return {
            'statusCode': 200,
            'body': json.dumps(response_payload)
            # ensures body is JSON serializable
        }
    except Exception as e:
        return {
            'statusCode': 500,
            # 'products': [product for product in products],
            'body': json.dumps({'error': str(e)})
        }
