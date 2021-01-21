URL = "sqlite:///:memory:"


class User:
    GROUPS = [1, 2, 3, ]

    @staticmethod
    def group_exists(cls, group_id):
        """
        Обьяснение зачем нужен @staticmethod
        >>> User.group_exists(1)
        ... True
        >>> User.group_exists(4)
        ... False
        """

        return group_id in cls.GROUPS

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username

    def delete(self):
        print('\nDeleted user', self)
        return True


# Драйвер для работы с базой данных
class Engine:
    def __init__(self, url):
        self.url = url


# Соединение с базой данных
class Connection:
    def __init__(self, engine: Engine):
        self.engine = engine

    def get_user(self, username):
        return User(username)

    def get_admin(self):
        return self.get_user("admin")


# хелперы
def get_engine(url=URL):
    return Engine(url=url)


def get_connection(engine=None):
    if engine is None:
        engine = get_engine()
    return Connection(engine=engine)


def get_user(username):
    conn = get_connection()
    return conn.get_user(username)
