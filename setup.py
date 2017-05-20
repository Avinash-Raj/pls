from setuptools import setup, find_packages
from pls import __version__

setup(
 name='pls',
 version=__version__,
 description='List files or folders exists in the current directory.',
 url='https://github.com/Avinash-Raj/pls',
 author='Avinash Raj',
 author_email='avistylein3105@gmail.com',
 packages=find_packages(),
 license= 'MIT',
 entry_points={
        'console_scripts': ['pls = pls.main:main']
 },
 zip_safe=False
)
