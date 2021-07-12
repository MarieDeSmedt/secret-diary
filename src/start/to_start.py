from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.utils.mysql_utils import connect_to_mysql, create_db, connect_to_db
from conf.connect import database_name

# FIRST FILE TO RUN TO CONNECT TO MYSQL AND TO CREATE DATABASE


# connect to mysql
mysql_connection = connect_to_mysql()

# create db if not exist
create_db(mysql_connection, database_name)

# connect to database
db_connection = connect_to_db(database_name)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_connection)

Base = declarative_base()













#

#

#
#
# # close connection
# close_connection(mysql_connection)
