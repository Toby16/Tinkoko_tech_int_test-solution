# Task 1
#### /create-user (Creating a new user)
#### Request Payload:
```
    {
    "activateUser": false,
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": [buyer/seller],
    "userName": "temi247",
    }
```
#### Response Payload
```
    {
    "id" "h3fons893dfjg944ff" [partion key -pk]
    "activateUser": false,
    "createdAt": "1667213189880",
    "currency": "NGN",
    "lastName": "Lamidi ",
    "email": "lamiditemitope31@email.com" ,
    "firstName": "Temitope ",
    "phone": "7043330737",
    "role": [buyer/seller],
    "userId": "temi247",
    }
```

## Solution
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/create-user
* http method: POST

## Postman api test/result
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_1/assets/postman_test_image.png" alt="postman test image">

## AWS dynamoDB result after Postman api call
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_1/assets/aws_test_result_image.png" alt="aws dynamoDB result image">
