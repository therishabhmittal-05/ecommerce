import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv("DBUSER")
db_pass = os.getenv("DBPASS")
SQLALCHEMY_DATABASE_URL = f"postgresql://{db_user}:{db_pass}@62.171.138.241:5432/bet_ecommerce"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
) 
SessionLocal = sessionmaker(autcomplete = False,  autoflush=False, bind=engine)

Base = declarative_base()