spam = ['cat', 'bat', 'rat', 'elephant']
print("spam = ['cat', 'bat', 'rat', 'elephant']")
print("spam[1:3]:", spam[1:3])
print("spam[0:-1]:", spam[0:-1])
print("spam[:2]:", spam[:2])
print("spam[1:]:", spam[1:])
print("spam[:]:", spam[:])
print('spam:', spam)
print(chr(10))

print("spam1=[1, 2, 3]")
spam1 = [1, 2, 3]
print("spam+spam1:", spam + spam1)
print("(spam+spam1)*3:", (spam + spam1) * 3)

print(chr(10))
del spam[2]
print("del spam[2]:", spam)

print(chr(10))
print('list(range(0, -30, -5)):', list(range(0, -30, -5)))

print(chr(10))
print('----------loop list----------')
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
print("for i in range(len(supplies)):")
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print(chr(10))
print("----------Multiple assignment trick----------")
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size, color, disposition)
size, color, disposition = color, disposition, size
print(size, color, disposition)

print(chr(10))
print("----------sort----------")
print("spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']")
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(reverse=True)
print("spam.sort(reverse=True):", spam)
spam.sort(key=str.lower, reverse=True)
print("spam.sort(key=str.lower,reverse=True):", spam)

print(chr(10))
print("----------string list----------")
print("name = 'Zophie'")
name = 'Zophie'
for i in name:
    print('* * * ' + i + ' * * *')

print('\n----------------append() and insert()--------------------')
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam.insert(3, 'insert')
print(spam)

print('\n----------------remove()--------------------')
spam.remove('insert')
print(r"spam.remove('insert')",spam)

print(chr(10))
print("\n----------tuples immutable----------")
print("type(('hello',))", type(('hello',)))
eggs = ('hello',)
print("eggs[0] = 'AAA'")
try:
    eggs[0] = 'AAA'
except Exception as e:
    print('str(Exception):\t', str(Exception))
    print('str(e):\t\t', str(e))
    print('repr(e):\t', repr(e))
    print('e.message:\t', e)
    # print('e.message:\t',e.message)
    # print('traceback.print_exc():', traceback.print_exc())
    # print('traceback.format_exc():',traceback.format_exc())

print(chr(10))
print("----------tuples convertion----------")
print("tuple(['cat', 'dog', 5]):", tuple(['cat', 'dog', 5]))
print("list(('cat', 'dog', 5)):", list(('cat', 'dog', 5)))
print("list('hello'):", list(list('hello')))

print(chr(10))
print("----------list reference----------")
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
sh = spam
sh[1] = 'elephant'
print("sh[1]='elephant'")
print('sh:', sh)
print('spam:', spam)

# deepcopy
print(chr(10))
print("----------copy and deepcopy----------")
import copy

list1 = ['name', 'greate', 'nice', [1, 2, 3, 4, 5]]
print("list2 = copy.copy(list1)", "list3 = copy.deepcopy(list1)")
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
print("list1[3][1] = 99", "list1[1] = 11")
list1[1] = 11
list1[3][1] = 99
print('list1:', list1)
print('list2:', list2)
print('list3:', list3)

print('\n--------------pop-------------')
print(list3.pop(2))
print(list3)
