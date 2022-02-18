from rest.rest import Rest
from datetime import datetime, timedelta


class TodosRest(Rest):
    def __init__(self):
        super().__init__()

    def retrieve_todos(self):
        return super().get(resource='todos')

    def create_todo(self, user, title, expected_resolve_time=15):
        data = {
            'user_id': user,
            'title': title,
            'due_on': datetime.now() + timedelta(days=expected_resolve_time),
            'status': 'pending'
        }

        super().post(resource='todos', data=data)
