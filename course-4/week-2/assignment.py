import sqlite3

conn = sqlite3.connect('./databases/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

with open('mbox.txt', 'r') as f:
    for line in f:
        if line.startswith('From: '):
            line = line.split()[1].split('@')[1]
            cur.execute('SELECT count FROM Counts where org=?', (line,))
            row = cur.fetchone()
            if row is None:
                cur.execute('INSERT INTO Counts (org,count) VALUES (?, 1)', (line,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org=?', (line,))
conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
