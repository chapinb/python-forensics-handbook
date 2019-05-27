# Outline

Outline of chapters and sections of the book. For quick reference
on where to find the snippet you are looking for. Each snippet
should drop into another script without significant tweaking

## Section 1 - Essential Script Snippets

### Argparse

Sample argparse usage and help information

### Logging

Setting up a basic logger with stdout and log file support.

### 

### CSV writing

For Python 2 and 3, also unicode csv. Drop into any

### Parallel Processing

Simple implementation of multithreading and multiprocessing

- Show off calling volatility?

## Section 2 - Registry Hives with YARP

### Using yarp to open a single hive

Opening a hive and confirming it's the one you want to view

### Read key information/metadata

- USB Devices

### Read value information/metadata

- USB Devices

### YARP hive file + transaction logs/other registry fragments

- Show how we can get more data with this method

## Section 3 - Event Logs

### Using python-evtx

#### Opening evtx files

- Counts/Metadata about EVTX container

#### Parsing Logins (with types, levels, privs)

#### Parsing Logouts (durations)

#### Parsing Powershell decoding

## Section 4 - Text logs

### Handling IIS Logs

### Handling Syslog

### Adding in GeoIP

## Section 5 - API calls & JSON data

### VirusTotal

### HybridAnalysis

### Manipulating JSON

- Lists of dictionaries

## Section 6 - SQLite & macOS/mobile/browsers

### macOS Activity

- KnowledgeC

### Andriod SMS

### Google Chome History DB

## Section 7 - Opening forensic images

### LibEWF

- Expose an E01 as a raw image

### PyTSK

#### Read data from a raw image

- Read MBR/GPT

#### Read data from a file

- Hashing a file

#### Iterate through folders

- Generate a metadata rich file listing

#### Perform targetted reads

- Signature look ups
