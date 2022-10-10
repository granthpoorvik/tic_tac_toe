#from helper import lis_of_ops as loo
#the upper import dose not concern with the tic tac toe code







import sys


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

who=None 
flag=False
def win_checker(lis):
    
    if theBoard[dict_map[lis[0]]]=='X':
        who='X'
        for i in lis[1:]:
            
                
            if theBoard[dict_map[int(i)]]=='X':
                flag=True
            else:
                return False,who

            
    else:
        who='O'
        for i in lis[1:]:
            if theBoard[dict_map[int(i)]]=='O':
                flag=True
            else:
                return False,who
            
    
    return flag,who
    


def winner(theboard):
    
    lis=[[1,2,3],[4,5,6],[7,8,9],
         [1,4,7],[2,5,8],[3,6,9],
         [1,5,9],[3,5,7]]
    for i in lis[0]:
        for j in lis:
            
            got=win_checker(j)
        if(got[0]==True):
            print(f"the winner is  {got[1]}")
            break
        else:

            print("NO one wone")
            continue 
   



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
winner(theBoard)