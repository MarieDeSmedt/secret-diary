import pytest
import sys
from mysql.connector import IntegrityError

def test_acces_db(create_db):
    create_db.execute("SELECT * from customer")
    rs = create_db.fetchall()
    assert len(rs)>0


