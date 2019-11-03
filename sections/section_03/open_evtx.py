"""Example for opening EVTX files.

Demonstrates how to open an EVTX file and get basic details about the event log.
This section makes use of python-evtx, a python library for reading event log
files. To install, run ``pip install python-evtx``.

Other libraries for parsing these event logs exist and we welcome others to
add snippets that showcase how to make use of them in reading EVTX files.

Example Usage:

    ``$ python open_evtx.py System.evtx``

References:

* https://github.com/williballenthin/python-evtx


Open Windows Event Logs (EVTX)
==============================

This function shows an example of opening an EVTX file and parsing out several
common parameters about the file.

.. literalinclude:: ../sections/section_03/open_evtx.py
    :pyobject: open_evtx

Docstring References
====================
"""

from collections import OrderedDict
import os
import Evtx.Evtx as evtx


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
__date__ = 20191103
__license__ = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Sample script to read EVTX files.'''
__docs__ = [
    'https://github.com/williballenthin/python-evtx'
]


def open_evtx(input_file):
    """Opens a Windows Event Log and displays common log parameters.

    Arguments:
        input_file (str): Path to evtx file to open
    """

    with evtx.Evtx(input_file) as open_log:
        header = open_log.get_file_header()
        properties = OrderedDict([
            ('major_version', 'File version (major)'),
            ('minor_version', 'File version (minor)'),
            ('is_dirty', 'File is ditry'),
            ('is_full', 'File is full'),
            ('next_record_number', 'Next record number')
        ])

        for key, value in properties.items():
            print(f"{value}: {getattr(header, key)()}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description=__desc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}"
    )
    parser.add_argument('EVTX_FILE', help="EVTX file to read")
    args = parser.parse_args()

    open_evtx(args.EVTX_FILE)
