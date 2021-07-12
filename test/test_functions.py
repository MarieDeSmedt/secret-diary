import sqlalchemy.connectors

from src.utils.mysql_utils import *

test_database_name = "test_secret_diary"

# Test the connexion to db.
def test_db_connection():
    mysql_connection = connect_to_mysql()
    db_cursor = create_db(mysql_connection, test_database_name)
    db_connection = connect_to_db(test_database_name)

    assert isinstance(db_connection ,sqlalchemy.connectors.Connector)