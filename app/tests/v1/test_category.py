# import pytest
# from ... import create_app

# from .dummy import category, empty

# # get auth headers for protected endpoints
# from .headers import attendant_headers, admin_headers


# """
#     Tests for category
# """


# # app instance as test
# app = create_app(config_name="testing")
# client = app.test_client()


# # test add categorys
# def test_add_category():
#     response = client.post('/api/v1/category', json=category[0],
#                            headers=admin_headers)
#     assert response.status_code == 201
#     assert 'clothes' in str(response.json)


# # test post same category
# def test_add_same_category():
#     response = client.post('/api/v1/category', json=category[0],
#                            headers=admin_headers)
#     assert response.status_code == 409
#     assert 'category with name already exists' in str(response.json)


# # test post missing field
# def test_add_missing_field():
#     response = client.post('/api/v1/category', json=category[1],
#                            headers=admin_headers)
#     assert response.status_code == 400
#     assert 'missing required field' in str(response.json)


# # test get all categorys 
# def test_get_all_categories():
#     response = client.get('/api/v1/categories', headers=attendant_headers)
#     assert response.status_code == 200


# # test get sigle item
# def test_get_item_by_id():
#     response = client.get('/api/v1/category/1', headers=attendant_headers)
#     assert response.status_code == 200


# # test get item non-existing id 
# def test_get_item_by_non_existing_id():
#     response = client.get('/api/v1/category/20', headers=attendant_headers)
#     assert response.status_code == 404
#     assert 'category with id 20 does not exist' in str(response.json)


# # test get item with str 
# def test_get_item_by_str():
#     response = client.get('/api/v1/category/"20"', headers=attendant_headers)
#     assert response.status_code == 405
#     assert 'int type required' in str(response.json)


# # test admin edit category
# def test_edit_category():
#     response = client.post('/api/v1/category/1', json=category[3],
#                            headers=admin_headers)
#     assert response.status_code == 201
#     assert 'vest' in str(response.json)


# # test attendant edit category
# def test_attendant_edit_category():
#     response = client.post('/api/v1/category/1', json=category[3],
#                            headers=attendnt_headers)
#     assert response.status_code == 401
#     assert 'unauthorized to perform this function' in str(response.json)


# # test edit nonexisting item 
# def test_edit_non_existing_item():
#     response = client.post('/api/v1/category/20', json=category[3],
#                            headers=admin_headers)
#     assert response.status_code == 404
#     assert 'category with id 20 does not exist' in str(response.json)


# # test delete
# def test_delete():
#     response = client.delete('/api/v1/category/1', headers=admin_headers)
#     assert response.status_code == 202
#     assert 'category deleted' in str(response.json)


# # test attendant delete
# def test_attendant_delete():
#     response = client.delete('/api/v1/category/1', headers=attendant_headers)
#     assert response.status_code == 401
#     assert 'unauthorized to perform this function' in str(response.json)
