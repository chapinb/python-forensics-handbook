"""Example for reading data from encoded text files.

Demonstrates how to handle setting the proper encoding for
UTF-8, UTF-16-LE, and UTF-16-BE with the ability to easily
expand to support checking other file magic values/signatures.

Example Usage:

    ``$ python open_files.py``

References:

* https://docs.python.org/3/library/io.html


Open files with proper encoding
===============================

This first function shows an example of opening a file after checking for a
byte-order mark (BOM). While this method could be expanded to check for a file's
magic value/file signature, this low-tech method will help with parsing a
collection of files that may be UTF-8, UTF-16-LE, and UTF-16-BE, three very
common text file encodings. Feel free to build and share on this.

.. literalinclude:: ../pyforhandbook/ch01_essentials/open_files.py
    :pyobject: open_file

Docstring References
====================
"""

from io import open

"""
Copyright 2019 Chapin Bryce

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

__author__ = "Chapin Bryce"
__date__ = 20191103
__license__ = "MIT Copyright 2019 Chapin Bryce"
__desc__ = """Sample script to read encoded text files."""
__docs__ = [
    "https://docs.python.org/3/library/csv.html",
    "https://docs.python.org/3/library/os.html",
]


def open_file(input_file):
    """Opens an encoded text file and prints the contents

    Arguments:
        input_file (str): Path to file to open
    """

    test_encoding = open(input_file, "rb")
    bom = test_encoding.read(2)
    file_encoding = "utf-8"
    if bom == b"FEFF":
        file_encoding = "utf-16-le"
    elif bom == b"FFFE":
        file_encoding = "utf-16-be"

    with open(input_file, "r", encoding=file_encoding) as open_input_file:
        for raw_line in open_input_file:
            line = raw_line.strip()
            print(line)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=__desc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}",
    )
    parser.add_argument("INPUT_FILE", help="Text file to read")
    args = parser.parse_args()

    open_file(args.INPUT_FILE)
