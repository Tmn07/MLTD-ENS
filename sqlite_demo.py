# coding: UTF-8

import sqlite3
import time

conn = sqlite3.connect('ENS-db')
print ("数据库打开成功")

# CREATE TABLE mltd (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     email TEXT(32) NOT NULL,
#     nickname TEXT(16) NOT NULL,
#     create_timestamp INTEGER NOT NULL,
#     update_timestamp INTEGER ,
#     valid INTEGER DEFAULT 1 NOT NULL,
#     token TEXT(32) NOT NULL
# );

def count_all():
    c = conn.cursor()
    cursor = c.execute("SELECT COUNT(*) FROM mltd m ;")
    for row in cursor:
        return row[0]

def count_now():
    c = conn.cursor()
    cursor = c.execute("SELECT COUNT(*) FROM mltd m WHERE m.valid ==1;")
    for row in cursor:
        return row[0]

def insert(email, nickname, notice_time):
    c = conn.cursor()
    token = "xxx"
    timestamp = int(time.time())
    sql = f"INSERT INTO mltd (email, nickname, create_timestamp, token, notice_time) VALUES ('{email}', '{nickname}', {timestamp}, '{token}', {notice_time})"
    print(sql)
    c.execute(sql)
    try:
        conn.commit()
        print("数据插入成功")
        return True
    except Exception as e:
        print(e)
        return False, e

def clear():
    conn.close()
