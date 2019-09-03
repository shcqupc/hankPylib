"""--------------------------------------------------------
<<Get file list>>
ls get full directories
ls b get list of basename
---------------------------------------------------------"""
import os
import sys
import pyperclip as pc


def listdir():
    working_directory = pc.paste()
    #working_directory = os.getcwd()
    print(working_directory)
    outstr = ''
    if len(sys.argv) == 1:
        list = os.listdir(working_directory)
        folder = []
        for x in range(len(list)):
            list[x] = os.path.join(working_directory, list[x])
            if not os.path.isfile(list[x]):
                folder.append(list[x])
                #print('folder', list[x])

        for y in folder:
            list.remove(y)
        outstr = '\n'.join(list)
        pc.copy(outstr)
        print(outstr)
    elif len(sys.argv) == 2 and sys.argv[1] == 'b':
        list = os.listdir(working_directory)
        outstr = '\n'.join(list)
        pc.copy(outstr)
        print(outstr)

listdir()
