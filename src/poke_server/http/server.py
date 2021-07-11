from http.server import (
    BaseHTTPRequestHandler
)
from json import (
    load,
    dumps
)
from logging import (
    basicConfig,
    getLogger,
    INFO
)
from re import fullmatch
from urllib.parse import (
    parse_qs,
    urlparse
)

from poke_server.http.router import HTTPRouter

basicConfig(
    level=INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = getLogger(__name__)

POKEMON_JSON_DB = "./data/pokemon.json"

class PokeHTTPRequestHandler(BaseHTTPRequestHandler):
    _router = HTTPRouter()

    def send_headers(self):
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def send_http_response(self, response, response_code=200):
        self.send_response(response_code)
        self.send_headers()
        self.wfile.write(dumps(response, default=lambda o: o.__dict__).encode("utf-8"))
        
    def do_GET(self):
        matching_routes = [
            route
            for route in self._router.get_routes("GET")
            if route.path == self.path
        ]
        logger.info(f"found {len(matching_routes)} matching routes")

        if len(matching_routes) == 0:
            logger.warning(f"route not found: GET - {self.path}")
            self.send_http_response({"path": self.path, "error": 404}, 404)
        else:
            response = matching_routes[0].handler(self.path, {})
            self.send_http_response(response, 200)

    def do_POST(self):
        parsed_url = urlparse(self.path)
        logger.info(f"parsed request url: {self.path} -> {parsed_url}")

        route_handler = self._router.route("POST", parsed_url.path)
        query_params = parse_qs(parsed_url.query)
        if 'Content-Length' in self.headers:
            body_length = int(self.headers.get('Content-Length', 0))
            if body_length > 0:
                req_body = self.rfile.read(body_length).decode("utf-8")
                logger.info(f"request body length: {len(req_body)}")
                logger.info(f"executing handler: {route_handler}")
                body_params = parse_qs(req_body)

                route_handler(
                self.send_http_response({"body": req_body}, 200)
                return

        self.send_http_response("internal error", 500)
