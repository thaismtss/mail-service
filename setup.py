import codecs
import os
import sys

from distutils.util import convert_path
from fnmatch import fnmatchcase
from setuptools import setup


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

PACKAGE = "mail_service"
NAME = "mail-service"
DESCRIPTION = "Sending email using various services."
AUTHOR = "Thais Martins"
AUTHOR_EMAIL = "thaismartins1999@gmail.com"
URL = "https://github.com/thaismtss/mail-service"
VERSION = '1.0.5'
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="GNU AFFERO GENERAL PUBLIC LICENSE",
    url=URL,
    packages=['mail_service'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Portuguese (Brazilian)",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3.8",
        "Topic :: Communications :: Email"
    ],

    zip_safe=False,
)

