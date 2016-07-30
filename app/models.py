from google.appengine.ext import ndb


class User(ndb.Model):
    # The model for the users
    user_id = ndb.StringProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    date_registered = ndb.DateTimeProperty(auto_now_add=True)
    date_edited = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def get_by_user(cls, user):
        # https://cloud.google.com/appengine/docs/python/users/userobjects
        return cls.query().filter(cls.user_id == user.user_id()).get()


class Note(ndb.Model):
    # The model for the notes
    user = ndb.KeyProperty(kind="User")
    content = ndb.TextProperty()
    date_created = ndb.DateTimeProperty(auto_now_add=True)
    date_edited = ndb.DateTimeProperty(auto_now=True)

