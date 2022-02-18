import requests
from exceptions.exceptions import UnknownApiVersionException,  ModificationFailedException
from constants.rest_const import rest_const


def verify_increment(func):
    def wrapper_func(*args, **kwargs):
        start_value = args[0].get(resource=kwargs['resource'], to_dict=False).headers['X-Pagination-Total']
        func(*args, **kwargs)
        end_value = args[0].get(resource=kwargs['resource'], to_dict=False).headers['X-Pagination-Total']
        if int(end_value) - 1 != int(start_value):
            raise rest_const.create_exceptions_dict[kwargs['resource']]
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
    def __init__(self):
        self.base_url = rest_const.BASE_URL
        if rest_const.API_VERSION == '1':
            self.base_url += '/public/v1'
        elif rest_const.API_VERSION == '2':
            self.base_url += '/public/v2'
        else:
            raise UnknownApiVersionException()
        self.token = rest_const.TOKEN

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
                    if options['query'][key]:
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
