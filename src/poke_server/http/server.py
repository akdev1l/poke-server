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

basicConfig(
    level=INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = getLogger(__name__)

POKEMON_JSON_DB = "/var/lib/poke_server/pokemon.json"

class PokeHTTPRequestHandler(BaseHTTPRequestHandler):
    def response_json(self, response):
        self.send_response(200);
        self.send_header(
            "Content-Type", "text/plain; charset=utf-8"
        )
        self.send_header(
            "Access-Control-Allow-Origin", "*"
        )
        self.end_headers()
        self.wfile.write(dumps(response).encode("utf-8"))
        
    def do_GET(self):
        # poke-back.hq.akdev.xyz:8081/pokemon/${id}

        # 1. read pokemon.json file
        # 2. search for pokemon id == pokemon_id
        # 3. return json.dumps(pokemon_found)


        if "/pokemon" in self.path:
            pokemon_request_id = int(self.path.split("/")[-1])
            logger.info(f"processing pokemon ID: {pokemon_request_id}")
            with open(POKEMON_JSON_DB) as pokemon_db:
                pokemons = load(pokemon_db)
                logger.info(f"found {len(pokemons)} pokemons")
                logger.info(f"pokemon_request_id = {pokemon_request_id}")
                pokemon_found = [
                    pokemon
                    for pokemon in pokemons
                    if pokemon["id"] == pokemon_request_id
                ]
                if len(pokemon_found) > 0:
                    logger.info(f"found {len(pokemon_found)} pokemons with id {pokemon_request_id}")
                    self.send_response(200);
                    self.send_header(
                        "Content-Type", "text/plain; charset=utf-8"
                    )
                    self.send_header(
                        "Access-Control-Allow-Origin", "*"
                    )
                    self.end_headers()
                    self.wfile.write(dumps(pokemon_found[0]).encode("utf-8"))
                else:
                    logger.warning(f"pokemon not found with id {pokemon_request_id}")
                    self.send_response(404);

        else:
            self.send_response(404);
                    

        
