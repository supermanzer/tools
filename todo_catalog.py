#!/usr/bin/python
import os
import sys
import re

def find_todos():
    """
    A function for walking the directory of a project, scanning the code files, finding TODO statements, and building a catalogue of them. A directory can be passed as the first command line argument to initiate the process somewhere other than the current working directory.  It will create or overwrite a TODO.txt document in the root folder.
    """
    # Checking to see if a directory was passed in
    if len(sys.argv) > 1:
        root = sys.argv[1]
    else:
        root = os.getcwd()

     # File extensions we will pay attention to. We will want to avoid any compiled files and stick to uncompiled script files.  If there are any that you would like to add, simply place them here.
    file_ext = ('.py', '.txt', '.php', '.js', '.css')

    #  Writing our TODO.txt file
    td=open(os.path.join(root,'TODO.txt'),'w+')

    # TODO: Write test to ensure this text is found and returned

    # Walking our directory tree with a counter variable
    k=1
    for (dirname, dirs, files) in os.walk(root):
        for filename in files:
            if filename.endswith(file_ext):
                # We dont need to confuse collaborators by including those portions of the project path that are specific to the machine on which this is run.  So we truncate the print_file variable to only include file paths relative to the root directory.
                print_file=os.path.join(dirname,filename)
                print_file=print_file.replace(root+'/','')
                with open(os.path.join(dirname,filename),'r') as f:
                    for n, line in enumerate(f, 1):
                        if "TODO" in line:
                            mObj=re.match(r'.*TODO:*\s*(.*)',line)
                            out_text= "#%i) %s line %i - %s \n" % (k,print_file,n,mObj.group(1))
                            td.write(out_text)
                            k+=1



if __name__ == '__main__':
    find_todos()
