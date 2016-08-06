import time

from google.appengine.ext import ndb

import auth
import helpers


def generate_auth_token(user_key):
    return auth.generate_auth_token(user_key)


def get_current_user(self):
    token = helpers.get_cookie('auth_token', self)
    return get_user_from_token(token)


def get_user_from_token(token):
    try:
        payload = auth.decode_auth_token(token)
        if int(payload['exp']) > int(time.time()):
            url_key_str = payload['user_key']
            return get_user_by_url_key(url_key_str)
        return False
    except:
        return False


def set_login_cookie(user, self):
    cookie_value = auth.generate_auth_token(user.key.urlsafe())
    helpers.set_cookie('auth_token', cookie_value, self)


def get_user_by_url_key(url_key_string):
    user = ndb.Key(urlsafe=url_key_string)
    return user.get()

