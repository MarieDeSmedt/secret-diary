import pandas as pd
import json
from src.start.to_start import db_connection

df = pd.read_sql('SELECT * FROM {}'.format("customer"), con=db_connection)
result = df.to_json(orient="index")
print(type(result))

response = json.loads(result)
print(type(response))

result = json.dumps(response, indent=4)
print(result)