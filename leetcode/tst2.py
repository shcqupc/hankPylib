d1 = {'a': 2, 't': 1, 'c': 1, 'h': 1}
d2 = {'c': 1, 'a': 1, 't': 1}
# {'c': 1, 'a': 1, 't': 2, 'b': 1}
# {'c': 1, 'a': 2, 't': 3, 'b': 1, 'h': 1}
# {'c': 1, 'a': 2, 't': 4, 'b': 1, 'h': 1, 'r': 1, 'e': 2}
diff = d1.keys() & d2.keys()
print(type(diff))
print(set(d2))
# print(d1.keys() - d2.keys())
# print(d1.keys() - d2.keys())
# print(list(d2.keys()))
# print(list(d1.keys()))
if ['c', 'a', 't'] in ['a', 't', 'c', 'h']:
    print(True)