"""This handbook has 7 sections covering common tasks for developing
Python scripts for use in DFIR. Each section contains short,
portable code blocks that can drop into a new script with minimal
tweaking. This way, you can quickly build out your custom script
without needing to re-invent the wheel each time.

This handbook is not intended to be read in order - if anything
this outline is the main launching point to find the correct page
containing the code block you wish to reference.

Please feel free to contribute your own sections with the snippets that have
worked well for you, even if a similar section already exists.

Section 1 - Essential Script Elements
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

Section 2 - Registry Hives with YARP
------------------------------------

* Using yarp to open a single hive
    - Opening a hive and recovering data available in transaction logs
* Parse registry hive keys and values
    - Building off our prior code to parse specific artifacts from an
      NTUSER.DAT hive, including string and binary values. Uses classes in a
      manner that is very flexible and permits extending functionality as
      needed with minimal effort.
* Searching for a pattern across hive keys and values.
    - Looking for a provided pattern across the entire hive.

Section 3 - Event Logs
----------------------

* Using python-evtx
    - Opening evtx files
* Parsing Logins (with types, levels, privs)
    - Parse out the commonly investigated 4624/4672 events
* Parsing Logouts (durations)
    - Parse 4624/4634 events to get information on user sessions
* Parsing Powershell decoding
    - Reassemble PowerShell strings in events and decode commands

Section 4 - Text logs
---------------------

* Handling IIS Logs
    - Parse common fields in IIS logs into a report
* Handling Syslog
    - Parse common syslog formats into a report
* Adding in GeoIP
    - Function to add GeoIP recognition

Section 5 - API calls & JSON data
---------------------------------

* VirusTotal
* HybridAnalysis
* Manipulating JSON

Section 6 - SQLite & macOS/mobile/browsers
------------------------------------------

* macOS Activity
    - KnowledgeC
* Andriod SMS
* Google Chome History DB

Section 7 - Opening forensic images
--------------------------------------

* LibEWF
    - Expose an E01 as a raw image
* PyTSK
    - Read data from a raw image (MBR)
    - Read data from a file (hashing)
    - Iterate through folders (file listing)
    - Perform targetted reads (file sigs)

"""
