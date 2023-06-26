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
    "role": "seller",
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
    "role": "seller",
    "userId": "temi247",
    }
```

## Solution
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/create-user
* http method: POST
