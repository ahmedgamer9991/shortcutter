import sqlite3 as sql

con = sql.connect(r"test.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS data(name TEXT, path TEXT)")
# cur.execute("ALTER TABLE data RENAME COLUMN command to path")
# cur.execute("DELETE FROM data WHERE rowid = ? ",("1",))
con.commit()