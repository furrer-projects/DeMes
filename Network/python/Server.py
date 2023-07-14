from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import threading
class DeMesServer:
    def __init__(self, port=8011, hostName="localhost"):
        self.port = port
        self.hostName = hostName
        self.webServer = HTTPServer((self.hostName, self.port), DeMesServerHandler)
    def start(self):
        print("Starting Server -> http://%s:%s" % (self.hostName, self.port))
        try:
            thread = threading.Thread(target=self.webServer.serve_forever)
            thread.daemon = True
            thread.start()
        except Exception:
            print('error on server execution')
            pass
    def stop(self):
        self.webServer.shutdown()
        print('Server Stopped...')


class DeMesServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        result = {}
        result['msg'] = 'request executed'
        result['code'] = 100 #initialization code
        result['timestamp'] = time.time_ns()
        self.wfile.write(bytes(json.dumps(result), 'utf-8'))

