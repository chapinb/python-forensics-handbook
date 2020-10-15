"""File recursion example.

Demonstration of iterating through a directory to interact with
files.

Example Usage:

    ``$ python recursion_example.py``

References:

* https://docs.python.org/3/library/os.html

List a directory
================

This function shows an example of displaying all files and
folders within a single directory. From here you can further
interact with individual files and folders or iterate recursively
by calling the function on identified subdirectories.

.. literalinclude:: ../pyforhandbook/section_01/recursion_example.py
    :pyobject: list_directory

List a directory recursively
============================

This function shows an example of displaying all files and
folders within a all directories. You don't need to worry about
additional function calls as the ``os.walk()`` method handles
the recursion on subdirectories and your logic can focus on
handling the processing of files. This sample shows a method of
counting the number of files, subdirectories, and files ending in
".py" as an example.

.. literalinclude:: ../pyforhandbook/section_01/recursion_example.py
    :pyobject: iterate_files

"""
import os

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

__author__ = 'Chapin Bryce'
__date__ = 20190527
__license__ = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Sample script to iterate over a folder of files.'''
__docs__ = [
    'https://docs.python.org/3/library/os.html'
]

def list_directory(path):
    """List all file and folder entries in `path`."""
    print(f"Files and folders in '{os.path.abspath(path)}':")
    # Quick and easy method for listing items within a single
    # folder.
    for entry in os.listdir(path):
        # Print all entry names
        print(f"\t{entry}")

def iterate_files(path):
    # Though `os.walk()` exposes a list of directories in the
    # current `root`, it is rarely used since we are generally
    # interested in the files found within the subdirectories.
    # For this reason, it is common to see `dirs` named `_`.
    # DO NOT NAME `dirs` as `dir` since `dir` is a reserved word!
    for root, dirs, files in os.walk(os.path.abspath(path)):
        # Both `dirs` and `files` are lists containing all entries
        # at the current `root`.
        for fentry in files:
            # To effectively reference a file, you should include
            # the below line which creates a full path reference
            # to the specific file, regardless of how nested it is
            file_entry = os.path.join(root, fentry)
            # We can then hand `file_entry` off to other functions.
            yield file_entry


if __name__ == "__main__":
    abspath = os.path.abspath
    print(f"Listing {abspath('.')}")
    list_directory('.')
    print(f"\nRecurively counting files in {abspath('../../')}")
    num_py_files = 0
    for file_entry in iterate_files('../../'):
        if file_entry.endswith('.py'):
            num_py_files += 1
    print(f"\t{num_py_files} python files found "
          f"in {abspath('../../')}")