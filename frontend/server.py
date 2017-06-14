#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple HTTPS server.

Development only.

options:
    --host - server IP address, default: 0.0.0.0 # listening all interfaces
    --port - 4443, default: 4443 # 443 requires root privileges
example:
    python server.py --host=0.0.0.0 --port=4443
"""
import ssl
import argparse

try:
    from http.server import HTTPServer, SimpleHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer
    from SimpleHTTPServer import SimpleHTTPRequestHandler

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='0.0.0.0', help='server IP address')
parser.add_argument('--port', type=int, default=4443, help='port to listen')
args = parser.parse_args()


httpd = HTTPServer((args.host, args.port), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True,
                               keyfile='../key.pem', certfile='../cert.pem')

print('HTTPS server at https://{}:{}/\nCtrl+C to Quit.'.format(args.host, args.port))
httpd.serve_forever()

