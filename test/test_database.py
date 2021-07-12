

def test_acces_db(init_db):
    init_db.execute("SELECT * from customer")
    rs = init_db.fetchall()
    assert len(rs)>0


