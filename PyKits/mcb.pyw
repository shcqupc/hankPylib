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
    source_path = os.path.join(os.path.dirname(__file__), 'sources')
    print(source_path)
    print(os.path.exists(source_path))
    if not os.path.exists(source_path):
        os.mkdir(source_path)
    # print('len(sys.argv)',len(sys.argv))
    # print('sys.argv[0]', sys.argv[0])
    # print('sys.argv[1]', sys.argv[1])
    # print('sys.argv[2]', sys.argv[2])
    clips = shelve.open(os.path.join(source_path, 'clips'))
    # add new key
    if len(sys.argv) == 3 and sys.argv[1] == 'save':
        clips[sys.argv[2]] = pyperclip.paste()
    # copy value
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'list':
            pyperclip.copy(str(list(clips.keys())))
        elif sys.argv[1] in clips:
            pyperclip.copy(clips[sys.argv[1]])
    elif len(sys.argv) == 2 and sys.argv[1] == 'del':
        clips.clear()

    clips.close()


multiclipboard()
