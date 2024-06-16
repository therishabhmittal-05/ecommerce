from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://shrihari:shrihari@62.171.138.241:5432/bet_ecommerce"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
) 
SessionLocal = sessionmaker(autcomplete = False,  autoflush=False, bind=engine)

Base = declarative_base()