def commaList(vlist):
    ret = ''
    try:
        llen = len(vlist)
        if llen == 1:
            ret = vlist[0]
        elif llen > 1:
            for x in range(len(vlist)):
                if x == llen - 1:
                    ret = ret[:-2] + ' and ' + vlist[x - 1]
                else:
                    ret += vlist[x - 1] + ', '
        print(ret)
    except Exception as e:
        print('error occurs')
        print(str(e))


def pivotList(vList):
    pList = []
    for y in range(len(vList)):
        if y == 0:
            for x in range(len(vList[y])):
                pList.append([vList[y][x]])
        else:
            for x in range(len(vList[y])):
                pList[x].append(vList[y][x])

    for x in range(len(pList)):
        print(pList[x])

    for y in range(len(pList)):
        row = ''
        for x in range(len(pList[y])):
            row += pList[y][x]
        print(row)


def countChar(vString):
    count = {}
    for x in vString:
        count.setdefault(x, 0)
        count[x] = count[x] + 1
    print(count)
