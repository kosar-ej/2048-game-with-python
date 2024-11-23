import random
import numpy as np
import os
game=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
print('*this is 2048 game*')
ch=input('do you want to start yes or no...')
#this function first add two random number in a random location to the matrix
def start(game):
    n=1
    while n<=2:
        row=random.randint(0,3)
        column=random.randint(0,3)
        for i in range(4):
            for j in range(4):
                if i==row and j==column:
                    cr=random.choice([2,2,4,2,2,2,2,2,2,4])
                    game[i,j]=cr
                    
        n+=1
    return game
if ch=='yes':
    game=start(game)
recorde=0
num=0
x=0
#this is the main loop of the game, which is repeated and the game continues until the user enter the q key 
while ch=='yes':
    ch='yes'
    #this function add one random number in a random location after moving
    def apeand_2(game):
        row=random.randint(0,3)
        column=random.randint(0,3)
        
        for i in range(4):
            for j in range (4):
                if i==row and j==column:
                    if game[i][j]==0:
                        cr=random.choice([2,2,4,2,2,2,2,2,2,4])
                        game[i,j]=cr
                    else:
                        apeand_2(game)
                           
        return game
    if x!=0:
        game=apeand_2(game)
        game_over(game)
    os.system('cls')
    print(game)
    print('your recorde is:',recorde)
    print('number of your corecct move is:',num)
    x+=1
    #this function scroll the matrix and print it
    def show_matrix(game):
        for i in range(4):
            for j in range(4):
                print(game[i,j])
    #this function checks whether the user has won or not
    def won(game):
        for i in range(4):
            for j in range(4):
                if game[i][j]== 2048:
                    print("you won")
                    ch="no"
    #this function checks whether the matrix cells are filled or not       
    def game_over(game):
        m=0
        for i in range(4):
            for j in range(4):
                if game[i][j]!=0:
                    m+=1
        if m==16:
            max(game)
            print('game over!!!')
            ch='no'
            exit()
    #this function causes the number of each row to come to the left position
    def move_left(game):
        new_game=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        for i in range(4):
            n=0
            for j in range(4):
                if game[i][j]!=0:
                    new_game[i][n]=game[i][j]
                    n+=1
        return new_game
    #this function reverse the matrix
    def reverse_row(game):
        new_game=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        for i in range(4):
            n=3
            for j in range(4):
                new_game[i,j]=game[i,n]
                n-=1
        return new_game
    #this function swaps rows and columns of the matrix
    def tranahade(game):
        new_game=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        for i in range(4):
            for j in range(4):
                new_game[i][j]=game[j][i]
        return new_game
    
    def max(game):
        max=0
        for i in range(4):
            for j in range(4):
                if game[i][j]>max:
                    max=game[i][j]
        
        print('>>>the max number is:',max)

    #>>enter d to move right
    #>>enter a to move left
    #>>enter w to move up
    #>>enter s to scroll down
    #>>enter r to reset
    #>>enter q to exit
    
    move=input('enter the move...if you dont want to continue press the key q...')

    if move=="q":
        asck=input('are you sure you want to exit? yes or no...')
        if asck=='yes':
            ch='no'
            max(game)
            print('game over!!!')
    if move=='r':
        asc=input('are you sure you want to reset? yes or no...')
        if asc=='yes':
            game=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
            game=start(game)
            os.system('cls')
            print(game)
            print('your recorde is:',recorde)
            print('number of your corecct move is:',num)
            move=input('enter the move...if you dont want to continue press the key q...')

    if move=="a":
        a1=move_left(game)
        for i in range(4):
            for j in range(3):
                if a1[i][j]==a1[i][j+1] and a1[i][j]!=0:
                    a1[i][j]+=a1[i][j+1]
                    recorde+=a1[i][j]
                    
                    a1[i][j+1]=0
                    game=a1
                    
                else:
                    game=a1
                    recorde=recorde

        num+=1
        
                
    if move=="d":
        d1=reverse_row(game)
        d2=move_left(d1)
        for i in range(4):
            for j in range(3):
                if d2[i][j]==d2[i][j+1] and d2[i][j]!=0:
                    d2[i][j]+=d2[i][j+1]
                    recorde+=d2[i][j]
                    
                    d2[i][j+1]=0
                    d3=reverse_row(d2)
                    game=d3
                    
                else:
                    d3=reverse_row(d2)
                    game=d3
                    recorde=recorde
                    
        num+=1
        
                    
    if move=="w":
        w1=tranahade(game)
        w2=move_left(w1)
        for i in range(4):
            for j in range(3):
                if w2[i][j]==w2[i][j+1] and w2[i][j]!=0:
                    w2[i][j]+=w2[i][j+1]
                    recorde+=w2[i][j]
                    
                    w2[i][j+1]=0
                    w3=tranahade(w2)
                    game=w3
                                       
                else:
                    w3=tranahade(w2)
                    game=w3
                    recorde=recorde
                    
        num+=1
        

    if move=="s":
        s1=tranahade(game)
        s2=reverse_row(s1)
        s3=move_left(s2)
        for i in range(4):
            for j in range(3):
                if s3[i][j]==s3[i][j+1] and s3[i][j]!=0:
                    s3[i][j]+=s3[i][j+1]
                    recorde+=s3[i][j]
                    
                    s3[i][j+1]=0
                    s4=reverse_row(s3)
                    s5=tranahade(s4)
                    game=s5
                                        
                else:
                    s4=reverse_row(s3)
                    s5=tranahade(s4)
                    game=s5
                    recorde=recorde
                    
        num+=1
        
    game_over(game)
    won(game)
        

                    
    

                    
    
                    
    