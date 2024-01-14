Skip to content
Lordwill1
/
alx-higher_level_programming

Code
Issues
Pull requests
1
Actions
Projects
Security
Insights
Breadcrumbsalx-higher_level_programming/0x0F-python-object_relational_mapping
/0-select_states.py
Go to file
t
Latest commit
Lordwill1
Lordwill1
Updated 0x0F-python-object-_relayional_mapping
18c70a1
 · 
10 months ago
History
Executable File·16 lines (14 loc) · 424 Bytes
File metadata and controls

Code

Blame
Older
Newer
Lordwill1
10 months ago

Updated 0x0F-python-object-_relayional_mapping
#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

