import re

'''
vstr = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
regex = re.compile(r"Agent (\w)\w*")
print(regex.search(vstr))
print(regex.findall(vstr))
print(regex.sub(r'Agent \1*****', vstr))

print(type(re.search('', '')))
print(type(re.match('', '')))
print(re.match(r'(abc){2,}', 'abcabcabcabcabc').group())
regexn = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(regexn.search('asdfsdf086-852-9988asdfsa').group(0))
print(regexn.search('asdfsdf086-852-9988asdfsa').group(1))
print(regexn.search('asdfsdf086-852-9988asdfsa').group(2))
print(regexn.search('asdfsdf086-852-9988asdfsa').groups())

print(re.search('\(\w+\)', 'asdf(dsfds)dasdf').group())
print(re.findall('ab', 'dasabdcdabddaejkab'))
print(re.findall('(a)(b)', 'dasabdcdabddaejkab'))

text = "xx12   3xx"
try:
    match = re.search(r'\d\s+\d\s+\d', text)
    print(match.group())
except Exception as e:
    print(e)
try:
    match = re.search(r'\d\s*\d\s*\d', text)
    print(match.group())
except Exception as e:
    print(e)

numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))
'''
print('\n----------------thousand delimiter-------------')
vstr1 = '42'
vstr2 = '1,234'
vstr3 = '6,368,745'
vstr4 = '12,34,567'
vstr5 = '1234'
nfx = re.compile(r'^\d{1,3}(,\d{3})*$')
print(nfx.search(vstr1))
print(nfx.search(vstr2))
print(nfx.search(vstr3))
print(nfx.search(vstr4))
print(nfx.search(vstr5))

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)
print(emailRegex.search('sdfascde% hank_h_su@manulife.com ()fasdfas'))

print('\n----------------name-------------')
str1 = 'Satoshi Nakamoto'
str2 = 'Alice Nakamoto'
str3 = 'Robocop Nakamoto'
str4 = 'satoshi Nakamoto'
str5 = 'Mr. Nakamoto'
str6 = 'Nakamoto'
str7 = 'Satoshi nakamoto'
regexName = re.compile(r'[A-Z][a-z]+ Nakamoto')
print('str1', regexName.search(str1))
print('str2', regexName.search(str2))
print('str3', regexName.search(str3))
print('str4', regexName.search(str4))
print('str5', regexName.search(str5))
print('str6', regexName.search(str6))
print('str7', regexName.search(str7))

regexname2 = re.compile(r'((Alice)|(Bob)|(Carol))\s((eats)|(pets)|(throws))\s((apples)|(cats)|(baseballs))', re.I)
print(regexname2.search('Alice eats apples.').group())
print(regexname2.search('Robocop eats apples.'))

print('\n-------------Strong Password Detection-------------')


def validpwd(pwd):
    regexpwd1 = re.compile(r'([a-z]|[A-Z]|[0-9]){8,}')
    regexpwd2 = re.compile(r'\d{1,}')
    try:
        regexpwd1.search(pwd).group()
    except Exception as e:
        return False

    try:
        regexpwd2.search(pwd).group()
    except Exception as e:
        return False

    return True

print(validpwd('asbdASDF'))
print(validpwd('asbd1ASDF'))
print(validpwd('asbdA_SDF'))

print('\n-------------self defined strip-------------')
def strip(string, sstr):
    if len(string) > 0:
        if sstr == '':
            reg1 = re.compile(r'^(\s*)(\w\W)*(\s*)$')
            reg1.sub('',string,)

