import mysql.connector
from sqlalchemy import create_engine
from conf.connect import mysql_user, mysql_host, mysql_password, database_name


def connect_to_mysql():
    """
    connect to mysql
    :return: cursor
    """
    mysql_connection = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password)

    return mysql_connection


def create_db(mysql_connection, database_name):
    """
    create database if not exist
    :param cursor: from connect_to_mysql()
    :param database_name: from conf
    :param mysql_user: from conf
    :param mysql_password: from conf
    :return:
    """
    cursor = mysql_connection.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS """ + database_name)
    cursor.execute("""USE """ + database_name)


def connect_to_db():
    db_connection = create_engine(
        'mysql+pymysql://{0}:{1}@localhost/{2}'.format(mysql_user, mysql_password, database_name))
    return db_connection


def create_customer_table(db_connection):
    # Creating table as per requirement
    sql = '''CREATE TABLE IF NOT EXISTS customer(
    id_customer INT NOT NULL,
    name VARCHAR(32) NOT NULL,
    firstname VARCHAR(32),
    information VARCHAR(255),
    creation_date DATE NOT NULL,
    modification_date DATE,
    deleted_date DATE,
    PRIMARY KEY (id_customer)
    )'''
    db_connection.execute(sql)


def create_text_table(db_connection):
    # Creating table as per requirement
    sql = '''CREATE TABLE IF NOT EXISTS text(
        id_text INT NOT NULL,
        content TEXT NOT NULL,
        creation_date DATE NOT NULL,
        modification_date DATE,
        delete_date DATE,
        id_customer INT NOT NULL,
        PRIMARY KEY (id_text),
        FOREIGN KEY (id_customer) REFERENCES customer(id_customer)        
        )'''
    #
    db_connection.execute(sql)


def create_feeling_table(db_connection):
    # Creating table as per requirement
    sql = '''CREATE TABLE IF NOT EXISTS feeling(
        id_feeling INT NOT NULL,
        first_feeling TEXT NOT NULL,
        first_pourcentage FLOAT NOT NULL,
        second_feeling TEXT NOT NULL,
        second_pourcentage FLOAT NOT NULL,
        third_feeling TEXT NOT NULL,
        third_pourcentage FLOAT NOT NULL,
        creation_date DATE NOT NULL,
        modification_date DATE,
        delete_date DATE,
        id_text INT NOT NULL,
        PRIMARY KEY (id_feeling),
        FOREIGN KEY (id_text) REFERENCES text(id_text)
        )'''
    db_connection.execute(sql)


def close_connection(mysql_connection):
    # Closing the connection
    mysql_connection.close()
