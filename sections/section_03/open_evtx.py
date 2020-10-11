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
header metadata parameters about the file.

.. literalinclude:: ../sections/section_03/open_evtx.py
    :pyobject: open_evtx

Iterate over record XML data (EVTX)
===================================

In this function, we iterate over the records within an EVTX file and expose
the raw XML. This leverages a yield generator for
low impact on resources.

Additionally, if you would like to parse the XML, or interact with the child
elements, you can enable it by assigning the `parse_xml` parameter as True,
which will then call the ``.lxml()`` method on the individual event record.
This requires the installation of the lxml Library, as it returns a lxml.etree
object that you can interact with.

.. literalinclude:: ../sections/section_03/open_evtx.py
    :pyobject: get_events

Filtering records within events logs
====================================

Now that we have :func:`get_events()`, we can begin to perform operations on
the newly accessible data. In this function, we extract information from the
LXML object, and use that to filter results based on Event ID and other fields
within the results. You can easily extend this to support other fields,
filters, and return values. Some examples include:

- extracting all login and logoff events, with their session identifiers,
  then calculating the session durations
- Identify PowerShell events and expose arguments for further processing
  (ie. Base64 decoding, shellcode analysis)

.. literalinclude:: ../sections/section_03/open_evtx.py
    :pyobject: filter_events_json

Docstring References
====================
"""
import json
from collections import OrderedDict
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

    Examples:
        >>> open_evtx("System.evtx")
        File version (major): 3
        File version (minor): 1
        File is ditry: True
        File is full: False
        Next record number: 10549

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


def get_events(input_file, parse_xml=False):
    """Opens a Windows Event Log and returns XML information from
    the event record.

    Arguments:
        input_file (str): Path to evtx file to open
        parse_xml (bool): If True, return an lxml object, otherwise a string

    Yields:
        (generator): XML information in object or string format

    Examples:
        >>> for event_xml in enumerate(get_events("System.evtx")):
        >>>     print(event_xml)

    """
    with evtx.Evtx(input_file) as event_log:
        for record in event_log.records():
            if parse_xml:
                yield record.lxml()
            else:
                yield record.xml()


def filter_events_json(event_data, event_ids, fields=None):
    """Provide events where the event id is found within the provided list
    of event ids. If found, it will return a JSON formatted object per event.

    If a list of fields are provided, it will filter the resulting JSON event
    object to contain only those fields.

    Arguments:
        event_data (genertor): Iterable containing event data as XML. Preferably
            the result of the :func:`get_events()` method.
        event_ids (list): A list of event identifiers. Each element should be a
            string value, even though the identifier is an integer.
        fields (list): Collection of fields from the XML data to include in the
            JSON output. Only supports top-level fields.

    Yields:
        (dict): A dictionary containing the filtered record information

    Example:

        >>> filtered_logins = filter_events_json(
        >>>     get_events("System.evtx", parse_xml=True),
        >>>     event_ids=['4624', '4625'],
        >>>     fields=["SubjectUserName", "SubjectUserSid",
        >>>             "SubjectDomainName", "TargetUserName", "TargetUserSid",
        >>>             "TargetDomainName", "WorkstationName", "IpAddress",
        >>>             "IpPort", "ProcessName"]
        >>> )
        >>> for filtered_login in filtered_logins:
        >>>     print(json.dumps(filtered_login, indent=2))

    """
    for evt in event_data:
        system_tag = evt.find("System", evt.nsmap)
        event_id = system_tag.find("EventID", evt.nsmap)
        if event_id.text in event_ids:
            event_data = evt.find("EventData", evt.nsmap)
            json_data = {}
            for data in event_data.getchildren():
                if not fields or data.attrib['Name'] in fields:
                    # If we don't have a specified field filter list, print all
                    # Otherwise filter for only those fields within the list
                    json_data[data.attrib['Name']] = data.text

            yield json_data


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description=__desc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=f"Built by {__author__}, v.{__date__}"
    )
    parser.add_argument('EVTX_FILE', help="EVTX file to read")
    args = parser.parse_args()

    print("EVTX File Header Information")
    open_evtx(args.EVTX_FILE)
    print("EVTX File records")
    for count, event in enumerate(get_events(args.EVTX_FILE)):
        if count >= 3:
            break
        print(event)

    print("Filter for Login events")
    logins = filter_events_json(
        get_events(args.EVTX_FILE, parse_xml=True),
        event_ids=['4624'],
        fields=["SubjectUserName", "SubjectUserSid", "SubjectDomainName",
              "TargetUserName", "TargetUserSid", "TargetDomainName",
              "WorkstationName", "IpAddress", "IpPort", "ProcessName"]
    )
    for login in logins:
        print(json.dumps(login, indent=2))
