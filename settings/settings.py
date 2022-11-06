from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


Faker.seed(1)
load_dotenv()


def sql_engine():
    username = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    database = os.environ["DB_NAME"]
    port = os.environ["DB_PORT"]
    host = os.environ["DB_HOST"]

    return create_engine(
        f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}", 
        echo=True
    )
    

ENGINE = sql_engine()
SESSION = sessionmaker(bind=ENGINE)
