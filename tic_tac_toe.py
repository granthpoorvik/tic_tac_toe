#from helper import lis_of_ops as loo
#the upper import dose not concern with the tic tac toe code

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
    
    loc=input(f"enter the location of the  {move} !---------------->")
    while True:
        if theBoard[dict_map[int(loc)]]!=' ':
            print(f"the move is unauthorised it has been already tacken by {theBoard[dict_map[int(loc)]]} at location {loc} ")
            loc=input(f"enter the location of the move! of {move}")
        else:
            

        
    
            theBoard[dict_map[int(loc)]]=move
            if move=='X':
                move='O'
            else:
                move='X'
            printBoard(theBoard)
            break
       