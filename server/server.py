from http.server import BaseHTTPRequestHandler
import json
import cgi
import os

from volume_control import set_volume_percent

dirname = os.path.dirname(__file__)


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back a Hello world message
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        file_path = os.path.join(dirname, "index.html")
        with open(file_path, "rb") as f:
            html = f.read()
            self.wfile.write(html)

    # POST echoes the message adding a JSON field
    def do_POST(self):
        volume = int(self.path.replace("/", ""))
        set_volume_percent(volume)

        json_str = f'{{"volume": {volume}}}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json_str.encode(encoding="utf_8"))
