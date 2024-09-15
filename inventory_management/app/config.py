import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@host:port/dbname')
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=300)