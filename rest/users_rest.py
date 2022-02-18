from rest.rest import Rest


class UsersRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_users(self, **kwargs):
        return super().get(resource='users', **kwargs)

    def create_user(self, name, gender, email, status):
        data = {
            'name': name,
            'gender': gender,
            'email': email,
            'status': status
        }
        super().post(resource='users', data=data)

    def filter_users(self, name=None, gender=None, email=None, status=None):
        options = {
            'query': {
                'name': name,
                'gender': gender,
                'email': email,
                'status': status
            }
        }
        return self.retrieve_users(options=options)

    def modify_user(self, target, **keyword):
        if all(key in ['name', 'gender', 'email', 'status'] for key in keyword.keys()):
            super().patch(resource='users', target=target, data=keyword)

    def search_by_name(self, name):
        response = self.filter_users(name=name)

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
        return self.retrieve_users(options=options)

    def search_by_middlename(self, count):
        page = 1
        users_found = []

        while len(users_found) < count:
            options = {
                'query': {
                    'page': page
                }
            }
            response = self.retrieve_users(options=options)

            for user in response:
                if len(user['name'].split(' ')) >= 3:
                    users_found.append(user)
            page += 1

        return users_found[:count]
