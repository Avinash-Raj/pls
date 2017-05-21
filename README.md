pls
==============

Python script to list files or folders according to the input regex. `pls` command without any optional argument should list only the files. To list folders or to do a recursive serach, you have to enable `-d`, `-r` options. 

To install this package, you have to run

```sh
sudo python setup.py install
```

Now you're free to use `pls` command from anywhere.

```sh
$ python pls.py -h
usage: pls.py [-h] [-r] [-d] regex

Utility for listing files.

positional arguments:
  regex       Regex

optional arguments:
  -h, --help  show this help message and exit
  -r          Recursive search.
  -d          List Only directories.

$ pls -rd ''
./.f
./documents
./versions

$ pls -r '\.py$'
./decorator_info.py
./versions/940992504396_.py
./repo.py

$ pls -d '^v.*s.*s$'
versions

$ pls '(?<!~)$'
 xml docs                      sample.xml 
 .m.swp                        .e.swp 
 .6.14.png                     s2s-django 
 decorator_info.py             .ri.swp 
 Doc 07-May-2017, 23_22.pdf    .fi.swp 
 repo.py                       .r.swp 

```
