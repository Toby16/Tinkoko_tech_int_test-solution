# Task 3
#### /get-user/[:id] (get a user record using the unique id )

#### /get-user/[:user-name] (get a user record using the userName attribute )

#### /update-user/[:id] (update a user record)
#### Request Payload:
```
    {
    "photo": [
    {
    "public_id": "n4t5ccur0shvzrnwlkoy",
    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
    ],
    "verificationMeans": "National ID"
    "idNumber": "0257248879HGT"
    }
```
#### Response Payload:
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
    "role": [buyer / seller],
    "userId": "temi247",
    "photo": [
    {
    "public_id": "n4t5ccur0shvzrnwlkoy",
    "url": "https://res.cloudinary.com/tinkokooffice/image/upload/v1685421283/n4t5ccur0shvzrnwlkoy.jpg"
    }
    ],
    "verificationMeans": "National ID"
    "idNumber": "0257248879HGT"
    }
```

## Solution
#### /get-user/[:id] (get a user record using unique id)
* logic: <a href="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_3/get_user_with_id.py">get_user_with_id.py</a>
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/get-user/{id}
* HTTP method: GET

#### Postman api test/result
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_3/assets/postman_test_image_1.png" alt="postman test image">
<hr>
<hr>

#### /get-user_/[:user-name] (get a user record using user-name)
* logic: <a href="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_3/get_user_with_user-name.py">get_user_with_user-name.py</a>
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/get-user_/{user-name}
* HTTP method: GET

#### Postman api test/result
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_3/assets/postman_test_image_2.png" alt="postman test image">
<hr>
<hr>

#### /update-user/[:id] (update a user record)
* logic: <a href="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_3/update_user_by_id.py">update_user_by_id.py</a>
* API endpoint: https://bt5jdtm5bc.execute-api.eu-north-1.amazonaws.com/user-api/update-user/{id}
* HTTP method: PUT

#### Postman api test/result
<img src="https://github.com/Toby16/Tinkoko_tech_int_test-solution/blob/main/task_3/assets/postman_test_image_3.png" alt="postman test image">
