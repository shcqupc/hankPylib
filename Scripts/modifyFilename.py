import os

# included_extensions = ['py']
file_list = [fn for fn in os.listdir() if fn[0] == 'S']
# file_list = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_extensions)]
# print(file_list)
for idx,fn in enumerate(file_list):
    # print(os.path.join(os.getcwd(),fn),os.path.join(os.getcwd(),"LC"+str(idx+1).rjust(4,'0')+fn[5:]))
    os.rename(os.path.join(os.getcwd(),fn),os.path.join(os.getcwd(),"LC"+str(idx+1).rjust(4,'0')+fn[5:]))
