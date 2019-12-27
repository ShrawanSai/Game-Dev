
import random
import numpy as np




def initial_setup(board):
    board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    vals=[2,2,2,2,4,2,2,2,2,2]
    for i in range(2):
        random.shuffle(vals)
        v=vals[0]
        x=random.randint(0,3)
        y=random.randint(0,3)
        if board[x][y]!=0:
            initial_setup([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
            
        else:
            board[x][y]=v
    return board

def genrate_block(board):
    print(board)
    x=random.randint(0,3)
    y=random.randint(0,3)
    if board[x][y]!=0:
        genrate_block(board)
    else:
        board[x][y]=2
    return board



def key_right(board):
    for row in range(len(board[0])):
        for col in range(len(board)-1,-1,-1):
            c=0
            while board[row][col]==0 and c<5:
                board[row].pop(col)
                board[row].insert(0,0)
                c+=1
    for row in range(len(board[0])):
        for col in range(len(board)-1,0,-1):
            if board[row][col]==board[row][col-1]:
                board[row][col]+=board[row][col-1]
                board[row].pop(col-1)
                board[row].insert(0,0)
    return board


def key_left(board):
    for row in range(len(board[0])):
        for col in range(0,len(board)):
            c=0
            while board[row][col]==0 and c<5:
                board[row].pop(col)
                board[row].insert(3,0)
                c+=1
    for row in range(len(board[0])):
        for col in range(len(board)-1):
            if board[row][col]==board[row][col+1]:
                board[row][col]+=board[row][col+1]
                board[row].pop(col+1)
                board[row].insert(3,0)
    return board

def key_up(board):
    b=np.array(board)
    b=b.T
    b=b.tolist()
    for row in range(len(b[0])):
        for col in range(0,len(b)):
            c=0
            while b[row][col]==0 and c<5:
                b[row].pop(col)
                b[row].insert(3,0)
                c+=1
    for row in range(len(b[0])):
        for col in range(len(b)-1):
            if b[row][col]==b[row][col+1]:
                b[row][col]+=b[row][col+1]
                b[row].pop(col+1)
                b[row].insert(3,0)
    b=np.array(b)
    b=b.T
    b=b.tolist()
    board=b
    return board

def key_down(board):
    b=np.array(board)
    b=b.T
    b=b.tolist()
    for row in range(len(b[0])):
        for col in range(len(b)-1,-1,-1):
            c=0
            while b[row][col]==0 and c<5:
                b[row].pop(col)
                b[row].insert(0,0)
                c+=1
    for row in range(len(b[0])):
        for col in range(len(b)-1,0,-1):
            if b[row][col]==b[row][col-1]:
                b[row][col]+=b[row][col-1]
                b[row].pop(col-1)
                b[row].insert(0,0)
    b=np.array(b)
    b=b.T
    b=b.tolist()
    board=b
    return board



'''
board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board=initial_setup(board)


for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col],end='')
        print('\n')

while True:
    
    prev=board
    move=input('Enter l,r,u,d-  ')
    if move=='l':
        board=key_left(board)
    elif move=='r':
        board=key_right(board)
    elif move=='u':
        board=key_up(board)
    elif move=='d':
        board=key_down(board)
    board=genrate_block(board)

    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[row][col],end='')
        print('\n')'''




