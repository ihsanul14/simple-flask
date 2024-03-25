import os
from sqlalchemy import create_engine


class Database:
    def connect_pg(self):
        engine = create_engine(os.environ['PG_URI'])
        return engine
