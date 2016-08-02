import auth

def get_current_user():
    return False

def generate_auth_token(user_key):
    return auth.generate_auth_token(user_key)

token = generate_auth_token("000001")

print token

print "\n\n\n\n\n\n"

print auth.decode_auth_token(token)
