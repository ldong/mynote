
__all__ = ['uri_mapping']

uri_mapping = (
        (r'^/$', 'static.index'),
        (r'^/dirs/?$', 'controller.directories'),
        (r'^/notes/(?P<dir>.*)$', 'controller.list_note'),
        (r'^/note/(?P<path>.+\.(?:jpg|jpeg|png|gif))$', 'static.note_image'),
        (r'^/note/(?P<note>.+\.md)$', 'controller.detail'),
        (r'^/static/(?P<path>.+)$', 'static.static'),
        (r'^/(?P<path>favicon.ico)$', 'static.static')
        )

