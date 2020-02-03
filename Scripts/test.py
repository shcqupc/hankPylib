import re

for x in ("keep the your pass ABCDEFG other text",
          "your pass: TESTVALUE other text",
          "no pass required other text"):
    print(re.search('no\s+pass|pass:?\s+([A-Z]+)',x).group(1))


print(re.findall ( '[A-Z][a-z]+|[A-Z]+' , 'ABCdef'))
