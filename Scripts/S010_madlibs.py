# -*-conding:utf-8-*
# #! python3
import re


def madlibs():
    print('\n------------------------------------')
    sentence = r'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
    print(sentence)
    # reg = re.compile(r'(.*)(NOUN)+?(.*)')
    # reg = re.compile(r'(.*?)(NOUN)(.*)')
    # print(reg.search(sentence).group())
    # print(reg.search(sentence).group(1))
    # print(reg.search(sentence).group(2))
    # print(reg.search(sentence).group(3))

    print('\n-----------------Enter an adjective:-------------------')
    adj = input()
    # print(str(adj))
    print('\n-----------------Enter an noun:-------------------')
    noun1 = input()
    # print(str(noun1))
    print('\n-----------------Enter an verb:-------------------')
    verb = input()
    # print(str(verb))
    print('\n-----------------Enter an noun:-------------------')
    noun2 = input()
    # print(str(noun2))

    adj_re = re.compile(r'ADJECTIVE')
    outstr = adj_re.sub(adj, sentence)
    print('adj_re', outstr)

    noun1_re = re.compile(r'NOUN')
    outstr = noun1_re.sub(noun1, outstr, 1)
    print(outstr)

    verb_re = re.compile(r'VERB')
    outstr = verb_re.sub(verb, outstr)
    print(outstr)

    noun2_re = re.compile(r'NOUN')
    outstr = noun2_re.sub(noun2, outstr)
    print(outstr)


madlibs()
