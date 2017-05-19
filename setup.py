from setuptools import setup
 
setup(
 name='pls',    # This is the name of your PyPI-package.
 version='0.1',                          # Update the version number for new releases
 description='List files or folders exists in the current directory.',
 url='https://github.com/Avinash-Raj/pls',
 author='Avinash Raj',
 entry_points={
        'console_scripts': ['pls = pls.main:main']
 }                 # The name of your scipt, and also the command you'll be using for calling it
)
