import pandas as pd
from sqlalchemy import create_engine
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

# CSV 파일 읽기
df = pd.read_csv('./db/security_stocks.csv', dtype={'stock_code': str})

# 데이터베이스에 데이터 삽입
df.to_sql(name='security_stocks', con=engine, if_exists='append', index=False)

print('CSV 파일이 MySQL 데이터베이스에 저장되었습니다: 테이블명 - security_stocks')
