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
__license = 'MIT Copyright 2019 Chapin Bryce'
__desc__ = '''Sample script to display and write logging 
    messages.'''
__docs__ = [
    'https://docs.python.org/3/library/logging.html',
    'https://docs.python.org/3/library/os.html'
]

# Set logger object, uses module's name
logger = logging.getLogger(name=__name__)

# Set default logger level to DEBUG. You can change this later
logger.setLevel(logging.DEBUG)

# Logging formatter. Best to keep consistent for most usecases
log_format = logging.Formatter(
    '%(asctime)s %(filename)s %(levelname)s %(module)s '
    '%(funcName)s %(lineno)d %(message)s')

# Setup STDERR logging
stderr_handle = logging.StreamHandler(stream=sys.stderr)
stderr_handle.setLevel(logging.INFO)
stderr_handle.setFormatter(log_format)

# Setup file loggings
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
    logger.info("Called from a function")

sample_function()