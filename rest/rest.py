import requests
from exceptions.exceptions import UnknownApiVersionException, UserNotCreatedException, PostNotCreatedException, \
    CommentNotCreatedException, TodoNotCreatedException, ModificationFailedException
from datetime import datetime, timedelta


def verify_increment(func):
    def wrapper_func(*args, **kwargs):
        start_value = args[0].get(resource=kwargs['resource'], to_dict=False).headers['X-Pagination-Total']
        func(*args, **kwargs)
        end_value = args[0].get(resource=kwargs['resource'], to_dict=False).headers['X-Pagination-Total']
        if int(end_value) - 1 != int(start_value):
            if kwargs['resource'] == 'users':
                raise UserNotCreatedException()
            if kwargs['resource'] == 'posts':
                raise PostNotCreatedException()
            if kwargs['resource'] == 'comments':
                raise CommentNotCreatedException()
            if kwargs['resource'] == 'todos':
                raise TodoNotCreatedException()
        print(f"{kwargs['resource']} updated successfully!")

    return wrapper_func


def verify_modification(func):
    def wrapper_func(*args, **kwargs):

        options = {
            'id': kwargs['target'],
        }
        options.update(kwargs['data'])
        options = {
            'query': options
        }
        func(*args, **kwargs)
        result = args[0].get(resource=kwargs['resource'], options=options)
        if result:
            print(f"{kwargs['resource']} updated successfully!")
        else:
            raise ModificationFailedException()

    return wrapper_func


class Rest:
    def __init__(self, base_url, version, token=None):
        self.base_url = base_url
        if version == '1':
            self.base_url += '/public/v1'
        elif version == '2':
            self.base_url += '/public/v2'
        else:
            raise UnknownApiVersionException()
        self.token = token

    def get(self, resource, to_dict=True, **kwargs):
        headers = {}
        url = self.base_url + '/' + resource

        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token

        if 'options' in kwargs.keys():
            options = kwargs['options']
            if options['query']:
                url += '?'
                for key in options['query'].keys():
                    url += f"{key}={options['query'][key]}&"

        print(f'GET - {url}')
        response = requests.get(url, headers=headers)
        if to_dict:
            return response.json()
        else:
            return response

    @verify_increment
    def post(self, resource, data):
        headers = {}
        url = self.base_url + '/' + resource
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        print(f'POST - {url}')
        print(f"DATA - {data}")
        response = requests.post(url, data, headers=headers)
        if response.status_code < 300:
            response = response.json()
            for key in response.keys():
                print(f"{key}: {response[key]}")
        else:
            print(f'Got stats code: {response.status_code}')

    @verify_modification
    def patch(self, resource, target, data):
        headers = {}
        url = self.base_url + '/' + resource + '/' + str(target)
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        print(f'PATCH - {url}')
        print(f"DATA - {data}")
        response = requests.patch(url, data, headers=headers)
        return response.json()

    def search_by_name(self, name):
        options = {
            'query': {
                'name': name
            }
        }
        response = self.get(resource='users', options=options)

        user_ids = []

        for user in response:
            user_ids.append(user['id'])

        return user_ids

    def get_userdata(self, user_id):
        options = {
            'query': {
                'id': user_id
            }
        }
        return self.get(resource='users', options=options)

    def get_user_posts(self, user_id):
        options = {
            'query': {
                'user_id': user_id
            }
        }
        return self.get(resource='posts', options=options)

    def search_middlename(self, count):
        page = 1
        users_found = []

        while len(users_found) < count:
            options = {
                'query': {
                    'page': page
                }
            }
            response = self.get(resource='users', options=options)

            for user in response:
                if len(user['name'].split(' ')) >= 3:
                    users_found.append(user)

        return users_found[:count]

    def create_post(self, user, data):
        expected_keys = ('title', 'body')

        if all(key in expected_keys for key in data.keys()):
            data['user_id'] = user
            self.post(resource='posts', data=data)

    def create_comment(self, post, user, data):
        expected_keys = ('body',)

        if all(key in expected_keys for key in data.keys()):
            data['post_id'] = post
            data['name'] = user['name']
            data['email'] = user['email']
            self.post(resource='comments', data=data)

    def create_todo(self, user, data, expected_resolve_time=15):
        expected_keys = ('title',)

        if all(key in expected_keys for key in data.keys()):
            data['user_id'] = user
            data['due_on'] = datetime.now() + timedelta(days=expected_resolve_time)
            data['status'] = 'pending'
            self.post(resource='todos', data=data)
