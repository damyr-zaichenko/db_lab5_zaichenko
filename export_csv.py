import csv
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'jobs_database'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cur = conn.cursor()


tables = ["Comic", "Writer", "Written"]

for table in tables:
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()

    csv_file_path = f"{table}.csv"

    with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([desc[0] for desc in cur.description])
        csv_writer.writerows(rows)