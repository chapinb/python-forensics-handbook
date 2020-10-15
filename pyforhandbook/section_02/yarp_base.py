"""Using the `yarp` library to open Windows registry hives using a class
structure that is very portable and flexible.

Example Usage:

    ``$ python yarp_base.py {NTUSER HIVE}``

References:

* https://github.com/msuhanov/yarp
* https://docs.python.org/3/library/struct.html
* https://docs.python.org/3/library/datetime.html


Opening a Registry Hive
=======================

This class demonstrates how to open a registry hive file with the `yarp` tool.
This library not only allows us to open a single offline hive, but also
leverage any available transaction logs to include additional information
otherwise available on the Window's system. This class handles both the opening
of the primary hive and attempted recovery of the transaction logs.

.. literalinclude:: ../pyforhandbook/section_02/yarp_base.py
    :pyobject: RegistryBase

Docstring References
====================
"""
from datetime import datetime, timedelta
import struct
# Installed via:
#   pip install https://github.com/msuhanov/yarp/archive/1.0.28.tar.gz
from yarp import Registry, RegistryHelpers


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
__desc__ = '''Registry parsing class that opens an offline hive.'''
__docs__ = [
    'https://github.com/msuhanov/yarp',
    'https://docs.python.org/3/library/datetime.html',
    'https://docs.python.org/3/library/struct.html'
]


class RegistryBase():
    """Base class containing common registry parsing code. Will open a hive
    and attempt recovery using available transaction logs"""
    def __init__(self, reg_file):
        """Base __init__ method, responsible for opening a hive."""
        self.reg_file = reg_file
        self.tx_log_files = []
        self.hive = None
        self._open_hive()

    def _open_hive(self):
        """Open a registry hive with yarp. Must be an open file object with read
        permissions. Will attempt to recover the hive with transaction logs if
        present.
        """
        self.hive = Registry.RegistryHive(self.reg_file)
        self._recover_hive()

    def _recover_hive(self):
        """Search for transaction logs and attempt recovery of the hive."""
        hive_path = self.hive.registry_file.file_object.name
        tx_logs = RegistryHelpers.DiscoverLogFiles(hive_path)
        self.tx_log_files = []
        for tx_path in ['log_path', 'log1_path', 'log2_path']:
            log_obj = None
            if getattr(tx_logs, tx_path, None):
                log_obj = open(getattr(tx_logs, tx_path), 'rb')
            self.tx_log_files.append(log_obj)
        self.hive.recover_auto(*self.tx_log_files)

    def close(self):
        """Properly close a hive."""
        self.hive = None
        self.reg_file.close()
        for log in self.tx_log_files:
            if log:
                log.close()


def main(reg_file):
    reg = RegistryBase(reg_file)
    print("Hive: " + reg.hive.registry_file.file_object.name)
    print("Last written time: " + reg.hive.last_written_timestamp().isoformat())
    print("Root key: " + reg.hive.root_key().name())


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
