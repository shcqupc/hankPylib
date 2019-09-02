# -*-conding:utf-8-*-
import os

from Scripts.Sources import myCats

print('\n-----------------os.getcwd-------------------')
print(os.getcwd())
os.chdir(r'E:\Downloads')
print(os.getcwd())

print('\n--------------os.makedirs()----------------------')
os.chdir(r'D:\PycharmProjects\hankPylib\Scripts')
# os.makedirs(r'.\newfolder')

print('\n------------------os.path----------------------')
print(os.path.join('aa', 'bb', 'cc'))
print('os.path.abspath', os.path.abspath('.'))
print('os.path.relpath', os.path.relpath(os.path.abspath('.'), r'D:\vim\src\auto'))
print('os.path.dirname', os.path.dirname(r"D:\vim\src\auto\configure"))
print('os.path.basename', os.path.basename(r"D:\vim\src\auto\configure"))
print('os.path.split', os.path.split(r"D:\vim\src\auto\configure"), os.path.split(r"D:\vim\src\auto\configure")[0])
print('os.path.sep', os.getcwd().split(os.path.sep))
print('os.path.getsize', os.path.getsize(r"D:\PycharmProjects\hankPylib\Scripts\S002_listSample.py"))
print('os.listdir', os.listdir(os.getcwd()))
print('\n-----------------calc total size-------------------')
total_size = 0
file_list = os.listdir(os.getcwd())
for x in range(len(file_list)):
    total_size += os.path.getsize(os.path.join(os.getcwd(), file_list[x]))
print(total_size)
print('os.path.exists', os.path.exists(os.getcwd()))
print('os.path.isfile', os.path.isfile(os.getcwd()))
print('os.path.isdir', os.path.isdir(os.getcwd()))

print('\n---------------read()--------------------')
file1 = open(os.path.join(os.getcwd(), r'Sources\new_file'))
old_content1 = file1.read()
print(file1.read())
file1.close()
file2 = open(os.path.join(os.getcwd(), r'Sources\new_file'))
print('file2.readlines()', file2.readlines())
file2.close()
file3 = open(os.path.join(os.getcwd(), r'Sources\new_file'))
old_content2 = file3.readline()
print('file3.readline()', old_content2)
file3.close()

print('\n---------------write()---------------------')
file4 = open(os.path.join(os.getcwd(), r'Sources\new_file'), 'w')
file4.write(old_content2)
file4.close()
file4 = open(os.path.join(os.getcwd(), r'Sources\new_file'), 'a')
file4.write(old_content1)
file4.close()

file4 = open(os.path.join(os.getcwd(), r'Sources\new_file'), 'r')
print(file4.read())
file4.close()

print('\n----------------shelve write-------------------')
import shelve

shelfFile = shelve.open('Sources\shelfFile')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
print('\n----------------shelve read--------------------')
shelfFile = shelve.open('Sources\shelfFile')
print(shelfFile['cats'])
print('shelfFile.keys()', list(shelfFile.keys()))
shelfFile.close()

print('\n----------------pprint and import--------------------')
import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(cats)
pprint.pprint(cats)
# print(pprint.pformat(cats))
fileObj = open('sources\myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import Scripts.Sources.myCats

print(myCats.cats)
