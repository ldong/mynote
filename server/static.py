import config
import os
import os.path
import utils

mimetypes = {
        'css': 'text/css',
        'js': 'application/x-javascript',
        'html': 'text/html; charset=UTF-8',
        'txt': 'text/plain; charset=UTF-8',
        'ico': 'image/x-icon',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif'
        }

def index(handler):
    static(handler, 'index.html')

def note_image(handler, path):
    local_path = _translate_path(config.note_dir, path)
    _send_file(handler, local_path)

def static(handler, path=''):
    local_path = _translate_path(config.static_dir, path)
    _send_file(handler, local_path)

def _send_file(handler, local_path):
    if os.path.exists(local_path):
        handler.send_response(200)
        mtype = _guess_type(local_path)
        if mtype:
            handler.send_header("Content-Type", mtype)

        with open(local_path, 'rb') as f:
            fs = os.fstat(f.fileno())
            handler.send_header("Content-Length", str(fs[6]))
            handler.send_header("Last-Modified", handler.date_time_string(fs.st_mtime))
            handler.end_headers()
            handler.wfile.write(f.read())
    else:
        handler.send_response(404)
        handler.end_headers()
        absolute_path = os.path.abspath(local_path)
        handler.wfile.write('Could not find file %s' % utils.encode(absolute_path))

def _translate_path(base_path, path):
    relative_path = path.lstrip('/')
    return os.path.join(base_path, relative_path)


def _guess_type(path):
    ext = os.path.splitext(path)[1]
    if not ext[1]:
        return None
    ext = ext[1:]
    mtype = mimetypes.get(ext)
    return mtype
    

