import sqlite3
import json

conn = sqlite3.connect('assignmentdb.sqlite')
cur = conn.cursor()

cur.executescript('''
    drop table if exists User;
    drop table if exists Member;
    drop table if exists Course;
    CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

json_string = open('roster.json', 'r').read()
json_data = json.loads(json_string)

for item in json_data:
    user, course, role = item
    print(user, course, role)

    cur.execute('Insert or ignore into User(name) values(?)', (user,))
    cur.execute('Select id from User where name=?', (user,))
    user_id = cur.fetchone()[0]

    cur.execute('Insert or ignore into Course(title) values(?)', (course,))
    cur.execute('Select id from Course where title=?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('Insert or ignore into Member(user_id, course_id, role) values(?, ?, ?)', (user_id, course_id, role))
conn.commit()
conn.close()