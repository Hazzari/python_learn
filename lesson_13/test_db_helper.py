from unittest import mock
from pytest import fixture

from lesson_13.db_helper import *


@fixture()
def user():
    print('Get user fixture')
    user = User('test_user')
    yield user
    user.delete()


class TestUser:
    def test_init(self):
        # проверяем создание пользователя с именем username
        username = "username"
        user = User(username)

        assert user.username == username


def test_get_connection():
    # Является ли возвращаемое значение правильным классом
    conn = get_connection()
    assert isinstance(conn, Connection)
    assert isinstance(conn.engine, Engine)


@mock.patch("lesson_13.db_helper.get_connection")
def test_get_user(mocked_get_connection, user):
    # Проверяем правильность вызова функции с пустыми объектами
    username = 'username'
    mocked_conn_get_user = mocked_get_connection.return_value.get_user
    # expected_result = mocked_conn_get_user.return_value
    expected_result = user
    mocked_conn_get_user.return_value = expected_result

    res = get_user(username=username)

    assert res is expected_result
    # mocked_conn_get_user.assert_called()
    # mocked_conn_get_user.assert_called_once()
    mocked_conn_get_user.assert_called_once_with(username)
