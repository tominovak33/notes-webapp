import handlers

ROUTES = [
    ('/', handlers.HomeHandler),
    ('/admin', handlers.AdminHomeHandler),
    ('/notes', handlers.NotesHandler),
    ('/note/(.*)', handlers.NoteHandler),
    ('/(.*)', handlers.NotFoundHandler)
]
