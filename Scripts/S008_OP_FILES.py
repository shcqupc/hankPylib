import os

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
print('os.path.listdir', os.listdir(os.getcwd()))
print('\n-----------------calc total size-------------------')
total_size = 0
file_list = os.listdir(os.getcwd())
for x in range(len(file_list)):
    total_size += os.path.getsize(os.path.join(os.getcwd(), file_list[x]))
print(total_size)
print('os.path.exists', os.path.exists(os.getcwd()))
print('os.path.isfile', os.path.isfile(os.getcwd()))
print('os.path.isdir', os.path.isdir(os.getcwd()))
