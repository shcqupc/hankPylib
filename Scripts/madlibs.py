import re


def madlibs():
    print('\n------------------------------------')
    sentence = r'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
    print(sentence)
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

    # adjre = re.compile(r'(.*)(ADJECTIVE)(.*)')
    adj_re = re.compile(r'ADJECTIVE')
    outstr = adj_re.sub(adj, sentence)
    # print('adj ', outstr)

    noun1_re = re.compile(r'(.*)(NOUN)(.*)')
    print(noun1_re.search(outstr).group())
    outstr = noun1_re.sub(r'\\2'+noun1, outstr)
    print('noun1', outstr)

    # verb_re = re.compile(r'(VERB)+')
    #     # outstr = verb_re.sub(verb_re, outstr)
    #     # print(outstr)

madlibs()
