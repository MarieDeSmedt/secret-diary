from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pytest
import asyncio
from api import models
from src.utils.mysql_utils import *

test_database_name = "test_secret_diary"

@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()



@pytest.mark.asyncio
@pytest.fixture(scope='module')
async def create_db(event_loop):

    print("Creating db")
    mysql_connection = connect_to_mysql()
    db_cursor = create_db(mysql_connection,test_database_name)
    db_connection = connect_to_db(test_database_name)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_connection)

    Base = declarative_base()

    models.Base.metadata.create_all(bind=db_connection)


    populate_table = """
    INSERT INTO customer(name,firstname, information)
    VALUES("de smedt","marie", "test")
    """
    db_cursor.execute(populate_table)
    db_connection.commit()

    yield db_cursor