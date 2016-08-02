import webapp2

from google.appengine.api import users  # Allow users to authentiucate with google. (used to authorise admin accounts)

from models import User as User
from models import Note as Note
import templates
import helpers
import abstractions


def login(required=False):
    def the_decorator(get_or_post_method):
        def get_logged_in_user(self, *args):
            self.user = False
            google_account = users.get_current_user()
            if google_account:
                if not User.get_by_user(google_account):
                    # register new user
                    user = User(id=google_account.user_id())
                    user.user_id = google_account.user_id()
                    user.email = google_account.email()
                    user.name = google_account.nickname()
                    user.put()
                self.user = User.get_by_id(google_account.user_id())
            else:
                if required:
                    self.error(403)
                    login_url = users.create_login_url(self.request.path)
                    return self.redirect(login_url)
            return get_or_post_method(self, *args)
        return get_logged_in_user
    return the_decorator


class HomeHandler(webapp2.RequestHandler):
    @login(False)
    def get(self):
        if self.user:
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Logout'

        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        template_values = {
            'user': self.user,
            'url': url,
            'url_link_text': url_link_text,
            'description': 'Notes App'
        }

        templates.render_page("home", template_values, self)


class AdminHomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {
            'user': user,
            'description': 'Notes App - Admin Area'
        }

        templates.render_page("admin", template_values, self)


class NotesHandler(webapp2.RequestHandler):
    @login(True)
    def get(self):
        notes_query = Note.query(Note.user == self.user.key)
        notes = notes_query.fetch()

        template_values = {
            'user': self.user,
            'notes': notes,
            'description': 'Notes App - Admin Area'
        }

        templates.render_page("notes/home", template_values, self)
        # get the users notes here
        return

    @login(True)
    def post(self):
        user = self.user
        if user:
            content = self.request.get('note')
            note = Note()
            note.content = content
            note.user = user.key
            note.put()

            # show confirmation of successful post creation
            template_values = {
                'message': 'Note created successfully'
            }

            templates.render_page("notes/created", template_values, self)
        else:
            # error about login
            return

        return


class NoteHandler(webapp2.RequestHandler):
    @login(True)
    def get(self, route):
        # get specific route
        return


class NotFoundHandler(webapp2.RequestHandler):
    def get(self, route):
        helpers.throw404(self)
