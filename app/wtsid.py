import pandas as pd
import json

from fastapi import FastAPI
from src.start.to_start import db_connection, mysql_connection

id = 1

df = pd.read_sql('SELECT * FROM customer WHERE id_customer = {}'.format(id), con=db_connection)
result = df.to_json(orient="index")
response = json.loads(result)

print(response)