# EduTech
Infomaton,Education Center for organisations to build mentor and mentee relationship where mentors develop curriculm and mentees learn from frrom mentors. Mentor's curriculum standard and mentees' learning progess is set managed by the Education Consultant

## Description
This is a django rest api backend where users can create accounts and each user group would have their respective functions.

Mentors, for example, can create courses and lectures.
Mentees, for example, can add courses and mentors to their profile.

## Getting Started
The API is deployed at https://mysterious-castle-94559.herokuapp.com

However, if you wish to set up locally within your local environment, here are the instructions:

### Installing
```git clone https://github.com/ezekieltech/eduTech-backend.git ```

``` pip install -r requirements.txt ```

``` python manage.py migrate ```

### Executing
``` python manage.py runserver ```

# REST API Endpoints

## User Sign-up
### Request
``` POST /users/ ```
Parameters are
- email
- username
- password
- password2
- role (options: Mentor, Mentee, Edu-consultant - it's case sensitive)

### Response
```
{
    "email": "postman1@example.com",
    "username": "postman1m",
    "role": "Mentor",
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMTE0NTQwMSwianRpIjoiODFiNTVmMTM4Zjk1NDQ0NmE4MWI3M2YxZGRhZTQxYTkiLCJ1c2VyX2lkIjoiTm9uZSJ9.uTdMuoaj4wDAMD8diEvUqNdc1qpfnZch1fztTyyWecI",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExMDU5MzAxLCJqdGkiOiJjZWVkM2RjYzJhYjM0OTFkYWY5ZmQ2NDA3ZGJlODA5YyIsInVzZXJfaWQiOiJOb25lIn0.4oH9vXfBkxd1mJkMrpLk-uh5-FVRD0GhoSyBy5yNUA8"
    }
}
```

The profile of the user is automatically created as well

## User Log in

### Request
``` POST /auth/jwt/create/ ```
Parameters are
- email
- password

### Response

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMTE0ODY5OCwianRpIjoiZDBhYzRiMDIxMjNmNDdkNDliMjUwNTExYWUyNWQ0OGUiLCJ1c2VyX2lkIjo3fQ.NENCInjBN1oWG3XkR-YVRq5YP1g5EUeNANQVG7gSWFE",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjExMDYyNTk4LCJqdGkiOiI3NDUzM2NhZDExZDI0MThmOTZmNzIyZGRjY2IyZjI3OCIsInVzZXJfaWQiOjd9.i4WEWt3ORRpygaqbn8I7b91nEmh-6SWV5NF0hS6cf1E"
}
```

## User Details

### Request

``` GET /users/{id}/ ```

### Response

```
{
    "email": "admin4@example.com",
    "username": "admin4",
    "role": "Mentor",
    "profile_mentor": 2,
    "tokens": null
}
```

## Mentor Creates Course

### Request

``` POST /classcourses/ ```

Parameters are
- name 
- teacher
- consultant

### Response

```
{
    "name": "Course A",
    "classcourse_lectures": [],
    "teacher": [
        1
    ],
    "consultant": [
        1
    ]
}
```

## Mentor Views Course and Lectures

### Request

``` GET /classcourses/ ```

### Response

```
[
    {
        "name": "Course A",
        "classcourse_lectures": [],
        "teacher": [
            1
        ],
        "consultant": [
            1
        ]
    }
]
```

## Mentor Adds Lectures to Courses

### Request

```POST /lectures/ ```

Parameters

- title

### Response

```
[
    {
        "title": "New Lectures",
        "lectures": null
    },
    {
        "title": "New Lectures II",
        "lectures": null
    }
]
```


