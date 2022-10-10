from helper import lis_of_ops as loo

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' \
', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoard)
dict_map={}
i=1
for k in theBoard.keys():
    dict_map[i]=k
    i+=1



move='X'
for i in range (9):
    #printBoard(theBoard)
    loc=input(f"enter the location of the move! of {move}")
    
    theBoard[dict_map[int(loc)]]=move
    if move=='X':
        move='O'
    else:
        move='X'
    printBoard(theBoard)