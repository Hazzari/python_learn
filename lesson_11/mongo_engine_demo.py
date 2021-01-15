import json
import os
from datetime import datetime

from mongoengine import *

connect("Test_BD_Mongo")


class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)
    password = BinaryField(required=True)
    age = IntField(max_value=150)
    bio = StringField(max_length=100)
    categories = ListField()
    admin = BooleanField(default=False)
    registered = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self) -> str:
        user_dict = {
            'username': self.username,
            'email': self.email,
            'age': self.age,
            'bio': self.bio,
            'categories': self.categories,
            'admin': self.admin,
            'registered': self.registered,
        }
        return json.dumps(user_dict)

    meta = {
        'indexes': ['username', 'age'],
        'ordering': ['date_created'],
    }


# dynamic documents
class BlogPost(DynamicDocument):
    title = StringField(unique=True, required=True)
    content = StringField(required=True)
    author = ReferenceField(User, required=True)
    date_created = DateTimeField(default=datetime.utcnow)

    meta = {
        'indexes': ['title'],
        'ordering': ['-date_created']
    }


def create_user(username: str, email: str, age: int, bio: str = None) -> None:
    user = User(
        username=username,
        email=email,
        password=os.urandom(16),
        age=age,
        bio=bio,
    ).save()
    print(f'Пользователь {user.username} создан!')
    return None


def find_user(username: str) -> str:
    try:
        found_user = User.objects().get(username=username)
    except DoesNotExist:
        found_user = 'Пользователь не найден'
    return found_user


def delete_user(user_id: str) -> None:
    deleted_user = User.objects().filter(id=user_id).first()
    deleted_user.delete()
    print(f'Пользователь {deleted_user.username} удален!')
    return None


def create_blog_post(title: str, content: str, author: User) -> None:
    new_blog_post = BlogPost(
        title=title,
        content=content,
        author=author,

    ).save()
    print(f'Пост {new_blog_post.title} создан')


def new_user() -> None:
    while True:
        try:
            username = input('Введите имя пользователя: ')
            email = input('Введите почту: ')
            age = int(input('Введите возраст: '))
            create_user(username, email, age)
            break
        except NotUniqueError:
            print("Пользователь с такими данными уже существует")
            res = input(f'продолжить создание пользователя? [Y/n]: ')
            if res == 'n'.lower():
                break


# new_user()
user = find_user('John')
print(type(user))
# try:
#     print(user.id)
# except AttributeError:
#     print(user)
#
# # delete_user(user.id)
