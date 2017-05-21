import os
import re
import argparse


class Search:
    def __init__(self, regex, is_recursive=False, only_directories=False):
        self.regex = re.compile(r'(?m)' + regex)
        self.is_recursive = is_recursive
        self.only_directories = only_directories
        self.files = set()
        self.final_files = set()
        self.cwd = os.getcwd()
        self.colorize = True if os.name == 'posix' else False

    def list_files(self):
        """List all the files."""
        # if the recursive option is set then search for the
        # files or directories in the same folder as well as
        # in the sub directories
        if self.is_recursive:
            # if the only_directories option is set to True
            # then search only for the directories else search for files
            if self.only_directories:
                for path, dirs, files in os.walk(self.cwd):
                    for directory in dirs:
                        self.files.add(os.path.join(path.replace(self.cwd, '.'), directory))
            else:
                for path, dirs, files in os.walk(self.cwd):
                    for fil in files:
                        self.files.add(os.path.join(path.replace(self.cwd, '.'), fil))

        else:
            files = os.listdir(self.cwd)
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
        final_files = list(self.final_files)
        if len(final_files) > 10:
            i = int(len(final_files)/2)
            if self.colorize and self.only_directories:
                for x, y in zip(final_files[:i], final_files[i:]):
                    print('\033[93m {0: <30}{1} \033[0m'.format(x, y))
            elif self.colorize and not self.only_directories:
                for x, y in zip(final_files[:i], final_files[i:]):
                    print('\033[94m {0: <30}{1} \033[0m'.format(x, y))
            else:
                for x, y in zip(final_files[:i], final_files[i:]):
                    print('{0: <30}{1}'.format(x, y))
            return
        for fil in final_files:
            print ('\033[93m {} \033[0m'.format(fil) if self.colorize else fil)


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
