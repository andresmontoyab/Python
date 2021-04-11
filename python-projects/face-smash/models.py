import datetime
from peewee import *
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

DATABASE = SqliteDatabase('social.db')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=120)
    joined_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    def get_posts(self):
        return Post.select().where(Post.user == self)

    @classmethod
    def create_user(cls, username, email, password):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password))
        except IntegrityError:
            pass
            #raise ValueError('User already exist')


class Post(Model):
    username = ForeignKeyField(User, related_name='posts',)
    time_stamp = DateTimeField(default=datetime.datetime.now)
    content = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post], safe=True)
    DATABASE.close()