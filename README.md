# Management Information System

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [End Points](#end-points)

## Introduction
This is a back-end application for management information system. It was created
using Django 4.0.2.

## Installation
Clone or download zipped version and do these following steps:

```
$ python manage.py makemigrations student
$ python manage.py migrate
```

Run this for seeds the student table:

```
$ python manage.py seed
```

## End Points
| HTTP Method | URL                 | Description                                                                  |
| ----------- | ------------------- | ---------------------------------------------------------------------------- |
| GET         | `/api/student/`     | Get all students.                                                            |
| POST        | `/api/student/add/` | Add a student. Require a JSON consists of `name`, `major`, and `email` keys. |
| GET         | `/api/student/{id}` | Get a student with specific ID.                                              |
| PUT         | `/api/student/{id}` | Change the student's data with specific ID.                                  |
| DELETE      | `/api/student/{id}` | Delete a student with specific ID.                                           |