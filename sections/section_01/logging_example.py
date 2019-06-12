"""Example for writing logging information to the console and a
log file.

Example Usage:

    ``$ python logging_example.py``

References:

* https://docs.python.org/3/library/logging.html
* https://docs.python.org/3/library/os.html

Logging configuration
=====================

This function shows an example of creating a logging instance that
writes messages to both STDERR and a file, allowing your script
to write content to STDOUT uninterrupted. Additionally, you can
set different logging levels for the two handlers - generally you
keep debugging information in the log file while writing more
critical messages to the console in STDERR.

.. literalinclude:: ../sections/section_01/logging_example.py
    :pyobject: setup_logging

Docstring References
====================
"""
import logging
import sys

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
__license__ = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Sample script to display and write logging
    messages.'''
__docs__ = [
    'https://docs.python.org/3/library/logging.html',
    'https://docs.python.org/3/library/os.html'
]

logger = None

def setup_logging():
    """Function to setup logging configuration and test it."""
    # Allow us to modify the `logger` variable within a function
    global logger

    # Set logger object, uses module's name
    logger = logging.getLogger(name=__name__)

    # Set default logger level to DEBUG. You can change this later
    logger.setLevel(logging.DEBUG)

    # Logging formatter. Best to keep consistent for most usecases
    log_format = logging.Formatter(
        '%(asctime)s %(filename)s %(levelname)s %(module)s '
        '%(funcName)s %(lineno)d %(message)s')

    # Setup STDERR logging, allowing you uninterrupted
    # STDOUT redirection
    stderr_handle = logging.StreamHandler(stream=sys.stderr)
    stderr_handle.setLevel(logging.INFO)
    stderr_handle.setFormatter(log_format)

    # Setup file logging
    file_handle = logging.FileHandler('sample.log', 'a')
    file_handle.setLevel(logging.DEBUG)
    file_handle.setFormatter(log_format)

    # Add handles
    logger.addHandler(stderr_handle)
    logger.addHandler(file_handle)

    # Sample log messages
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is a error message")
    logger.critical("This is a critical message")

    def sample_function():
        """Sample function to demonstrate logging formatting."""
        logger.info("Called from a function")

    sample_function()

if __name__ == "__main__":
    setup_logging()
