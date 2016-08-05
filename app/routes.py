import handlers

ROUTES = [
    ('/', handlers.HomeHandler),
    ('/admin', handlers.AdminHomeHandler),
    ('/notes', handlers.NotesHandler),
    ('/login', handlers.LoginHandler),
    ('/register', handlers.RegistrationHandler),
    ('/note/(.*)', handlers.NoteHandler),
    ('/(.*)', handlers.NotFoundHandler)
]
