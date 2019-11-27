"""Example for opening and exploring Sqlite database.

Example Usage:

    ``$ python opening_sqlite.py history_db``

References:

* https://docs.python.org/3/library/argparse.html
* https://docs.python.org/3/library/os.html
* https://docs.python.org/3/library/sqlite3.html

Opening Sqlite configuration
============================

This function shows an example of opening a Sqlite database with Python. 
Additional information regarding Sqlite modules can be
seen at https://docs.python.org/3/library/sqlite3.html.

.. literalinclude:: ../sections/section_06/opening_sqlite.py
    :pyobject: open_sqlite

Listing Tables configuration
============================

This function shows an example of listing available tables in an opened Sqlite database.

.. literalinclude:: ../sections/section_06/opening_sqlite.py
    :pyobject: list_tables
"""
import argparse
import os
import sqlite3

"""
Copyright 2019 Brittney Argirakis

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

__author__ = 'Brittney Argirakis'
__date__ = 20191126
__license__ = 'MIT Copyright 2019 Brittney Argirakis'
__desc__ = '''Sample script to open a SqLite DB.'''
__docs__ = [
    'https://docs.python.org/3/library/argparse.html',
    'https://docs.python.org/3/library/os.html',
    'https://docs.python.org/3/library/sqlite3.html'
]

def open_sqlite(inputdb):
    print("Provided Database: {}".format(inputdb))
    return sqlite3.connect(inputdb)

def list_tables(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master")
    table_list = []
    for i in cur.fetchall():
        table_list.append(i[0])
    
    return table_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__desc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}"
    )
    parser.add_argument("db", help="path to the database to read")
    args = parser.parse_args()
    conn = open_sqlite(args.db)
    listed_tables = list_tables(conn)

    print(listed_tables)
