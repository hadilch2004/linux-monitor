from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base #Base knows every table you've defined.

DATABASE_URL = "postgresql+psycopg://user@localhost/linux_monitor" #local host if its ur computer ur psgr is on
#only for beginners, ur user name should not usually be hardcoded 
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)