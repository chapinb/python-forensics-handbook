"""
.. note::
    IN DEVELOPMENT - More sections will release over the coming weeks/months/as
    time permits. Feel free to contribute as you have an idea or time to assist,
    otherwise stay tuned!

This handbook consists of 7 sections covering common tasks for developing
Python scripts for use in DFIR. Each section contains short,
portable code blocks that can drop into a new script with minimal
tweaking. This way, you can quickly build out your custom script
without needing to re-invent the wheel each time.

This handbook is not intended to be read in order - if anything
this outline is the main launching point to find the correct page
containing the code block you wish to reference.

Please feel free to contribute your own sections with the snippets that have
worked well for you, even if a similar section already exists. This handbook
is hosted on GitHub at https://github.com/chapinb/python-forensics-handbook and
available to read online at https://chapinb.com/python-forensics-handbook.
Please consider submitting a pull request with your additions!

Chapter 1 - Essential Script Elements
-------------------------------------

This chapter covers code blocks that are useful across scripts
and are not DFIR specific, but solid practices to integrate into
projects to allow for uniformity.

* Argparse
    - Command line parameter handling
* Logging
    - Writing status and error messages to the console and
      log file
* Open Files
    - Read text files with varying UTF encodings.
* CSV Generation
    - For better or worse, CSV reports are very common in DFIR
      and this code block covers several methods for
      generating a CSV
* Recursive File Exploration
    - Quick example of code to explore directories and access
      nested files.
* Parallel Processing
    - Simple implementation of multithreading and multiprocessing

Chapter 2 - Registry Hives
------------------------------------

In this chapter, we demonstrate how to open a registry hive, navigate through
its keys, and interact with values to expose information for analysis.

* Using yarp to open a single hive
    - Opening a hive and recovering data available in transaction logs
* Parse registry hive keys and values
    - Building off our prior code to parse specific artifacts from an
      NTUSER.DAT hive, including string and binary values. Uses classes in a
      manner that is very flexible and permits extending functionality as
      needed with minimal effort.
* Searching for a pattern across hive keys and values.
    - Looking for a provided pattern across the entire hive.

Chapter 3 - Event Logs
----------------------

The functions showcased in this chapter highlight methods to access events
within Windows event log files, iterating over the events, and extracting
useful records for further examination.

* Using python-evtx
    - Opening evtx files
    - Iterating over events
* Parsing Logins
    - Parse out the commonly investigated 4624/4672 events

Chapter 4 - Text logs
---------------------

* Handling IIS Logs
    - Parse common fields in IIS logs into a report
* Handling Syslog
    - Parse common syslog formats into a report
* Adding in GeoIP
    - Function to add GeoIP recognition

Chapter 5 - API calls & JSON data
---------------------------------

* VirusTotal
* HybridAnalysis
* Manipulating JSON

Chapter 6 - Databases
------------------------------------------

Databases are found within many applications and operating systems. This chapter
covers methods to extract information from these common databases, along with
functions that are purpose built to parse information from frequently seen
database tables.

* macOS Activity
    - KnowledgeC
* Android SMS
* Google Chrome History DB

Chapter 7 - Opening forensic images
--------------------------------------

Media acquisition and preservation formats are very common within DFIR and
the ability to extract specific contents from these files leads to faster
analysis and simplified usage of the tool you are building. With these functions
you can read files from a forensic image and pass them straight to your other
utilities for further parsing.

* LibEWF
    - Expose an E01 as a raw image
* PyTSK
    - Read data from a raw image (MBR)
    - Read data from a file (hashing)
    - Iterate through folders (file listing)
    - Perform targeted reads (file signatures)

"""
