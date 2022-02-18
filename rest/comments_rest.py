from rest.rest import Rest


class CommentsRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_comments(self):
        return super().get(resource='comments')

    def create_comment(self, post, user, body):
        data = {
            'post_id': post,
            'name': user['name'],
            'email': user['email'],
            'body': body
        }

        super().post(resource='comments', data=data)
