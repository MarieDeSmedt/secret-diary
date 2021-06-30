from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from conf.connect import mysql_user, mysql_password, database_name
from src.utils.mysql_utils import connect_to_mysql, create_db, connect_to_db
from conf.connect import database_name
from api import models

# connect to mysql
mysql_connection = connect_to_mysql()

# create db if not exist
create_db(mysql_connection, database_name)

# connect to database
db_connection = connect_to_db()
#
# # create customer table
# create_customer_table(db_connection)
#
# # create text table
# create_text_table(db_connection)

# SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_user, mysql_password, database_name)
#
# db_connection = create_engine(
#     SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_connection)

Base = declarative_base()













#

#

#
#
# # close connection
# close_connection(mysql_connection)
