import os
import re
import argparse


class Search:
    def __init__(self, regex, is_recursive=False, only_directories=False):
        self.regex = re.compile(regex)
        self.is_recursive = is_recursive
        self.only_directories = only_directories
        self.files = set()
        self.final_files = set()

    def list_files(self):
        """List all the files."""
        # if the recursive option is set then search for the
        # files or directories in the same folder as well as
        # in the sub directories
        if self.is_recursive:
            # if the only_directories option is set to True
            # then search only for the directories else search for files
            if self.only_directories:
                for path, dirs, files in os.walk('.'):
                    for dir in dirs:
                        self.files.add(os.path.join(path, dir))
            else:
                for path, dirs, files in os.walk('.'):
                    for fil in files:
                        self.files.add(os.path.join(path, fil))

        else:
            files = os.listdir('.')
            if self.only_directories:
                for fil in files:
                    if os.path.isdir(fil):
                        self.files.add(fil)
            else:
                for fil in files:
                    if not os.path.isdir(fil):
                        self.files.add(fil)

        self.apply_regex()
        self.print_files()

    def apply_regex(self):
        """Apply the input regex on stored file names."""
        for fil in self.files:
            dir, basename = os.path.split(fil)
            if re.search(self.regex, basename):
                self.final_files.add(fil)

    def print_files(self):
        for fil in self.final_files:
            print (fil)


def main():
    parser = argparse.ArgumentParser(description='Utility for listing files.')
    parser.add_argument('regex', type=str,
                        help='Regex')
    parser.add_argument('-r', action='store_true',
                        help='Recursive search.')
    parser.add_argument('-d', action='store_true', help='List Only directories.')

    args = parser.parse_args()
    search = Search(args.regex, is_recursive=args.r, only_directories=args.d)
    search.list_files()


if __name__ == '__main__':
    main()

