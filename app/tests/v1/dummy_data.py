"""
    Has tests dummy data
"""


users_login = [
    {"email": "munenedeveloper@gmail.com", "password": "123456"}]

users = [

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
     "password": "123456", "confirm_password": "123456", "role": 1},

    {"username": "nesh", "email": "ksksksk", "password": "123456",
        "confirm_password": "123456", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "123245", "confirm_password": "123456", "role": 1},

    {"email": "munenedeveloper@gmail.com",
        "password": "123245", "confirm_password": "123456", "role": 1},

    {"username": "nesh", "password": "12345",
     "confirm_password": "123456", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "12345"},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "1234ss5", "confirm_password": "1234ss5", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "123456", "confirm_password": "123456",  "role": 2},

    {"username": "Rose", "email": "rose@gmail.com",
        "password": "123456", "confirm_password": "123456",  "role": 2},
    {"username": "Eric", "email": "eric@gmail.com",
        "password": "123456", "confirm_password": "123456",  "role": 1}
]

empty_data = {}

products = [
    {
        "id": 1,
        "name": "shirt", "description": "A white polo shirt",
        "price": 100, "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "id": 1,
        "description": "A white polo shirt", "price": 100,
        "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "id": 1,
        "name": "shirt", "description": "A white polo shirt",
        "price": "100", "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "id": 1,
        "name": "vest", "description": "A white polo shirt",
        "price": 100, "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },
    {
        "id": 1,
        "name": "trouser", "description": "A white denim trouser",
        "price": 100, "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

]

category = [
    {
        "id": 1,
        "name": "clothes",
        "description": "category has all types of apparels"
    },
    {

        "id": 1,
        "description": "category has all types of apparels"
    },
    {
        "id": 1,
        "name": 1,
        "description": "category has all types of apparels"
    },
    {
        "id": 1,
        "name": "Apparels",
        "description": "category has all types of apparels"
    },
    {
        "id": 1,
        "name": "electronics",
        "description": "category has all types of electronics"
    },


]

sales = [
    {
        "id": 1,
        "product_id": 1,
        "quantity": 3,
        "attendant": "munenedeveloper@gmail.com",
        "customer": "Rose"

    },
    {
        "id": 1,
        "quantity": 3,
        "customer": "Rose"
    },
    {
        "id": 1,
        "product_id": "shirt",
        "quantity": "3",
        "customer": "Rose"
    },
    {
        "id": 1,
        "product_id": 1,
        "quantity": 3,
        "customer": "Rose"
    }


]
