import sqlite3

con = sqlite3.connect('assignment_ex15.sqlite')
curs = con.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')

curs.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
fhandle = open(fname)
for line in fhandle:
    if not line.startswith('From: '):
        continue
    tmp = line.split()
    addr = tmp[1]
    addrpos = addr.find('@')
    org = addr[addrpos+1:]
    curs.execute('SELECT count FROM Counts WHERE org = ? ',(org,))
    row = curs.fetchone()
    if row is None:
        curs.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
    else:
        curs.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
    con.commit()    

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in curs.execute(sqlstr):
    print(str(row[0]), row[1])

curs.close()