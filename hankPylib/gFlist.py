"""--------------------------------------------------------
<<Get file list>>
os.listdir()
os.path.join(path1[, path2[, ...]])
gflist "D:/work/GIT/hankPylib/hankPylib/"
---------------------------------------------------------"""
import os,sys,pyperclip as pc

def getRawFileList(path): 
    files = []
    names = []
    for f in os.listdir(path):
        if not f.endswith("~") or not f == "":
            files.append(os.path.join(path, f))
            names.append(f)
    return files, names

def opList():
    path = ''
    fmt  = ''   
    try:
        path = sys.argv[1]
        fmt  = sys.argv[2]
    except Exception as e:
        print(e)
        
    print('\npath',path,'\nfmt',fmt)
    files = []
    names = []    
    files,names = getRawFileList(path)
    '''
    print("files:", files)
    print("\nnames:", names)
    '''
    vList = ''
    if fmt == "":
        for s in range(len(names)):
            vList = vList + names[s] + '\r\n'
    
    pc.copy(vList)

opList()    
