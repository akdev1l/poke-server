from logging import (
    basicConfig,
    getLogger,
    INFO
)

from poke_server.db.core.model import DbModel

basicConfig(
    level=INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = getLogger(__name__)

class Pokemon(DbModel):
    def get_by_id(self, id):
        
