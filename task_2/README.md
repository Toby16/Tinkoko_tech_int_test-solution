# Task 2
#### /create-product (Creating a new product)
#### Request Payload:
```
    {
    "category": "627cc555046919d2a6f21662",
    "city": "Abuja",
    "count": 10,
    "country": "Nigeria",
    "description": "Banana Flavour Minimum Order Quantity - 10pcs",
    "images": [
    {
    "public_id": "n4t5ccur0shvzrnwlkoy",
    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
    ],
    "price": "1000",
    "productName": "L&Z Yoghurt ",
    "quantity": 100,
    "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
    "sellerId": "634084c8fd2c16ba75c006e8",
    "weight": "500"
    }
```
#### Response Payload:
```
    {
    "id": "SaiUFv2oJurhMWq92VAesQKF", [pk],
    "category": "627cc555046919d2a6f21662",
    "city": "Abuja",
    "count": 10,
    "country": "Nigeria",
    "createdAt": "1685421412232",
    "description": "Banana Flavour Minimum Order Quantity - 10pcs",
    "images": [
    {
    "public_id": "n4t5ccur0shvzrnwlkoy",
    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
    ],
    "price": "1000",
    "productName": "L&Z Yoghurt ",
    "quantity": 100,
    "subCategory": "hLBxpm6XoCWvhQQdsmRjQPZL",
    "sellerId": "634084c8fd2c16ba75c006e8",
    "weight": "500"
    }
```

## Solution
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/create-product
* http method: POST

## Postman api test/result
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_2/assets/postman_test_image.png" alt="postman test image">

## AWS dynamoDB result after Postman api call
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_2/assets/aws_test_result_image.png" alt="aws dynamoDB result image">
