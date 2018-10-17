"""
    Has tests dummy data
"""

users = [

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "12345", "role": 1},

    {"username": "nesh", "email": "ksksksk", "password": "12345", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "123245", "role": 1},

    {"email": "munenedeveloper@gmail.com",
        "password": "123245", "role": 1},

    {"username": "nesh", "password": "12345", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "12345"},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "1234ss5", "role": 1},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
        "password": "12345", "role": 2}
]

empty = {}

products = [
    {
        "name": "shirt", "description": "A white polo shirt",
        "price": 100, "category": "clothes", "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "description": "A white polo shirt", "price": 100,
        "category": "clothes", "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "name": "shirt", "description": "A white polo shirt",
        "price": "100", "category": "clothes", "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "name": "vest", "description": "A white polo shirt",
        "price": 100, "category": "clothes", "quantity": 2,
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
        "name": "Apprels",
        "description": "category has all types of apparels"
    }


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
