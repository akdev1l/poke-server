#!/usr/bin/env python
from logging import (
    getLogger,
)
from re import fullmatch
from sys import exit

logger = getLogger(__name__)


class HTTPResponse:
    def __init__(self, payload, return_code=200):
        self.payload = payload
        self.return_code = return_code


# class HTTPHandler:
#    @staticmethod
#    def handle(path, data):
#        logger.info(f"unimplemented route: {path}")
#        return HTTPResponse(
#            "not implemented",
#            404
#        )


class HTTPRoute:
    def __init__(self, path, handler):
        self.path = path
        self.handler = handler


class HTTPRouter:
    def __init__(self):
        self._routes = {
            "GET": [],  # /pokemon/1, /pokemon/1
            "POST": [],
            "PUT": [],
            "PATCH": [],
            "DELETE": [],
        }

    def _register(self, method, path, handler):
        new_route = HTTPRoute(path, handler)

        if any(route.path == new_route.path for route in self._routes[method]):
            logger.error("found duplicate route at: {method} -> {new_route.path}")
            exit(1)

        self._routes[method].append(new_route)

    def route(self, method, path):
        for http_route in self._routes[method]:
            if http_route.path == path:
                # if route_match := fullmatch(http_route.path, path):
                return http_route.handler
        # if not found ?

    def get(self, path, handler):
        self._register("GET", path, handler)

    def post(self, path, handler):
        self._register("POST", path, handler)

    def get_routes(self, method):
        return self._routes[method]
