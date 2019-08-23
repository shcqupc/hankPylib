import sys,pyperclip

def concat():
    vStr = pyperclip.paste()
    print(vStr)
    try:
        print('sys.argv[1]',sys.argv[1])
        if sys.argv[1] == '':
            conLon = '\''
        else:
            conLon = sys.argv[1]
    except:
        conLon = '\''

    try:
        print('sys.argv[2]',sys.argv[2])
        if sys.argv[2] == '':
            sepChr = ','
        else:
            sepChr = sys.argv[2]
    except:
        sepChr = ',' 
            
    vList = vStr.split('\r\n')
    for x in range(len(vList)):
        vList[x] = conLon + vList[x] + conLon
    vStr = sepChr.join(vList)
    print('\n',vStr)
    pyperclip.copy(vStr)

concat()
