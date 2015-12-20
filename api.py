import os
import yaml
from datetime import datetime
from gevent.wsgi import WSGIServer
from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api, reqparse, request, abort

version = '0.1'

def make_post(cmd, desc, mode, tag):
    if len(desc) > 80:
        print('description too long')
        return False

    meta = { 'title': cmd,
             'date': datetime.utcnow(),
             'Tags': [tag],
             'Mode': mode }

    return [ meta, desc ]

class Version(Resource):
    def get(self):
        return {'version': 'v%s' % version}, 200

class SubmitCommand(Resource):
    def post(self):
        args = self._parse()

        post = make_post(args['cmd'], args['desc'], args['mode'], args['tag'])
        print(yaml.dump_all(post))
        #if not ok:
        #return make_error(400, result)

        return {'ok': True}, 200

    def _parse(self):
        parser = reqparse.RequestParser()
        parser.add_argument('cmd')
        parser.add_argument('desc')
        parser.add_argument('tag')
        parser.add_argument('mode')
        return parser.parse_args()

class VimCommandsApi(object):
    def __init__(self, debug=False):
        self.app = Flask('vimcommands')
        self.api = Api(self.app)
        self.app.config['DEBUG'] = debug
        self.app.config['ERROR_404_HELP'] = False
        self.api.add_resource(Version, '/version')
        self.api.add_resource(SubmitCommand, '/submit')

        @self.app.errorhandler(404)
        def not_found(error):
            return make_response("", 404)

    def start_server(self, listen_port=8000):
        print('VimCommands API starting on 0.0.0.0:%s' % listen_port)
        http_server = WSGIServer(('', listen_port), self.app)
        http_server.serve_forever()

if __name__ == '__main__':
    v = VimCommandsApi(debug=True)
    v.start_server()
