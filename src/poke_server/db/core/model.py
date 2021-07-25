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

class DbModel:
    def get_by_id(self, id):
        logger.error("not implemented")

    @classmethod
    def get_table_name(cls):
        logger.info("get_table_name: {cls.__name__.upper()}")
        return cls.__name__.upper()
