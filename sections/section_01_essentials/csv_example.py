import csv
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
__license = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Sample script to write to CSV files.'''
__docs__ = [
    'https://docs.python.org/3/library/csv.html',
    'https://docs.python.org/3/library/os.html'
]


def write_csv_dicts(outfile, data, headers=None):
    """Writes a list of dictionaries to a CSV file.

    Arguments:
        outfile (str): Path to output file
        data (list): List of dictionaries to write to file
        headers (list): Header row to use. If empty, will use the
            first dictionary in the `data` list.
    """

    if not headers:
        # Use the first line of data
        headers = [str(x) for x in data[0].keys()]

    with open(outfile, 'w', newline="") as open_file:
        # Write only provided headers, ignore others
        csvfile = csv.DictWriter(open_file, headers,
                                 extrasaction='ignore')
        csvfile.writeheader()
        csvfile.writerows(data)


def write_csv_lists(outfile, data, headers=None):
    """Writes a list of lists to a CSV file.

    Arguments:
        outfile (str): Path to output file
        data (list): List of lists to write to file
        headers (list): Header row to use. If empty, will use the
            first list in the `data` list.
    """

    with open(outfile, 'w', newline="") as open_file:
        # Write only provided headers, ignore others
        csvfile = csv.writer(open_file)
        for count, entry in enumerate(data):
            if count == 0:
                # If headers are defined, write them, otherwise
                # continue as they will be written anyways
                if headers:
                    csvfile.writerow(headers)
            csvfile.writerow(entry)

sample_dict_data = [
    {'id': '0', 'city': 'Boston', 'state': 'MA',
     'country': 'USA'},
    {'id': '1', 'city': 'New York', 'state': 'NY',
     'country': 'USA'},
    {'id': '2', 'city': 'Washington', 'state': 'DC',
     'country': 'USA'},
]

write_csv_dicts('dict_test.csv', sample_dict_data)

headers = ['id', 'city', 'state', 'country']
sample_list_data = [
    ['0', 'Boston', 'MA', 'USA'],
    ['1', 'New York', 'NY', 'USA'],
    ['2', 'Washington', 'DC', 'USA']
]

write_csv_lists('list_test.csv', sample_list_data,
                headers=headers)
