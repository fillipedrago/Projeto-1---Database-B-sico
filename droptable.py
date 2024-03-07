# Used if it's necessary to drop the table

import psycopg2

try:
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=myfirstdb user=postgres password=PI314159")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

try:
    cur.execute("DROP TABLE IF EXISTS students")
except psycopg2.Error as e:
    print(e)

print("Table dropped succefully")

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

