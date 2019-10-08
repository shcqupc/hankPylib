print('\n--------loop-----')
list = []
for x in range(1, 11, 2):
    print(x)
    list.append(x ** 2)
print(list)

list2 = []
list2 = [x ** 2 for x in range(1, 15, 3)]
print(list2)

n = 0
while n <= 15:
    print(n)
    n += 1


def multInput(a, *b):
    print(a + ":" + str(b))

multInput('ab', 'cd', 'ef', 'gh', 'ij')
