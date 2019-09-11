from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from rauth import OAuth2Service
from requests_oauthlib import OAuth2Session
from threading import Thread
from time import sleep
import json
import webbrowser
import pickle
import ast


KEEP_RUNNING = True

my_client_id = ''#put your client id
my_client_secret = ''#put your client secret
authorization_url = 'https://oauth.lichess.org/oauth/authorize'
access_token_url = 'https://oauth.lichess.org/oauth'
base_url = 'https://lichess.org/'
redirect_uri = 'http://127.0.0.1:8080'
scope = 'bot:play preference:read preference:write email:read challenge:read challenge:write tournament:write puzzle:read'

thread = None
code = None

def threaded_function(arg):
    service = arg
    params = {'scope': scope,
    'redirect_uri': redirect_uri,
    'response_type': 'code'}
    url = service.get_authorize_url(**params)
    webbrowser.open_new(url)

def keep_running():
    return KEEP_RUNNING
    
def new_decoder(payload):
    return json.loads(payload.decode('utf-8'))
    
class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        global code
        code = parse_qs(self.path[2:])['code'][0]
        global KEEP_RUNNING
        KEEP_RUNNING = False

def run(server_class=HTTPServer, handler_class=GP, port=8080):
    server_address = ('localhost', 8080)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:8080...')
    while keep_running():
        thread.start()
        httpd.handle_request()
    thread.join()

if __name__ == "__main__":
    service = OAuth2Service(
           name='Bot app',
           client_id=my_client_id,
           client_secret=my_client_secret,
           access_token_url=access_token_url,
           authorize_url=authorization_url,
           base_url=base_url)
    thread = Thread(target = threaded_function, args = (service, ))     
    run()
    data = {'code': code,'grant_type': 'authorization_code','redirect_uri': redirect_uri}
    session = service.get_auth_session(data=data, decoder=new_decoder)
    r = session.get('/api/account')
    f = open(str(json.loads("../bin/"+str(r.content.decode('utf-8')))["id"])+".bin","wb")
    pickle.dump(session, f)
    f.close() #save session of the current id player
