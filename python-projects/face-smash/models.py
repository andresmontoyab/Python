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
        return (Posts.select()
                .where(
                    (Posts.user << self.get_following())) |
                    (Posts.user == self)
                )


    def get_stream(self):
        return Posts.select().where(Posts.user == self)

    def get_following(self):
        return (User.select()
                .join(Relationship, on=Relationship.to_user)
                .where(Relationship.from_user==self))

    def get_followers(self):
        return (User.select()
                .join(Relationship, on=Relationship.to_user)
                .where(Relationship.to_user==self))

    @classmethod
    def create_user(cls, username, email, password):
        try:
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password))
        except IntegrityError:
            raise ValueError('User already exist')


class Posts(Model):
    user = ForeignKeyField(User, related_name='posts',)
    time_stamp = DateTimeField(default=datetime.datetime.now)
    content = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)


class Relationship(Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    class Meta:
        database = DATABASE
        indexes = (
            (('from_user', 'to_user'), True),
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Posts, Relationship], safe=True)
    DATABASE.close()