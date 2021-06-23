from src.utils.mysql_utils import connect_to_mysql, connect_to_db, create_db, create_customer_table, \
    create_text_table, close_connection
from conf.connect import database_name

# connect to mysql
mysql_connection = connect_to_mysql()

# create db if not exist
create_db(mysql_connection, database_name)

# connect to database
db_connection = connect_to_db()

# create customer table
create_customer_table(db_connection)

# create text table
create_text_table(db_connection)


# close connection
close_connection(mysql_connection)
