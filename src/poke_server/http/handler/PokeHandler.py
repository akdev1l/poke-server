#!/usr/bin/env python

from logging import getLogger

from poke_server.http.router import HTTPResponse

logger = getLogger(__name__)


class PokeHandler:
    @classmethod
    def index(cls, path, body):  # PokeHandler.index("/", "{}")
        logger.info("poke-handler executing")
        return HTTPResponse("hello poke", 200)

    @classmethod
    def get_pokemon(cls, path, body):
        logger.info("fetching pokemon")
        return HTTPResponse({"id": 1}, 200)

    @classmethod
    def update_pokemon(cls, path, body):
        logger.info("updating pokemon")
        return HTTPResponse({"id": 1}, 200)

    @classmethod
    def get_and_update_pokemon(cls, path, body):
        cls.get_pokemon(path, body)
        cls.update_pokemon(path, body)
