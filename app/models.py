from google.appengine.ext import ndb
from datetime import datetime

import helpers


class User(ndb.Model):
    # The model for the users
    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty()
    date_registered = ndb.DateTimeProperty(auto_now_add=True)
    date_edited = ndb.DateTimeProperty(auto_now=True)
    last_login = ndb.DateTimeProperty()
    login_history = ndb.JsonProperty(default=[])

    @classmethod
    def get_by_user(cls, user):
        # https://cloud.google.com/appengine/docs/python/users/userobjects
        return cls.query().filter(cls.user_id == user.user_id()).get()

    @staticmethod
    def get_user_by_email(email):
        user = False
        query = User.query(User.email == email).fetch(1)
        for res in query:
            if res.email == email:
                user = res
                break
        return user

    @staticmethod
    def register(email, password):
        user = User()
        user.email = email
        user.password = helpers.hash_password(password)
        user.put()
        return user

    @staticmethod
    def login(email, password):
        login = False
        user = User.get_user_by_email(email)
        if user:
            if helpers.check_password(password, user.password) == user.password:
                login = True
                now = datetime.now()
                user.last_login = now
                user.login_history.insert(0, str(now))
                user.put()

        return login, user


class Note(ndb.Model):
    # The model for the notes
    user = ndb.KeyProperty(kind="User")
    content = ndb.TextProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    date_edited = ndb.DateTimeProperty(auto_now=True)
