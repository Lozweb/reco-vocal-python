import sqlite3
from sqlite3 import Error
import os
import uuid

knowledge = "./database/knowledge.db"
current_path = os.path.dirname(__file__)


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
    fd = open(os.path.join(current_path, "tables.sql"))
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


def create_question(guess: str, res: str, ty: str, cmd: str):
    conn = sqlite3.connect(knowledge)
    c = conn.cursor()

    try:
        uid: str = str(uuid.uuid4())
        c.execute("INSERT INTO Response VALUES (?,?,?,?)", (uid, res, ty, cmd))
        c.execute("INSERT INTO Question VALUES (?,?)", (guess, uid))
        conn.commit()
    except Error as e:
        print("Create question error", e)
    finally:
        conn.close()


def search_question(guess: str):
    conn = sqlite3.connect(knowledge)
    c = conn.cursor()

    try:
        c.execute("SELECT responseUUID FROM Question WHERE guess=?", (guess,))
        rows = c.fetchall()
        return rows[0]

    except Error as e:
        print("Search Question error : ", e)

    finally:
        conn.close()


def search_response(uid: str):
    conn = sqlite3.connect(knowledge)
    c = conn.cursor()

    try:
        c.execute("SELECT * FROM Response WHERE UUID=?", (uid,))
        rows = c.fetchall()
        return rows[0]

    except Error as e:
        print("Search Response error", e)

    finally:
        conn.close()

