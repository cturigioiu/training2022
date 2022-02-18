from rest.users_rest import UsersRest
from rest.comments_rest import CommentsRest
from rest.posts_rest import PostsRest
from rest.todos_rest import TodosRest
from parsers.json_parser import json_to_table
from utils.dict_utils import dict_order, take_duedate

if __name__ == '__main__':
    user_rest = UsersRest()
    post_rest = PostsRest()
    comment_rest = CommentsRest()
    todo_rest = TodosRest()

    # 1
    print(json_to_table(user_rest.retrieve_users()))
    print(json_to_table(post_rest.retrieve_posts()))
    print(json_to_table(comment_rest.retrieve_comments()))
    print(json_to_table(todo_rest.retrieve_todos()))

    # 2     # 3
    user_rest.create_user(name='Test User 9', gender='male', email='test.user9@test.com', status='active')

    # 4
    print(user_rest.search_by_name(name='Test User 9'))

    # 5
    print(json_to_table(user_rest.filter_users(status='active')))

    # 6
    print(json_to_table(user_rest.search_by_middlename(count=5)))

    # 7

    post_rest.create_post(user=user_rest.search_by_name(name='Test User 9')[0], title='test_title', body='test_body')

    comment_rest.create_comment(
        post=post_rest.get_user_posts(user_id=user_rest.search_by_name(name='Test User 9')[0])[0]['id'],
        user=user_rest.get_userdata(user_id=user_rest.search_by_name(name='Test User 9')[0])[0],
        body='test_comment'
    )

    todo_rest.create_todo(user=user_rest.search_by_name(name='Test User 9')[0], title='todo_title')

    # 8

    user_rest.modify_user(target=user_rest.search_by_name(name='Test User 9')[0], email='test_email@test.com')

    # 9

    print(json_to_table(dict_order(todo_rest.retrieve_todos(), order_by=take_duedate)))
