# Store-Manager-API

[![Build Status](https://travis-ci.org/kevinene91/Store-Manager-API.svg?branch=ch-tests-161209990)](https://travis-ci.org/kevinene91/Store-Manager-API)[![Coverage Status](https://coveralls.io/repos/github/kevinene91/Store-Manager-API/badge.svg?branch=ch-tests-161209990)](https://coveralls.io/github/kevinene91/Store-Manager-API?branch=ch-tests-161209990)

Store Manager is an app that allows a store owner to manage their inventory, sales and staff. 

The app has two roles the store owner and store attendant who conduct the sales. 

This is the REST API For the APP 



### Installation and Setup 
Clone the repo 

`git clone https://github.com/kevinene91/Store-Manager-API.git`

Switch the develop branch 

`git fetch origin develop`

Navigate to the folder 

`cd Store-Manager-API`

create a virual env 

`virtualenv venv`

Activate the venv 

`source/venv/activate`

Install the required packages 

`pip install -r requirements.txt`

### Launch the program 

`python run.py`

Use Postman to the test the following endpoints 

# API Auth


|Endpoint           |   Method   | description         |
|  ------------     | ---------- |  -----------------  |
|/api/v1/register   |   POST     | add  a new user     |
|                   |            |                     |
|/api/v1/login      |   POST     |User Login token     |
|                   |            |                     | 
|/api/v1/logout     |   POST     | User logout         |

# API Endpoints

|   # Endpoint         |  # Methods    | # Description           |Auth Required           |
|   -----------        | ----------    | -----------------       | ------------           |
|/api/v1/caregories    |   GET         |  list all categories    | attendant & admin      |
|                      |               |                         |                        | 
|/api/v1/categories    |   POST        | add  a new category     |  attendant & admin     |
|                      |               |                         |                        |
|/api/v1/category/<id> |  PUT          |edit category            |  attendant & admin     |
|                      |               |                         |                        |
|/api/v1/category/<id> |   GET         | get a specific category |  attendant & ad  min   |
|                      |               |                         |                        |
|/api/v1/products      |   POST        | add  a new product      |  attendant & admin     |
|                      |               |                         |                        |
|/api/v1/products/<id> |   PUT         |edit a product           |  attendant & admin     |
|                      |               |                         |                        |
|/api/v1/products      |   GET         | list all products       |   attendant & admin    |
|                      |               |                         |                        |  
|/api/v1/sales         |   GET         |   List all sales        |  admin                 |
|                      |               |                         |                        | 
|/api/v1/sales         |  POST         |    create sales         |  attendant             |
|                      |               |                         |                        |
|/api/v1/sales/<id>    |  GET          |   Get a sale            |  admin and sale creator|
|                      |               |                         |                        |
|/api/v1/sales/<id>    |  DEL          |    Delete a sale item   |  admin                 |
|                      |               |                         |                        |  
|/api/v1/sales/<id>    |  PUT          |    Edit a sale record   |   admin                |
|                      |               |                         |                        |

### CREATED WITH

Flask, Flask Restful 

### API DOCUMENTATION 

[Documentation](https://documenter.getpostman.com/view/2464061/RWguvbZ1)

### HEROKU LINK
[HEROKU API](https://store-manger.herokuapp.com/)

### Author 

# Kevin Munene