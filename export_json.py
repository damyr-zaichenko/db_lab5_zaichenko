import json
import psycopg2
from datetime import date

username = 'postgres'
password = 'postgres'
database = 'jobs_database'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables = cur.fetchall()

all_data = {}

for table in tables:
    table_name = table[0]

    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    all_data[table_name] = []

    for row in rows:
        row_dict = {}
        for i, desc in enumerate(cur.description):
            # Convert date objects to string using isoformat()
            if isinstance(row[i], date):
                row_dict[desc[0]] = row[i].isoformat()
            else:
                row_dict[desc[0]] = row[i]
        all_data[table_name].append(row_dict)

json_file_path = "all_data.json"

with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, indent=2)

cur.close()
conn.close()
