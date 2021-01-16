from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

# Создаем драйвер базы данных
engine = create_engine("sqlite:///example.db")
# Указываем на тип базы данных(декларативный)
Base = declarative_base(bind=engine)

# Создаем
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Таблица для Many to many связей.
posts_tags_table = Table('posts_tags',
                         Base.metadata,
                         Column('post_id', Integer(), ForeignKey('posts.id'), primary_key=True),
                         Column('tags_id', Integer(), ForeignKey('tags.id'), primary_key=True)
                         )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts: list = relationship("Post", back_populates="author")

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.username!r})'

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__: str = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)

    # Один к многим (один автор много постов)
    author = relationship(User, back_populates="posts")

    # связь через промежуточную таблицу posts_tags_table many-to-many
    tags = relationship("Tag", secondary=posts_tags_table, back_populates="posts")

    # tags = None
    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title!r}, author={self.author})'

    def __repr__(self):
        return str(self)


class Tag(Base):
    __tablename__: str = "tags"

    id = Column(Integer, primary_key=True, )
    name = Column(String(32), unique=True, nullable=True)

    # связь через промежуточную таблицу posts_tags_table many-to-many
    posts = relationship(Post, secondary=posts_tags_table, back_populates="tags")

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, name={self.name!r})'

    def __repr__(self):
        return str(self)


def create_user(username: str) -> User:
    new_user = User(username=username)
    session.add(new_user)
    session.commit()
    return new_user


def author_posts(author, posts):
    # получение пользователя
    user: User = session.query(User).filter_by(username=author).one()
    # Создание поста

    # Создание поста через user
    post = Post(title="First post!", author=user)
    user.posts.append(post)
    session.commit()

    # Вывод результатов
    print(post)
    print(user.posts)


def create_tags(name):
    user = session.query(User).filter_by(username=name).one()
    print(user)
    user.is_staff = True
    tags = [Tag(name=name) for name in ("news", "flask", "django", "python")]
    post = Post(title="News Flask vs Django", author_id=user)

    post.tags.extend(tags)
    session.commit()
    print()

    new_post = session.query(Post).filter_by(title='First post!').all()
    print(new_post)
    # print("post.id =", new_post.id)
    #
    # print(post, post.tags)
    #
    # for tag in tags:
    #     print(tag, tag.posts)


if __name__ == '__main__':
    Base.metadata.create_all()
    session = Session()

    # Создание пользователя
    name = 'alex'
    # create_user(name)
    # author_posts(name, 'New post two alex')
    create_tags(name=name)
    user = session.query(User).filter_by(username='alex').one()

    # Обязательно закрывать соединение с БД
    session.close()
