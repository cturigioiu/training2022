from rest.rest import Rest
from constants.rest_const import rest_const
from parsers.json_parser import json_to_table
from utils.dict_utils import dict_order, take_duedate
import os

if __name__ == '__main__':
    token = os.environ['gorest_token']
    gorest = Rest(base_url=rest_const.BASE_URL, version=rest_const.API_VERSION, token=token)

    # 1
    # for res in ['users', 'posts', 'comments', 'todos']:
    #     response = gorest.get(resource=res, token=token)
    #     response = json_to_table(response)
    #     print(response)

    # 2     # 3
    # user_data = {
    #     'name': 'Test User 9',
    #     'gender': 'male',
    #     'email': 'test.user9@test.com',
    #     'status': 'active'
    # }
    # response = gorest.post(resource='users', data=user_data, token=token)

    # 4

    # print(gorest.search_by_name(token=token, name='Test User 9'))

    # 5
    # options = {
    #     'query': {
    #         'status': 'active'
    #     }
    # }
    # print(json_to_table(gorest.get(resource='users', token=token, options=options)))

    # 6
    # print(json_to_table(gorest.search_middlename(token=token, count=5)))

    # 7
    # desired_id = gorest.search_by_name(name='Test User 9')[0]
    # data = {
    #     'title': 'test_title',
    #     'body': 'test_body'
    # }
    # gorest.create_post(user=desired_id, data=data)

    # user_data = gorest.get_userdata(user_id=desired_id)
    # data = {
    #     'body': 'test_comment'
    # }
    # user_posts = gorest.get_user_posts(user_id=desired_id)
    # gorest.create_comment(post=user_posts[0]['id'], user=user_data[0], data=data)

    # data = {
    #     'title': 'test_todo',
    # }
    # gorest.create_todo(user=desired_id, data=data)

    # 8
    # data = {
    #     'email': 'test_email@test.com'
    # }
    # gorest.patch(resource='users', target=desired_id, data=data)

    # 9

    # result = gorest.get(resource='todos')
    # result = dict_order(result, order_by=take_duedate)
    # print(json_to_table(result))
