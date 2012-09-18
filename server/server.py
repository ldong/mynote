#!/usr/bin/env python

import BaseHTTPServer
import uri
import sys
import os
import os.path
import re
import config
import urllib

class IntegratedHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.path = urllib.unquote(self.path)
        self.path = self.path.decode('UTF-8')
        self.dispatch()

    def perform_handler(self, handler, kargs):
        module_name, ignore, method_name = handler.rpartition('.')
        if module_name:
            tmp = __import__(name=module_name, fromlist=[ method_name ])
            method = getattr(tmp, method_name)
            method(self, **kargs)
        else:
            raise Exception('handler must be in a module')

    def dispatch(self):
        for pattern, handler in uri.uri_mapping:
            print pattern, handler
            matcher = re.match(pattern, self.path)
            if matcher:
                self.perform_handler(handler, matcher.groupdict())
                return
        self.send_response(404)
        self.end_headers()
        self.wfile.write('no handler for %s' % self.path)

    def simple_response(self, headers={}, body=''):
        self.send_response(200)
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)


def start(static_dir, template_dir, note_dir):
    config.static_dir = static_dir
    config.template_dir = template_dir
    config.note_dir = note_dir

    server = BaseHTTPServer.HTTPServer(('127.0.0.1', 8000), IntegratedHTTPRequestHandler)
    server.serve_forever()

