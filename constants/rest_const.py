import os

from exceptions.exceptions import UserNotCreatedException, PostNotCreatedException, CommentNotCreatedException, \
    TodoNotCreatedException


class rest_const:

    BASE_URL = 'https://gorest.co.in'
    API_VERSION = '2'
    TOKEN = os.environ['gorest_token']

    create_exceptions_dict = {
        'users': UserNotCreatedException(),
        'posts': PostNotCreatedException(),
        'comments': CommentNotCreatedException(),
        'todos': TodoNotCreatedException()
    }