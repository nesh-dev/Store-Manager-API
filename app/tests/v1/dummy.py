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
        "password": "123456", "confirm_password": "123456",  "role": 2}
]

empty = {}

products = [
    {
        "name": "shirt", "description": "A white polo shirt",
        "price": 100, "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "description": "A white polo shirt", "price": 100,
        "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "name": "shirt", "description": "A white polo shirt",
        "price": "100", "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "name": "vest", "description": "A white polo shirt",
        "price": 100, "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },
    {
        "name": "trouser", "description": "A white denim trouser",
        "price": 100, "category_id": 1, "quantity": 2,
        "minimum_inventory": 100
    },

]

category = [
    {
        "name": "clothes",
        "description": "category has all types of apparels"
    },
    {
        "description": "category has all types of apparels"
    },
    {
        "name": 1,
        "description": "category has all types of apparels"
    },
    {
        "name": "Apparels",
        "description": "category has all types of apparels"
    },
    {
        "name": "electronics",
        "description": "category has all types of electronics"
    },


]

sales = [
    {
        "product_name": "shirt",
        "quantity": 3,
        "customer": "Rose"

    },
    {
        "quantity": 3,
        "customer": "Rose"
    },
    {
        "product_name": "shirt",
        "quantity": "3",
        "customer": "Rose"
    },
    {
        "product_name": "vest",
        "quantity": 3,
        "customer": "Rose"
    }


]
