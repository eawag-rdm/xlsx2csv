import os
from setuptools import setup

with open('xlsx2csv.py', 'r') as f:
    for line in f:
        if line.find('__version__'):
            exec(line)
            version = __version__
            break
    else:
        version = '0.0.0'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.0",
    "Programming Language :: Python :: 3.1",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Office/Business",
    "Topic :: Utilities"
]

setup(
    name='xls2csv',
    version=version,
    description="xlsx to csv converter",
    author="Dilshod Temirkhdojaev",
    author_email="tdilshod@gmail.com",
    classifiers=classifiers,
    packages=['xlsx2csv'],
    url="http://github.com/dilshod/xlsx2csv",
    entry_points = {
        'console_scripts': ['xlsx2csv=xlsx2cs.xlsx2csv.main']
    },
    zip_safe=false,
    license='GPL-2+'
)
