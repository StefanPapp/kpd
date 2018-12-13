"""
@copyright: 2018 Data Wizard
"""

import os
from setuptools import setup
from datawrangler import __version__


def _read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file:
        return file.read()


setup(
    name="datawrangler",
    version=__version__,
    author="Data Wizard",
    author_email="stefan.papp@data-wizard.net",
    description="loading files to kafka topic and doing some data wrangling",
    keywords="datawrangler",
    packages=["datawrangler"],
    long_description=_read('readme.md'),
    zip_safe=True,
    license="2017 Data Wizard. All rights reserved.",
    classifiers=[
        "Development Status :: Release",
        "Topic :: Documents",
    ],
    install_requires=["pykafka"]
)
