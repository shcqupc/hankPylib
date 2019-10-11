import re

reg = re.compile(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):')
print(reg.search('def myfunc():').group())
print(reg.search('def myfunc():').group(1))

outstr =re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
        r'static PyObject*\npy_\1(void)\n{',
        'def myfunc():', re.VERBOSE)
      

print(outstr)

