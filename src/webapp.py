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
import tkinter
import interface

KEEP_RUNNING = True

my_client_id = ''#put your client id
my_client_secret = ''#put your client secret
authorization_url = 'https://oauth.lichess.org/oauth/authorize'
access_token_url = 'https://oauth.lichess.org/oauth'
base_url = 'https://lichess.org/'
redirect_uri = 'http://127.0.0.1:8080'
scope = 'bot:play preference:read preference:write email:read challenge:read challenge:write tournament:write puzzle:read'
web_app_url = 'https://lichess.org/account/oauth/app/create'
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
        
    global thread
    thread.join()
    print(thread)

def bt0(self):
    webbrowser.open_new(web_app_url)
def bt1(self):
    try:
        f = open("../text/client_inf.txt","r")
        global my_client_id
        my_client_id = f.readline().strip()
        global my_client_secret
        my_client_secret = f.readline().strip()
        f.close()
        service = OAuth2Service(
               name='Bot app',
               client_id=my_client_id,
               client_secret=my_client_secret,
               access_token_url=access_token_url,
               authorize_url=authorization_url,
               base_url=base_url)
        thread2 = Thread(target = threaded_function, args = (service, ))
        global thread
        thread = thread2     
        run()
        data = {'code': code,'grant_type': 'authorization_code','redirect_uri': redirect_uri}
        session = service.get_auth_session(data=data, decoder=new_decoder)
        r = session.get('/api/account')
        f = open("../bin/"+str(json.loads(str(r.content.decode('utf-8')))["username"])+".bin","wb")
        pickle.dump(session, f)
        f.close()
    except:
        window = tkinter.Tk()
        window.title("Error")
        interface.center_window(window,200,200)
        label = tkinter.Label(window, text = "You Need Client Credentials").pack()
        label = tkinter.Label(window, text = "try to create a webApp!").pack()


