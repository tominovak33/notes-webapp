import templates
import datetime
from py_bcrypt import bcrypt


# merge 2 dictionaries into one
def merge(a, b):
    a.update(b)
    return a


# wrapper around merge to allow for more than two dictionaries to merged
def merge_many(*arguments):
    res = {}
    for argument in arguments:
        res = merge(res, argument)

    return res


def throw404(self):
    self.error(404)
    templates.render_page("404", {}, self)


def set_cookie(name, value, self):
    self.response.set_cookie(name, value, expires=(datetime.datetime.now() + datetime.timedelta(weeks=4)), path='/')


def destroy_cookie(name, self):
    self.response.set_cookie(name, "", expires=datetime.datetime.now(), path='/')


def get_cookie(name, self):
    if self.request.cookies.get(name):
        return self.request.cookies.get(name)


def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt(10))


def check_password(password, hashed):
    return bcrypt.hashpw(password, hashed)
