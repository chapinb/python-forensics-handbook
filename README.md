# Python Forensics Handbook

A handy reference guide for building Python scripts to help out
Digital Forensic, Incident Response, and other Cyber Security
tools.

## Accessing the Handbook

There are several ways you can access the content in this handbook:

* Online at [https://chapinb.com/python-forensics-handboook](https://chapinb.com/python-forensics-handbook)
* Accessing the latest release available GitHub at 
    [https://github.com/chapinb/python-forensics-handbook/releases](https://github.com/chapinb/python-forensics-handbook/releases)
    and downloading the `pyforhandbook_html_docs_{version}.zip` file. You can 
    then extract the arvhive and open `index.html` in your web browser.
* Cloning the repository and checking out the gh-pages branch.
* Building it yourself! See instructions below.


## Building the handbook

To build this handbook, you will need Python 3.6 or later. To start, clone the master branch (or check out 
a tag for the release you want to build.) Then install all requirements by running `pip install -r requirements.txt`.

Once that finishes, navigate to the `doc_src/` directory and run `make html`. This will run on Windows, Linux, or macOS.
After the make command completes, you can view the built documentation within the `doc_src/_build/html` folder.

## Contributing

Have an idea for a section or a function that you would like to share? Please follow the above steps in 
"Building the handbook", add your changes, and open a pull request to get it integrated in to the repository!

More details on how to contribute coming soon. In the meantime, if you have any questions about the above, feel free
to open an issue on Github or reach out to me on Twitter @chapindb.
