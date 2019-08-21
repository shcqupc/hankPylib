import sys, pyperclip
vStr = pyperclip.paste()
print('vStr:',vStr)
bullet = sys.argv[1]
print('bullet:',bullet)
vList = vStr.split('\n')
#print('vList:',vList)
for x in range(len(vList)):
    vList[x] = bullet + vList[x]
    #print(vList[x])
vStr = '\n'.join(vList)
pyperclip.copy(vStr)
