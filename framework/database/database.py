import os
from sqlalchemy import create_engine


def connect_pg():
    engine = create_engine(os.environ['PG_URI'])
    return engine
