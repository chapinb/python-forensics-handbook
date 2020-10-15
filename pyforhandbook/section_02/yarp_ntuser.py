"""Using the `yarp` library to parse NTUSER.DAT Windows registry hives
using a class structure that is very portable and flexible. Parses the
MountPoints2 and TrustRecords keys for with string and binary values.

Example Usage:

    ``$ python yarp_ntuser.py {NTUSER HIVE}``

References:

* https://github.com/msuhanov/yarp
* https://docs.python.org/3/library/struct.html
* https://docs.python.org/3/library/datetime.html

Creating a Hive Specific Parser
===============================

Since we have a strong base class providing functionality to open hives, we can
build hive specific parsing classes that are tailored to handle artifacts
distinct to a single hive type. In this case we set up a class to handle
NTUSER.DAT files, though could get more specific on Windows versions, etc. In
this class we store a few useful details including fixed values used by other
methods and metadata about the class.

.. literalinclude:: ../pyforhandbook/section_02/yarp_ntuser.py
    :pyobject: NTUSER.__init__

Reading Hive String Values
==========================

With an open hive, we can begin to parse values from a known key location
within the hive. This method allows us to specify a key path and inspect each
of the subkeys. For each of the subkeys, we can then get the names and data
associated with each value in the key. Additionally we could - if needed -
continue to recurse on subkeys here. Instead we return this cursory information
for the caller to display as they wish. Since the values within MountPoints2
store string data, we don't need to perform further parsing of the record.

.. literalinclude:: ../pyforhandbook/section_02/yarp_ntuser.py
    :pyobject: NTUSER.parse_mountpoints2

Reading Hive Binary Values
==========================

Similarly to our prior example, we can get a key by path. In this case we don't
have a sense of what Office versions are available in the key and have elected
to iterate through each of those using the `parse_office_versions()` method.
Using each of the versions, we then access the respective `TrustRecords` key.
If found, we then parse the binary data (retrieved with the same `.data()`
method) using Struct to extract a timestamp and integer marking whether a
trusted macro was used. These parsed attributes are then returned to the caller
to be displayed.

.. literalinclude:: ../pyforhandbook/section_02/yarp_ntuser.py
    :pyobject: NTUSER.parse_trustrecords

Docstring References
====================
"""

from datetime import datetime, timedelta
import struct

import yarp
try:
    from pyforhandbook.section_02.yarp_base import RegistryBase
except ImportError:
    from yarp_base import RegistryBase

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
__date__ = 20190707
__license__ = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Registry parsing class that parses the NTUSER.DAT hive.'''
__docs__ = [
    'https://github.com/msuhanov/yarp',
    'https://docs.python.org/3/library/datetime.html',
    'https://docs.python.org/3/library/struct.html'
]


class NTUSER(RegistryBase):
    """Class to handle the parsing of the NTUSER.DAT hive."""
    def __init__(self, reg_path):
        super().__init__(reg_path)
        self.hive_type = 'NTUSER.DAT'
        self.macro_enabled_val = 2147483647

    def parse_mountpoints2(self):
        """Demonstration of parsing values from a key by path."""
        key_path = ('Software\\Microsoft\\Windows\\CurrentVersion'
                    '\\Explorer\\MountPoints2')
        for mp in self.hive.find_key(key_path).subkeys():
            mp_data = {}
            mp_data['name'] = mp.name().replace('#', '\\')
            mp_data['values'] = {x.name(): x.data() for x in mp.values()}
            mp_data['last_written'] = mp.last_written_timestamp()
            yield mp_data

    def parse_office_versions(self):
        """Get Office versions within an open Registry hive.

        Yields:
            (str): Office version number (ie. '15.0')
        """
        office_versions = self.hive.find_key('Software\\Microsoft\\Office')
        for subkey in office_versions.subkeys():
            key_name = subkey.name()
            is_ver_num = False
            try:
                _ = float(key_name)
                is_ver_num = True
            except ValueError:
                is_ver_num = False

            if is_ver_num:
                yield key_name

    def parse_trustrecords(self):
        """Demonstration of parsing binary values within a key."""
        trust_record_path = 'Software\\Microsoft\\Office\\{OFFICE_VERSION}' \
                    '\\Word\\Security\\Trusted Documents\\TrustRecords'
        for office_version in self.parse_office_versions():
            trust_rec_key = self.hive.find_key(
                trust_record_path.format(OFFICE_VERSION=office_version))
            if not trust_rec_key:
                continue

            for rec in trust_rec_key.values():
                date_val, macro_enabled = struct.unpack('q12xI', rec.data())
                ms = date_val/10.0
                dt_date = datetime(1601, 1, 1) + timedelta(microseconds=ms)
                yield {
                    'doc': rec.name(),
                    'dt': dt_date.isoformat(),
                    'macro': macro_enabled == self.macro_enabled_val
                }

def main(reg_file):
    reg = NTUSER(reg_file)
    # Call an example parsing method and display the values from NTUSER keys
    print("{:=^30}".format(' MountPoints2 '))
    for mount_point in reg.parse_mountpoints2():
        print(f"Found MountPoints2 path '{mount_point['name']}' with values:")
        value_str = '\tlast written time: {}\n'.format(
                mount_point["last_written"].isoformat())
        value_str += "\n".join(
            [f"\t{x}: {y}" for x, y in mount_point['values'].items()])
        print(value_str)

    print("{:=^30}".format(' TrustRecords '))
    for tr in reg.parse_trustrecords():
        print(f"Document: {tr['doc']}")
        print(f"\tCreated Date: {tr['dt']}")
        print(f"\tMacro Enabled: {tr['macro']}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='Registry Parsing',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}"
    )
    parser.add_argument('REG_FILE', help='Path to registry file',
                        type=argparse.FileType('rb'))
    args = parser.parse_args()
    main(args.REG_FILE)