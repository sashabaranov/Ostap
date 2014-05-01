from setuptools import setup

setup(
    name='Ostap',
    version='0.1.0',
    author='Sasha Baranov',
    author_email='a.baranov@cern.ch',
    packages=['ostap'],
    url='https://github.com/scr4t/Ostap',
    description='CERN LHCb physics analysis library',
    long_description=open('README').read(),
    install_requires=[
        "rootpy >= 0.7.1",
    ],
)