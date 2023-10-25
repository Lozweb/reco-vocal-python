import sqlite3
from sqlite3 import Error
import os
import uuid

knowledge = "./database/knowledge.db"
dir = os.path.dirname(__file__)

def create():
    conn = None

    try:
        conn = sqlite3.connect(knowledge)
        print("database initialized")

    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()


def install():
    create()
    fd = open(os.path.join(dir, "tables.sql"))
    sqlfile = fd.read()
    fd.close()
    sqlcommands = sqlfile.split(';')
    conn = sqlite3.connect(knowledge)
    c = conn.cursor()

    for command in sqlcommands:
        try:
            c.execute(command)
        except Error as e:
            print("Command skip", e)

    print("database install ok!")
    conn.close()


def create_question(guess: str, res: str, type: str, cmd: str):
    conn = sqlite3.connect(knowledge)
    c = conn.cursor()

    try:
        id: str = str(uuid.uuid4())
        c.execute("INSERT INTO Response VALUES (?,?,?,?)", (id, res, type, cmd))
        c.execute("INSERT INTO Question VALUES (?,?)", (guess, id))
        conn.commit()
    except Error as e:
        print("Create question error", e)
    finally:
        conn.close()
