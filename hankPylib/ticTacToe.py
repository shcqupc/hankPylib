#! python3
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

printBoard(theBoard)


def checkWin(board):
    isFull = 'Y'
    isEmpty = 'Y'
    vList = [['','',''],['','',''],['','','']]
    vList[0][0] = board['top-L']
    vList[0][1] = board['top-M']
    vList[0][2] = board['top-R']
    vList[1][0] = board['mid-L']
    vList[1][1] = board['mid-M']
    vList[1][2] = board['mid-R']
    vList[2][0] = board['low-L']
    vList[2][1] = board['low-M']
    vList[2][2] = board['low-R']

    for y in range(len(vList)):
        for x in range(len(vList[y])):
            if vList[y][x] !=  ' ':
                isEmpty = 'N'
                break
            
    if isEmpty == 'Y':
        return 'N'
    else:
        for y in range(len(vList)):
            for x in range(len(vList[y])):
                try:
                    if vList[y][x] != ' ' and vList[y][x] == vList[y][x+1] and vList[y][x] == vList[y][x+2]:
                        win = 'Y'
                    else:
                        win = 'N'                    
                except:
                    win = 'N'

                if win == 'Y':
                    #print('vertical x:',x,' y:',y)
                    return 'Y'
                
                try:
                    if vList[y][x] != ' ' and vList[y][x] == vList[y+1][x] and vList[y][x] == vList[y+2][x]:
                        win = 'Y'
                    else:
                        win = 'N'                    
                except:
                    win = 'N'

                if win == 'Y':
                    #print('vertical x:',x,' y:',y)
                    return 'Y'
                
                try:
                    if vList[y][x] != ' ' and vList[y][x] == vList[y+1][x+1] and vList[y][x] == vList[y+2][x+2]:
                        win = 'Y'
                    else:
                        win = 'N'                    
                except:
                    win = 'N'

                if win == 'Y':
                    #print('down cross x:',x,' y:',y)
                    return 'Y'

                try:
                    if (vList[y][x] != ' '
                        and y >= 2
                        and vList[y][x] == vList[y-1][x+1]
                        and vList[y][x] == vList[y-2][x+2]):
                        win = 'Y'
                    else:
                        win = 'N'                    
                except:
                    win = 'N'

                if win == 'Y':
                    print('up cross x:',x,' y:',y)
                    print('vList[y][x]:',vList[y][x])
                    print('vList[y-1][x+1]:',vList[y-1][x+1])
                    print('vList[y-2][x+2]:',vList[y-2][x+2])                    
                    return 'Y'                

        for y in range(len(vList)):
            for x in range(len(vList[y])):
                if vList[y][x] == ' ':
                    isFull = 'N'
                    break
        if isFull == 'Y':
            print(vList)
            return 'E'
        else:
            return 'N'
    
def runGame(board):
    marker = 'X'
    
    def switchMarker(marker):
        if marker == 'X':
            return 'O'
        else:
            return 'X'

    def isNewgame(board):        
        print('Start a new game? Y/N')
        isNew = input()
        if str.upper(isNew) == 'Y':
            for k in board.keys():
                board[k] = ' '
            printBoard(board)
            return True
        else:
            return False
        
    while True:
        if checkWin(board) == 'N':
            marker = switchMarker(marker)
            print('Turn for ' + marker + ' Which cell do you want to place? ')        
            place = input()
            if place in ('top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R'):
                if board[place] == ' ':
                   board[place] = marker
                   printBoard(board)
                else:
                    print('Choose a blank cell')
                    marker = switchMarker(marker)
                    printBoard(board)
                    continue
            else:
                print('Incorrect place')
                marker = switchMarker(marker)          
                printBoard(board)
                continue
        elif checkWin(board) == 'E':
            print('Draw.')
            if isNewgame(board):
                continue
            else:
                break
            
        else:
            print('Winner is ' + marker + '!!!')
            if isNewgame(board):
                continue
            else:
                break
    
runGame(theBoard)
#checkWin(theBoard)    
