
""" Users dummy data """
users = [
    {"username": "testadmin", "email": "testadmin@gmail.com",
     "password": "123456", "confirm_password": "123456"},

    {"username": "testattendant", "email": "testattendant@gmail.com",
     "password": "123456", "confirm_password": "123456"},

    {"username": "mary", "email": "mary@gmail.com",
     "password": "123456", "confirm_password": "123456"},

    {"username": "mary", "email": "marygmail.com",
     "password": "123456", "confirm_password": "123456"},

    {},

    {"username": "mary", "email": "mary@gmail.com",
     "password": "123456", "confirm_password": "12345996"},

    {"username": "mary",
     "password": "123456", "confirm_password": "12345996"},

    {"username": "nesh", "email": "munenedeveloper@gmail.com",
     "confirm_password": "123456"},

    {"username": "", "email": "munenedeveloper@gmail.com",
     "password": "123456", "confirm_password": "123456"},
     ]

"""products dummy data"""

products = [
    {
        "name": "shirt", "description": "A white polo shirt",
        "price": 100, "quantity": 2,
        "minimum_inventory": 100
    },

    {
        "description": "A white polo shirt", "price": 100,
        "quantity": 2,
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
    }

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

category_product = [{"product_id": 1, "category_id": "1"}]


sale_items = [
   {
    "sale_items": [{"product_id":1, "quantity":1}],
    "customer":"victor"
    },
    {
    "sale_items": [{"product_id":1, "quantity":1}, {"product_id":1, "quantity":3}]
    },
    {
    "sale_items": [{"product_id":1, "quantity":1}, {"product_id":2, "quantity":3}],
    "customer":"victor"
    },
    {
    "sale_items": [{"product_id":1, "quantity":1}, {"product_id":2, "quantity":3}],
    "customer":"victor"
    },
    ]
