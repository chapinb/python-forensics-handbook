import argparse
import os
from pathlib import PurePath

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
__license = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Sample script to accept command line arguments.'''
__docs__ = [
    'https://docs.python.org/3/library/argparse.html',
    'https://docs.python.org/3/library/os.html',
    'https://docs.python.org/3/library/pathlib.html'
]

# Only run if called directly (not imported)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Sample Argparse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}"
    )
    parser.add_argument('INPUT_FILE', help="Input file to parse")
    parser.add_argument('OUTPUT_FOLDER', 
        help="Folder to store output")
    parser.add_argument('-l', '--log', help="Path to log file",
        default=os.path.abspath(os.path.join(
            PurePath(__file__).parent, 
            PurePath(__file__).name.rsplit('.', 1)[0] + '.log'))
    )
    parser.add_argument('-v', '--verbose', action='store_true',
        help='Include debug log messages')

    args = parser.parse_args()

    # Show arguments
    print(f'Input file: {args.INPUT_FILE}')
    print(f'Output folder: {args.OUTPUT_FOLDER}')
    print(f'Log file: {args.log}')
    print(f'Be verbose?: {args.verbose}')