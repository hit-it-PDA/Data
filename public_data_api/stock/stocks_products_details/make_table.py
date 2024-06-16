import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, select
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.dialects.mysql import DOUBLE
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

# MySQL 연결 정보
mysql_user = os.environ.get('MYSQL_USER')
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_host = os.environ.get('MYSQL_HOST')
mysql_port = os.environ.get('MYSQL_PORT', 3306)
mysql_db = os.environ.get('MYSQL_DB')


# SQLAlchemy 엔진 생성
engine = create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}')
#engine = create_engine('mysql://hitit-user:hitit1234!@hitit-db-mydata.c9oy8g6q0v76.ap-northeast-2.rds.amazonaws.com:3306/hitit')

# CSV 파일 읽기
# df = pd.read_csv('./db/stocks_products_details.csv')

# 메타데이터 객체 생성
metadata = MetaData()

# result = engine.execute('select * from stocks_products')

print(1)
# 테이블 생성 쿼리
create_table_query = """
CREATE TABLE stocks_products_details (
    date Date,
    stock_code VARCHAR(255),
    price INT,
    amount INT,
    volume INT,
    per DOUBLE,
    eps DOUBLE,
    PRIMARY KEY (date, stock_code)
)
"""

# 테이블 생성
engine.execute(create_table_query)

print(2)

# FOREIGN KEY (stock_code) REFERENCES stocks_products(stock_code)

# stocks_products_details 테이블 생성
# stocks_products_details = Table('stocks_products_details', metadata,
#                                 Column('date', VARCHAR(6), primary_key=True),
#                                 Column('code', VARCHAR(20), ForeignKey('stocks_products.code')),
#                                 Column('price', Integer),
#                                 Column('amount', Integer),
#                                 Column('volume', Integer),
#                                 Column('per', DOUBLE),
#                                 Column('eps', DOUBLE)
#                                 )



# # 테이블 생성 (기존 테이블이 있으면 삭제 후 생성)
# with engine.connect() as connection:
#     stocks_products_details.drop(engine, checkfirst=True)  # 기존 테이블 삭제
#     stocks_products_details.create(engine)  # 새로운 테이블 생성

# stocks_products 테이블 불러오기
#stocks_products = Table('stocks_products', metadata, autoload_with=engine)



# 데이터베이스에 데이터 삽입
#with engine.connect() as connection:
#    df.to_sql(name='stocks_products_details', con=connection, if_exists='append', index=False)

#print('CSV 파일이 MySQL 데이터베이스에 저장되었습니다: 테이블명 - stocks_products_details')
