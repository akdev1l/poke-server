from http.server import HTTPServer

from poke_server.http.server import PokeHTTPRequestHandler

def main():
    server = HTTPServer(("", 8081), PokeHTTPRequestHandler)
    server.serve_forever()
