import psycopg2

conn = psycopg2.connect("dbname='postgres' user='postgres'  host='localhost'")
cur = conn.cursor()


def created_table():
    cur.execute("CREATE TABLE tf_idf "
                "ID INT       KEY     NOT NULL"
                "TERM           TEXT    NOT NULL,"
                "DOCU           TEXT    NOT NULL,"
                "FREQUENCY      FLOAT,);")
    print("Table created successfully")


def insert_a(table='NEW_TABLE', culom='A', value=0):
    cur.execute(f"insert into {table} ({culom}) values ({value})")


def join_to():
    cur.execute("select * from words_pass as w"
                "join chaim_projct as c"
                " on w.word = c.word")


def select_all(TABLE='NEW_TABLE'):
    cur.execute(f"select * from {TABLE}")

created_table()
# insert_a(value=7)
conn.commit()

select_all(TABLE='tf_idf')
[print(row) for row in cur.fetchall()]

conn.close()


# select * from words_pass as w
# join chaim_projct as c
# on w.id = c.id
#
# insert into words_pass (word,pass) values ('shira',false)
#
# insert into words_pass (word,pass) values ('moshe',true)
























