import shutil
import os

src_path = os.path.join(os.getcwd(), 'Sources')
des_path = os.path.join(os.getcwd(), 'tstSources')
print('src_path', src_path)
print('des_path', des_path)

print('\n-----------------copy-------------------')
try:
    shutil.copy(os.path.join(os.getcwd(), 'pip.bat'), src_path)
    shutil.copy('pyTst1.py', os.path.join(src_path, 'pyTst2.py'))
except Exception as e:
    print(e)

print('\n----------------copytree--------------------')
try:
    shutil.copytree(src_path, des_path)
except Exception as e:
    print(e)

print('\n----------------Moving and Renaming--------------------')
try:
    shutil.move(os.path.join(src_path, 'pip.bat'), des_path)
    shutil.move(os.path.join(src_path, 'pyTst2.py'), os.path.join(des_path, 'pyTst3.py'))
except Exception as e:
    print(e)

print('\n---------------Deleting ---------------------')
print(os.listdir(src_path))
dir_lst = os.listdir(src_path)
for x in range(len(dir_lst)):
    dir_list = os.path.join(des_path, dir_lst[x])
    if os.path.isfile(dir_list):
        print('unlink', dir_list)
        # os.unlink(dir_list)
    elif os.path.isdir(dir_list):
        print('rmtree', dir_list)
        # shutil.rmtree(dir_list)

print('\n---------------send2trash ---------------------')
import send2trash

# send2trash.send2trash(des_path)

print('\n----------------os.walk()--------------------')
for folderName, subfolders, filenames in os.walk(des_path):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
