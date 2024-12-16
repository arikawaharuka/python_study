import sqlite3
import json

conn = sqlite3.connect('Member.sqlite')
curs = conn.cursor()

curs.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter file name: ')
fhandle = open(fname)
str_data = fhandle.read()
json_data = json.loads(str_data)

for data in json_data:
    name = data[0]
    title = data[1]
    role = data[2]

    print((name,title))

    curs.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
    curs.execute('SELECT id FROM User WHERE name=?',(name,))
    user_id = curs.fetchone()[0]

    curs.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title,))
    curs.execute('SELECT id FROM Course WHERE title=?',(title,))
    course_id = curs.fetchone()[0]

    curs.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role) 
                VALUES (?,?,?)''',(user_id,course_id,role))
    
    conn.commit()    

