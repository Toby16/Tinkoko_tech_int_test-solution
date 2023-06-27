# Task 4
#### /list-product (get list of product; Limits=10)
##### Use the sellerId attached to each product to get the seller info (i.e firstName, lastName, userName and profilePic) before returning the list
#### Response Payload:
```
    {
    "LastEvaluatedKey": {
        "id": "633192b485f761e0d94b2bfd"
    },
    "statusCode": 200,
    "length": 10,
    "items": [
        {
            "productName": "Irish Potatoes",
            
            "category": "627cc5f7046919d2a6f2167d",
            "createdAt": "1663787083980",
            "images": [
                {
                    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                    "public_id": "1663787064948"
                }
            ],
            "sellerId": "632ab45bca9584f349e7f0e1",
            "productId": "632b604b0da9bd1d419a07db",
            "posterInfo": {
                "role": "seller",
                "firstName": "Yakubu",
                "lastName": "Rimamnungra",
                "profilePicUrl": "N/A"
            }
        },
        {
            "productName": "Brown Rabbit",
            
            "category": "627cc5f7046919d2a6f2167d",
            "createdAt": "1663787083980",
            "images": [
                {
                    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                    "public_id": "1663787064948"
                }
            ],
            "sellerId": "632ab45bca9584f349e7f0e1",
            "productId": "632b604b0da9bd1d419a07db",
            "posterInfo": {
                "role": "seller",
                "firstName": "Ajayi",
                "lastName": "Rafel",
                "profilePicUrl": [
                {
                    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1663787065/1663787064948.jpg",
                    "public_id": "1663787064948"
                }
            ],
            }
        }
        
    ]
}
```

## Solution
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/list-product
* HTTP method: GET

#### Postman api test/result
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_4/assets/postman_test_image.png" alt="postman test image">
