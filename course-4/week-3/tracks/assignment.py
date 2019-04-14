import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect("assignment.sqlite")
cur = conn.cursor()

cur.executescript('''
    Drop table if exists Album;
    Drop table if exists Artist;
    Drop table if exists Genre;
    Drop table if exists Track;

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
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
    );

''')

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

filename = 'Library.xml'
tree = ET.parse(filename)
items = tree.findall('dict/dict/dict')
print(f'Total Items: {len(items)}')

for item in items:
    if lookup(item, 'Track ID') is None:
        continue
    name = lookup(item, 'Name')
    artist = lookup(item, 'Artist')
    album = lookup(item, 'Album')
    genre = lookup(item, 'Genre') 
    count = lookup(item, 'Play Count')
    rating = lookup(item, 'Rating')
    length = lookup(item, 'Total Time') 

    if name is None or artist is None or album is None or genre is None:
        continue
    print(name, artist, album, genre)

    cur.execute('Insert or ignore into Artist(name) values(?)', (artist,))
    cur.execute('select id from Artist where name=?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('Insert or ignore into Album(title, artist_id) values(?, ?)', (album, artist_id))
    cur.execute('select id from Album where title=?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('Insert or ignore into Genre(name) values(?)', (genre, ))
    cur.execute('select id from Genre where name=?', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
    (title, album_id, genre_id, len, rating, count) 
    VALUES ( ?, ?, ?, ?, ?, ? )''', 
    (name, album_id, genre_id, length, rating, count))


conn.commit()
conn.close()
