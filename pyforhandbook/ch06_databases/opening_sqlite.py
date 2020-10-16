"""Example for opening and exploring Sqlite databases.

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

.. literalinclude:: ../pyforhandbook/ch06_databases/opening_sqlite.py
    :pyobject: open_sqlite

Listing Tables configuration
============================

This function shows an example of listing available tables in an opened Sqlite
database.

.. literalinclude:: ../pyforhandbook/ch06_databases/opening_sqlite.py
    :pyobject: list_tables
"""
import argparse
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

__author__ = "Brittney Argirakis"
__date__ = 20191126
__license__ = "MIT Copyright 2019 Brittney Argirakis"
__desc__ = """Sample script to open a SqLite DB."""
__docs__ = [
    "https://docs.python.org/3/library/argparse.html",
    "https://docs.python.org/3/library/os.html",
    "https://docs.python.org/3/library/sqlite3.html",
]


def open_sqlite(input_db):
    """Open a SQLite database

    Args:
        input_db: Path to a SQLite database to open

    Returns:
        A connection to a SQLite database
    """
    print("Provided Database: {}".format(input_db))
    return sqlite3.connect(input_db)


def list_tables(conn):
    """List all tables in a SQLite database

    Args:
        conn: An open connection from a SQLite database

    Returns:
        list: List of table names found in the database
    """
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master")
    return [i[0] for i in cur.fetchall()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__desc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}",
    )
    parser.add_argument("db", help="path to the database to read")
    args = parser.parse_args()
    connection = open_sqlite(args.db)
    listed_tables = list_tables(connection)

    print(listed_tables)
