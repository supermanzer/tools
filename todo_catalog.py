#!/home/ryan/anaconda3/bin/python
import os
import sys


def find_todos():
    """
    A function for walking the directory of a project, scanning the code files, finding TODO statements, and building a catalogue of them. A directory can be passed as the first command line argument to initiate the process somewhere other than the current working directory.
    """
    # Checking to see if a directory was passed in
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = os.getcwd()

     # File extensions we will pay attention to. We will want to avoid any compiled files and stick to uncompiled script files.  If there are any that you would like to add, simply place them here.

    file_ext = ('.py', '.txt', '.php', '.js', '.css')
    for (dirname, dirs, files) in os.walk(root):
        for filename in files:
            if filename.endswith(file_ext):
                with open(os.path.join(dirname,filename),'r') as f:
                    for n, line in enumerate(f, 1):
                        if "TODO" in line:
                             # TODO: Write the function that collects the file name, task text, and writes to a TODO.txt file.
                            print("%i %s" % (n, line))



if __name__ == '__main__':
    find_todos()
