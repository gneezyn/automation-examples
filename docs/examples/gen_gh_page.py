#!/usr/bin/env python

"""
Generates the a HTML file that lists all of the files
in a directory.
"""

from __future__ import print_function
import os
import sys
import argparse
import shutil

html_header = ''.join([
'''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<title>Index of {directory}</title>
</head>
<body>
'''
])

html_section = '''
<object data="{file_path}" type="text/HTML" scrolling="no" frameborder="0" marginheight="0px" marginwidth="0px" height="100%" width="100%"></object>
'''

html_footer = '''
</body>
</html>
'''

get_input = getattr(__builtins__, 'raw_input', input)

def generate_file():
    """
    Goes through the directory and generates the HTML file.
    """
    print("\nGenerating the HTML file")
    html = html_header.format(directory=args.directory)
    cwd = os.getcwd()
    path = os.path.normpath(os.path.join(cwd, 'docs/examples', args.directory))
    for root, dirs, files in os.walk(path):
        for name in files:
            print(name)
            
            file_path = join_path_names('examples/', args.directory, name)
            html += html_section.format(file_path=file_path)

    file_path = os.path.join('docs/', args.file_name)
    with open(file_path, 'w') as index_file:
        index_file.write(html)

def join_path_names(path_one, path_two, *argv):
    full_path = os.path.normpath(path_one + '/' + path_two)
    for arg in argv:
        full_path = os.path.normpath(full_path + '/' + arg)
        
    return full_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generates the an HTML file that lists all of'
        ' the files in a directory.'
    )
    parser.add_argument(
        '--directory', default='indexgen',
        help='The directory that the files/folders are located in. By'
        ' default, it is set to the "indexgen" directory.')
    parser.add_argument(
        '--file-name', default='index.html',
        help='The name of the HTML file to be generated/updated. Should'
        ' contain the ".html" extension; default value is "indexgen.html".')
    args = parser.parse_args()

    generate_file()