import sys
import pyperclip
print('bullet begin')
vStr = pyperclip.paste()
bullet = sys.argv[1]
print('bullet:', bullet)
vList = vStr.split('\n')
# print('vList:',vList)
for x in range(len(vList)):
    vList[x] = bullet + vList[x]
    # print(vList[x])
vStr = '\n'.join(vList)
pyperclip.copy(vStr)
print(vStr)
