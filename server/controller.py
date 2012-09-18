import markdown
import os
import json
import config
import os.path
import template_engine
import utils
import urllib
import logging

log = logging.getLogger('controller')

def walk_dir(base, link_prefix=''):
    '''
        deep first search
        level can filter top directory
    '''
    ret = []
    files = os.listdir(unicode(base))
    for f in files:
        path = os.path.join(base, f)
        if os.path.isdir(path):
            link = link_prefix + '/' + urllib.quote(utils.encode(f))
            result = walk_dir(path, link)
            ret.append((f, link, result))
    return tuple(ret)

def directories(handler):
    '''
    walk on config.note_dir and list all files
    '''
    result = walk_dir(config.note_dir)

    html = template_engine.render('directories.html', {'result': result})
    headers = {
            'Content-Type': 'text/html;charset=UTF-8',
            'Content-Length': len(html)
            }
    handler.simple_response(headers, html)

def detail(handler, note):
    local_path = os.path.join(config.note_dir, note)
    if not os.path.exists(local_path):
        handler.send_response(404)
        return
    with open(local_path) as f:
        md = f.read()
        md = utils.unicode(md)
    content = markdown.markdown(md, ['toc'])
    html = template_engine.render('detail.html', {'content':content})
    headers = {
            'Content-Type': 'text/html;charset=UTF-8',
            'Content-Length': len(html)
            }
    handler.simple_response(headers, html)

def create_link(relative_path):
    words = relative_path.split(os.path.sep)
    words = [ urllib.quote(utils.encode(w)) for w in words if w ]
    return '/'.join(words)

def list_note(handler, dir):
    '''
    dir is unicode
    '''
    if not dir:
        dir = u'.'
    path = os.path.join(config.note_dir, translate_path(dir))
    log.debug('list note for path %s' % path)
    notes = []
    for dir, subdirs, subfiles in os.walk(path):
        for f in subfiles:
            if f.lower().endswith('md'):
                relative_path = os.path.join(dir[len(config.note_dir):], f)
                link = create_link(relative_path)
                notes.append((f, link))
    html = template_engine.render('list_note.html', {'notes':notes})
    headers = {
            'Content-Type': 'text/html;charset=UTF-8',
            'Content-Length': len(html)
            }
    handler.simple_response(headers, html)

def translate_path(path):
    '''
    translate uri path to local filesystem ath
    '''
    words = path.split(os.path.sep)
    words = filter(None, words)
    return os.path.sep.join(words)

