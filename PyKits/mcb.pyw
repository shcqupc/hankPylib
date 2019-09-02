# -*-conding:utf-8-*
# ! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import sys
import os
import shelve
import pyperclip


def multiclipboard():
    print('begin')
    source_path = os.path.join(os.getcwd(), 'sources')
    print(source_path)
    print(os.path.exists(source_path))
    if not os.path.exists(source_path):
        os.mkdir(source_path)

    clips = shelve.open(r'.\sources\clips')
    # insert
    if len(sys.argv) == 3 and sys.argv[1] == 'save':
        clips[sys.argv[2]] = pyperclip.paste()

    # del
    # elif len(sys.argv[]) ==3 and sys.argv[1] == 'del':
    #     clips = shelve.open(r'.\sources\clips')

    # copy
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            pyperclip.copy(str(list(clips.keys())))
        elif sys.argv[1] in clips:
            pyperclip.copy(clips[sys.argv[1]])

    clips.close()


multiclipboard()
