from os import getenv
from http.server import HTTPServer

from poke_server.http.server import PokeHTTPRequestHandler
from poke_server.http.handler.PokeHandler import PokeHandler

from logging import basicConfig, getLogger, INFO
from os import getenv

basicConfig(level=INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = getLogger(__name__)


def main():
    SERVER_INTERFACE = getenv("POKE_BIND_IP", "0.0.0.0")
    SERVER_PORT = int(getenv("POKE_PORT", 8081))

    # we're missing some redirection "/index" => "/"
    PokeHTTPRequestHandler._router.get("/", PokeHandler.index)
    PokeHTTPRequestHandler._router.get("/index", PokeHandler.index)
    PokeHTTPRequestHandler._router.get("/pokemon", PokeHandler.get_pokemon)
    logger.info("initialized routes")

    server = HTTPServer((SERVER_INTERFACE, SERVER_PORT), PokeHTTPRequestHandler)

    logger.info(f"initialized web server: {SERVER_INTERFACE}:{SERVER_PORT}")
    server.serve_forever()
