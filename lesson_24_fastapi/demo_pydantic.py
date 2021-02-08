from datetime import datetime
from typing import Optional
from uuid import uuid4
from pydantic import BaseModel, Field


def create_user(username: Optional[str] = None):
    """
    :param username:
    :return:
    """
    if username is None:
        username = 'asdqweqwe'  # a VERY random string
    return User(id=0, username=username)


def generate_token() -> str:
    token = str(uuid4())
    print("new token", token)
    return token


class UserBase(BaseModel):
    username: str
    is_staff: bool = False
    date_banned: Optional[datetime] = None

    class Config:
        extra = "forbid"
        # extra = Extra.ignore


class User(UserBase):
    id: int
    token: str = Field(default_factory=generate_token)

    # class Config:
    #     orm_mode = True


class UserOut(BaseModel):
    user: User


if __name__ == '__main__':
    u = User(id=1, username='Alex', is_staff=True)

    print(repr(u))
    print(u)

    user_data = {
        'id': 2,
        'username': 'Many',
        'is_admin': True,
    }

    u2 = User(**user_data)
    print(u2)

    # Если в конфиге extra = 'forbid' не возьмет неизвестные атрибуты
    u3 = User(id=3, username='Aln', is_staff=True)
    print(u3)

    # не отдаст чужие атрибуты
    user_dict = u2.dict(exclude_unset=True)
    print(user_dict)

    # Удаляет определенные поля
    user_dict = u2.dict(exclude={'id'})
    print(user_dict)
