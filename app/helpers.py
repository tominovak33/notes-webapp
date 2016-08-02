import templates
import datetime


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
