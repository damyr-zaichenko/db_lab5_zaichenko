import csv
import psycopg2
import uuid

username = 'postgres'
password = 'postgres'
database = 'jobs_database'

INPUT_CSV_FILE = 'Marvel_Comics.csv'

delete_query = '''
DELETE FROM written;
DELETE FROM writer;
DELETE FROM comic;
'''

query_insert_comic = '''
INSERT INTO comic (comic_id, comic_name, comic_price, comic_format) VALUES (%s, %s, %s, %s)
ON CONFLICT (comic_id) DO NOTHING;
'''

query_insert_writer = '''
INSERT INTO writer (writer_id, writer_name) VALUES (%s, %s)
ON CONFLICT (writer_id) DO NOTHING;
'''

query_insert_written = '''
INSERT INTO written (date, writer_id, comic_id) VALUES (%s, %s, %s);
'''

def generate_uuid():
    return str(uuid.uuid4())

unique_writers = set()
unique_comics = set()

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(delete_query)

    with open(INPUT_CSV_FILE, 'r', encoding='utf-8') as inf:
        reader = csv.DictReader(inf)
        id = 1
        for row in reader:
            # Generate unique IDs for comic and writer
            comic_id, writer_id = id, id
            id += 1
            if id >= 150: break

            writers = list(row['writer'].split(', '))

            for writer in writers:

                # Check if writer with the same name already exists
                cur.execute("SELECT writer_id FROM writer WHERE writer_name = %s", (writer,))
                existing_writer = cur.fetchone()

                if existing_writer:
                    writer_id = existing_writer[0]
                else:
                    cur.execute(query_insert_writer, (writer_id, writer))

                publish_date = row['publish_date'] if row['publish_date'] is not None else '1970-01-01'

                cur.execute(query_insert_comic, (comic_id, row['issue_title'], row['Price'], row['Format']))
                cur.execute(query_insert_written, (publish_date, writer_id, comic_id))

conn.commit()
