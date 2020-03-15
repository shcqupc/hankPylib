import os

print(os.getcwd())
included_extensions = ['py']
file_list = [fn for fn in os.listdir() if fn[0] == 'S']
# file_list = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_extensions)]
print(file_list)

