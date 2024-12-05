import sqlite3

conn = sqlite3.connect('iTunes_assignment.sqlite')
curs = conn.cursor()

curs.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fhandle = open('tracks.csv')

for line in fhandle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7:
        continue

    title = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    print(title,artist,album,count,rating,length,genre)

    curs.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    curs.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = curs.fetchone()[0]

    curs.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    curs.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = curs.fetchone()[0]

    curs.execute('''INSERT OR IGNORE INTO Album (title,artist_id) 
                VALUES (?,?)''',(album,artist_id))
    curs.execute('SELECT id FROM Album WHERE title= ?',(album,))
    album_id = curs.fetchone()[0]

    curs.execute('''INSERT OR IGNORE INTO Track 
                (title,album_id,genre_id,len,rating,count) VALUES (?,?,?,?,?,?)''',
                (title,album_id,genre_id,length,rating,count))
    
    conn.commit()


