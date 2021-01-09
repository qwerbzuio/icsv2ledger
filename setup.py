import sys
from setuptools import setup

# extra check to avoid accidentally running this script lower python versions
assert sys.version_info >= (3, 2)

setup(
    name='icsv2ledger',
    version='0.1.0',
    description="This is a command-line utility to convert CSV files of transactions, such as you might download from an online banking service, into the format used by John Wiegley's excellent Ledger system.",
    author='Quentin Stafford-Fraser',
    author_email='quentin@pobox.com',
    url="http://github.com/quentinsf/icsv2ledger",
    python_requires='>=3.2',
    entry_points={
        'console_scripts': [
            'icsv2ledger = icsv2ledger:main'
        ]
    },
)
