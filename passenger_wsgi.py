import os
import sys
import requests

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'Hello people!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    resp = 'empty'
    response = '\n'.join([message, version, resp])
    return [response.encode()]
