import psycopg2

# Host 127.0.0.1 é o local host
try:
    conn = psycopg2.connect("host=127.0.0.1 port=5433 dbname=postgres user=postgres password=PI314159")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

""" Por padrão, todas as ações numa conexão com database através de DB API
2.0 devem ser commitadas. Setando um autocommit, deixa de haver essa
necessidade.
"""
conn.set_session(autocommit=True)

try:
    cur.execute("create database myfirstdb")
except psycopg2.Error as e:
    print(e)