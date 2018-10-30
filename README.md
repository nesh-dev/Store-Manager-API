# Store-Manager-API

[![Build Status](https://travis-ci.org/kevinene91/Store-Manager-API.svg?branch=develop)](https://travis-ci.org/kevinene91/Store-Manager-API)
[![Coverage Status](https://coveralls.io/repos/github/kevinene91/Store-Manager-API/badge.svg?branch=develop)](https://coveralls.io/github/kevinene91/Store-Manager-API?branch=develop)

Store Manager is an app that allows a store owner to manage their inventory, sales and staff. 

The app has two roles the store owner and store attendant who conduct the sales. 

This is the REST API For the APP 



### Installation and Setup 
- Clone the repo 

    `git clone https://github.com/kevinene91/Store-Manager-API.git`

- Switch the develop branch 

    `git fetch origin develop`

- Navigate to the folder 

    `cd Store-Manager-API`

- create a virual env 

    `virtualenv venv`

- Activate the venv 

    `source/venv/activate`

- Install the required packages 

    `pip install -r requirements.txt`

- Install Postgresql 

    `CREATE DATABASE storemanager`

- Run configurations 
  configurations for the app are contained in the sample.env you can copy and paste the structure  and add it to a .env file

   `$ cp sample.env .env`


- navigate back to root and run python run.py 


- use postman to test the endpoints

### Testing 

- run `pytest` within your virtualenviroment 

### Launch the program 

 - `python run.py`

Use Postman to the test the following endpoints 

# API Auth


|Endpoint           |   Method   | description         |
|  ------------     | ---------- |  -----------------  |
|/api/v1/auth/role  |   POST     | add  a new user     |
|                   |            |                     |
|/api/v2/auth/login |   POST     |User Login token     |
|                   |            |                     |
|/api/v2/auth/role  |   POST     | change user role    |
|                   |            |                     |
|                   |            |                     | 
|/api/v2/auth/logout|   POST     | User logout         |

# API Endpoints

|   # Endpoint              |  # Methods    | # Description           |Auth Required           |
|   -----------             | ----------    | -----------------       | ------------           |
|/api/v2/categories         |   GET         |  list all categories    | attendant & admin      |
|                           |               |                         |                        | 
|/api/v2/categories         |   POST        | add  a new category     |  admin                 |
|                           |               |                         |                        |
|/api/v2/category/<id>      |  PUT          |edit category            |  admin                 |
|                           |               |                         |                        |
|/api/v2/category/<id>      |   GET         | get a specific category |  attendant & admin     |
|                           |               |                         |                        |
|/api/v2/products           |   POST        | add  a new product      |  admin                 |
|                           |               |                         |                        |
|/api/v2/products/<id>      |   PUT         |edit a product           |   admin                |
|                           |               |                         |                        |
|/api/v2/products           |   GET         | list all products       |   attendant & admin    |
|                           |               |                         |                        |
|/api/v2/products/<id>      |   GET         | Get a specific product  |   attendant & admin    |
|                           |               |                         |                        |
|url/cat/products           |   POST        | add products to category|   attendant            | 
|                           |               |                         |                        |
|url/products/cat/<id>      |   GET         | all product in category |   attendant and admin  | 
|                           |               |                         |                        |  
|/api/v2/sales              |   GET         |   List all sales        |  admin                 |
|                           |               |                         |                        | 
|/api/v2/sales              |  POST         |    create sales         |  attendant             |
|                           |               |                         |                        |
|/api/v2/sales/<id>         |  GET          |   Get a sale            |  admin and sale creator|
|                           |               |                         |                        |
|/api/v2/sales/<id>         |  DEL          |    Delete a sale item   |  admin                 |
|                           |               |                         |                        |  
|                           |               |                         |                        |
 
### CREATED WITH 

Flask, Flask Restful , Postgres 

### API DOCUMENTATION 
[Apiary Version 2 Documentation](https://storemanagerv2.docs.apiary.io/#)
[PostMan Documentation](https://documenter.getpostman.com/view/2464061/RWguvbZ1)
[Apiary Version 1 Documentation](https://storemanagerv1.docs.apiary.io/#introduction/authentication)



### HEROKU LINK
[HEROKU API](https://store-manger.herokuapp.com/)

### Author 

# Kevin Munene