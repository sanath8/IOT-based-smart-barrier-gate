import time
import sqlite3
import datetime

def Database_access(registration):
    #!/usr/bin/python

    conn = sqlite3.connect('test.db')
    print "Opened database successfully"


    starttime = str(time.time())

    sql = '''INSERT INTO PARKING (regNo, entryTime) VALUES(?, ?)'''

    conn.execute(sql,(registration,starttime))

    cur = conn.cursor()
    cur.execute("SELECT * FROM PARKING")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    conn.commit()

Database_access("wewe9439")

    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    #
    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
    #
    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
    #
    # conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
    #       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
    #
    # conn.commit()
    # print "Records created successfully";
    # conn.close()
