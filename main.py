import psycopg2
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd

db_params = {
    'host': 'localhost',
    'database': 'jobs_database',
    'user': 'postgres',
    'password': 'postgres',
    'port': '5432'
}

# Create views directly in the queries
query_1 = '''
CREATE OR REPLACE VIEW view_writer_comics AS
SELECT
  w.writer_name,
  COUNT(DISTINCT wr.comic_id) AS total_comics_written
FROM
  Writer w
  JOIN Written wr ON w.writer_id = wr.writer_id
GROUP BY
  w.writer_id;

SELECT * FROM view_writer_comics;
'''

query_2 = '''
CREATE OR REPLACE VIEW view_comic_year AS
SELECT
  EXTRACT(YEAR FROM date) AS comic_year,
  COUNT(DISTINCT comic_id) AS total_comics
FROM
  Written
GROUP BY
  comic_year
ORDER BY
  comic_year;

SELECT * FROM view_comic_year;
'''

query_3 = '''
CREATE OR REPLACE VIEW view_comic_format AS
SELECT
  comic_format,
  COUNT(comic_id) AS total_comics
FROM
  Comic
GROUP BY
  comic_format;

SELECT * FROM view_comic_format;
'''

def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def print_query_results(query, result, cursor):
    print(f"\nQuery: {query}\n")
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(result, headers, tablefmt="pretty"))

def plot_bar_chart(data, x_label, y_label, title):
    x = [item[0] for item in data]
    y = [item[1] for item in data]

    plt.bar(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def main():
    connection = psycopg2.connect(
        user=db_params['user'],
        password=db_params['password'],
        dbname=db_params['database'],
        host=db_params['host'],
        port=db_params['port']
    )

    with connection.cursor() as cursor:
        result_1 = execute_query(cursor, query_1)
        result_1 = pd.DataFrame(result_1)

        def my_fmt(x):
            return '{:.1f}%\n({:.0f})'.format(x, result_1.shape[0] * x / 100)

        plt.figure(figsize=(14, 6))

        plt.subplot(131)
        plt.title("Number of comics per author")
        threshold = 3
        filtered_labels = result_1[1][result_1[1] >= threshold]
        filtered_x = result_1[0][result_1[1] >= threshold]
        pie_chart = plt.pie(x=filtered_labels, labels=filtered_x, autopct=my_fmt)
        for label in pie_chart[1]:
            label.set_fontsize(5)

        result_2 = execute_query(cursor, query_2)
        result_2 = pd.DataFrame(result_2)
        plt.subplot(132)
        plt.title("Number of comics per year")
        xticks = [result_2[0][i] for i in range(0, len(result_2[0]), 2)]
        print(xticks)
        plt.xticks(xticks, rotation=90, fontsize=7)
        plt.plot(result_2[0], result_2[1], linewidth=3)

        plt.subplot(133)
        plt.title("Comics by format")
        result_3 = execute_query(cursor, query_3)
        result_3 = pd.DataFrame(result_3)
        print(result_3[0])
        plt.bar(result_3[0], result_3[1])
        plt.xticks(rotation=90)

        plt.tight_layout()

        plt.show()

if __name__ == '__main__':
    main()
