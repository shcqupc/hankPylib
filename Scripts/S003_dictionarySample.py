#Dictionary
print('-------Birthday---------')
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

    print('birthdays:',birthdays)



print(chr(10))
print('-------keys() values() items()---------')
print("spam = {'color': 'red', 'age': 42}")
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print("for v in spam.values():",v)
for k in spam.keys():
    print("for k in spam.keys():",k)
for i in spam.items():
    print("for i in spam.items():",i)
for k, v in spam.items():
    print("for k, v in spam.items():",k,v)
    
print("spam.keys():",spam.keys())
print("list(spam.keys()):",list(spam.keys()))
print("for k, v in spam.items():")
print('color in spam:','color' in spam)
print('42 in spam:',42 in spam)
print('42 in spam.values():',42 in spam.values())

print(chr(10))
print("-------spam.get()---------")
print("spam.get('eggs', 0)",'I am bringing ' + str(spam.get('eggs', 0)) + ' eggs.')

print(chr(10))
print("-------spam.setdefault('color', 'black')---------")
print("spam.setdefault('weight', 10)", spam.setdefault('weight', 10))
print(spam)

print(chr(10))
print("-------pprint.pprint()---------")
import pprint
message = '''It was a bright cold day in April, and the clocks were striking thirteen.'''
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
pprint.pprint(count)
vStr = pprint.pformat(count)
print(vStr)
