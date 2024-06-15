
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def connect_db():
    # load .env
    load_dotenv()

    username = os.environ.get('db_username')
    password = os.environ.get('db_password')
    hostname = os.environ.get('db_hostname')
    schema = os.environ.get('db_schema')

    # sql로 저장
    db_connection_str = f'mysql+pymysql://{username}:{password}@{hostname}:3306/{schema}'
    db_connection = create_engine(db_connection_str)
    db_connection.connect()
    return db_connection

if __name__ == "__main__":
    connect_db()
