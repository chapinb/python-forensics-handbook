"""This handbook has 7 sections covering common tasks for developing
Python scripts for use in DFIR. Each section contains short,
portable code blocks that can drop into a new script with minimal
tweaking. This way, you can quickly build out your custom script
without needing to re-invent the wheel each time.

This handbook is not intended to be read in order - if anything
this outline is the main launching point to find the correct page
containing the code block you wish to reference.

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
    - Opening a hive and confirming it's the one you want to view
* Read key information/metadata
    - USB Devices
* Read value information/metadata
    - USB Devices
* YARP hive file + transaction logs/other registry fragments

Section 3 - Event Logs
----------------------

* Using python-evtx
    - Opening evtx files
* Counts/Metadata about EVTX container
* Parsing Logins (with types, levels, privs)
* Parsing Logouts (durations)
* Parsing Powershell decoding

Section 4 - Text logs
---------------------

* Handling IIS Logs
* Handling Syslog
* Adding in GeoIP

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
