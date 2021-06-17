import mysql.connector

from sqlalchemy import create_engine
from conf.connect import mysql_user, mysql_host, mysql_password, database_name


def connect_to_mysql():
    """
    connection to mysql and create database
    :return: db_connection
    """
    mydb = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password)
    cursor = mydb.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS """ + database_name)
    cursor.execute("""USE """ + database_name)
    db_connection = create_engine(
        'mysql+pymysql://{0}:{1}@localhost/{2}'.format(mysql_user, mysql_password, database_name))
    return db_connection


# test2
