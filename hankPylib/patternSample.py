message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print('------without regex-------')

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

for i in range(len(message)):
   chunk = message[i:i+12]
   #print(chunk)
   if isPhoneNumber(chunk):
     print('Phone number found: ' + chunk)
print('Done')


print('------with regex-------')
import re
regex = re.compile(r'\d{3}-\d{3}-\d{4}')
regexGrp = re.compile(r'(\d{3})-(\d{3}-\d{4})')
print(regex.search(message).group())
print(regex.search(message).group())
print(regex.match(message))
print(regex.findall(message))
print(regexGrp.search(message).groups())
areaCode, mainNumber = regexGrp.search(message).groups()
print(areaCode,mainNumber,sep=' ** ')


print('----------Optional Matching with the Question Mark---------')
