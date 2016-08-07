import jwt
import time

import config


secret_key = config.JWT_SECRET_KEY

audience = "http://notes.tomi33.co.uk"
algorithm = 'HS256'


def generate_auth_token(user_key):
    payload = {
        'iss': 'me@tomi33.co.uk',
        'sub': 'me@tomi33.co.uk',
        'aud': audience,
        'iat': int(time.time()),
        'exp': int(time.time() + 3600*24*31),
        'user_key': user_key
    }

    encoded = jwt.encode(payload, secret_key, algorithm=algorithm)

    return encoded


def decode_auth_token(token):
    # return jwt.decode(token, secret_key, audience='http://tomi-dev.tech')
    try:
        return jwt.decode(token, secret_key, audience=audience, algorithms=algorithm)
    except:
        return False
