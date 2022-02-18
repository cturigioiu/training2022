from rest.rest import Rest


class PostsRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_posts(self, **kwargs):
        return super().get(resource='posts', **kwargs)

    def create_post(self, user, title, body):
        data = {
            'user_id': user,
            'title': title,
            'body': body
        }
        super().post(resource='posts', data=data)

    def get_user_posts(self, user_id):
        options = {
            'query': {
                'user_id': user_id
            }
        }
        return self.retrieve_posts(options=options)
