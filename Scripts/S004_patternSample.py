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
print(regex.match(message))
print('findall:',regex.findall(message))
print('group findall:',regexGrp.findall(message))
print('groups:',regexGrp.search(message).groups())
print('group0:',regexGrp.search(message).group(0))
print('group1:',regexGrp.search(message).group(1))
areaCode, mainNumber = regexGrp.search(message).groups()
print(areaCode,mainNumber,sep=' ** ')

print('\n----------Curly Brackets---------')
batRegex1 = re.compile(r'Bat(wo)*man')
batRegex2 = re.compile(r'Bat(wo){3,}man')
mo1 = batRegex1.search('The Adventures of Batwoman')
print('mo1',mo1)
print(mo1.group())
try:
    mo2 = batRegex2.search('The Adventures of Batwoman')
    print('mo2',mo2)
    print(mo2.group())
except Exception as e:
    print('e.message:\t',e)
mo2 = batRegex2.search('The Adventures of Batwowowowoman')
print('mo2',mo2)
print(mo2.group())

batRegex1 = re.compile(r'(Ha){3,5}')
batRegex2 = re.compile(r'((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))')
print(type(batRegex1))
print(batRegex1 == batRegex2)


print('\n----------Greedy and Nongreedy Matching---------')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
nongreedyHaRegex = re.compile(r'(Ha)+?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

print('\n--------Character Classes--\d\D\w\W\s\S []---------')
print('\d',re.search(r'(\d{3})+','abcdef123456').group())
print('\D',re.search(r'(\D{3})+','123456abcdef').group())
print('\w',re.search(r'\w+','%^&1aB_**').group())
print('\W',re.search(r'\W+','%^&1aB_**').group())
print(re.search(r'\s+','%^&1a B_**').group())
print(re.search(r'\S+','%^&1a B_**').group())
print(re.search(r'[\S|\s]+','%^&1a B_**').group())

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))

print('\n--------Caret and Dollar---------')
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890').group())
print(wholeStringIsNum.search('12345xyz67890'))

print('\n--------Wildcard  and Dot-Star---------')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

Regex1 = re.compile(r'<.*?>')
print(Regex1.search('<To serve man>abc <for dinner>').group())
Regex2 = re.compile(r'<.*>')
print(Regex2.search('<To serve man>abc <for dinner>').group())

print('\n--------re.DOTALL---------')
noNewline = re.compile('.*')
print(noNewline.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
newLine = re.compile('.*', re.DOTALL)
print(newLine.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

print('\n--------Case-Insensitive---------')
vStr = 'abCDefG'
reGex = re.compile(r'AB', re.I)
print(reGex.search(vStr).group())

print('\n--------substitution---------')
namesRegex = re.compile(r'Agent \w+')
outStr = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(outStr)
agentNamesRegex = re.compile(r'Agent (\w)\w*')

outStr = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(outStr)

print('\n--------VERBOSE---------')
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


print('\n--------Combining ---------')
comRegex = re.compile(r'''
foo.*''', re.IGNORECASE | re.DOTALL | re.VERBOSE)
print(comRegex.search('Serve FOO.\nProtect the innocent.'))
