#Assignment-2, Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

from random import randint
# There are 2 players: player1 and player2
player1 = 1
player2 = 2

 
#  There are 9 tiles numbered tile0 to tile9
#  0 value of a tile indicates that tile has not been ticked
#  1 value indicates that the tile is ticked by player-1
#  2 value indicates that the tile is ticked by player-2

tile1=0
tile2=0
tile3=0
tile4=0
tile5=0
tile6=0
tile7=0
tile8=0
tile9=0


strategy_intelligent  = 3
x=1
# turn variable defines whose turn is now
turn = player1

def random_select():

    global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9
    count = tile_count(0)
    
    a = randint(1,count)

    count =0

    if tile1==0:
        count+=1
        if count == a:
            return 1
    if tile2==0:
        count+=1
        if count == a:
            return 2
        
    if tile3==0:
        count+=1
        if count == a:
            return 3
        
    if tile4==0:
        count+=1
        if count == a:
            return 4
    if tile5==0:
        count+=1
        if count == a:
            return 5
    if tile6==0:
        count+=1
        if count == a:
            return 6
    if tile7==0:
        count+=1
        if count == a:
            return 7
    if tile8==0:
        count+=1
        if count == a:
            return 8
    if tile9==0:
        count+=1
        if count == a:
            return 9
        
def tile_count(a):
    count =0
    global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9
    if tile1==a:
        count+=1
    if tile2==a:
        count+=1
    if tile3==a:
        count+=1
    if tile4==a:
        count+=1
    if tile5==a:
        count+=1
    if tile6==a:
        count+=1
    if tile7==a:
        count+=1
    if tile8==a:
        count+=1
    if tile9==a:
        count+=1
    


    return count


def validmove(move):
        """ Checks whether a move played by a player is valid or invalid.
                Return True if move is valid. 
                
                A move is valid if the corresponding tile for the move is not ticked.
        """
        global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9 
        
        for i in range(1,10):
            if i == move:
                if i==1:
                    if tile1 ==0:
                        return True
                if i==2:
                    if tile2 ==0:
                        return True
                if i==3:
                    if tile3 ==0:
                        return True
                if i==4:
                    if tile4 ==0:
                        return True
                if i==5:
                    if tile5 ==0:
                        return True
                if i==6:
                    if tile6 ==0:
                        return True
                if i==7:
                    if tile7 ==0:
                        return True
                if i==8:
                    if tile8 ==0:
                        return True
                if i==9:
                    if tile9 ==0:
                        return True
            else:
                return False

def win():
        """ Returns True if the board state specifies a winning state for some player.
                
                A player wins if ticks made by the player are present either
                i) in a row
                ii) in a cloumn
                iii) in a diagonal
        """
        global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9


        if tile1 == tile2 == tile3 != 0:
            return True
        if tile4 == tile5 == tile6 != 0:
            return True
        if tile7 == tile8 == tile9 != 0:
            return True
        if tile1 == tile4 == tile7 != 0:
            return True
        if tile2 == tile5 == tile8 != 0:
            return True
        if tile3 == tile6== tile9 != 0:
            return True        
        if tile1 == tile5==  tile9 != 0:
            return True
        if tile2== tile5== tile7 != 0:
            return True
        
        
        return False
                        
        
def takeNaiveMove():
        """ Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
        """
        global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9
        a = random_select()
        return a
        

def takeStrategicMove():
        """ Returns a tile number from the set of unchecked tiles
        using some rules.
        
        """
        global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9
        global strategy_intelligent
        global x

        
        if tile1 == tile2==turn and tile3 == 0:
            return 3
        if tile4 == tile5==turn and tile6 == 0:
            return 6
        if tile7 == tile8==turn and tile9 == 0:
            return 9
        if tile1 == tile4==turn and tile7 == 0:
            return 7
        if tile2 == tile5==turn and tile8 == 0:
            return 8
        if tile3 == tile6==turn and tile9 == 0:
            return 9        
        if tile1 == tile5==turn and  tile9 == 0:
            return 9
        if tile3 == tile5==turn and tile7 ==0:
            return 7
        
        if tile1 == tile3==turn and tile2 == 0:
            return 2
        if tile4 == tile6==turn and tile5 == 0:
            return 5
        if tile7 == tile9==turn and tile8 == 0:
            return 8
        if tile1 == tile7==turn and tile4 == 0:
            return 4
        if tile2 == tile8==turn and tile5 == 0:
            return 5
        if tile3 == tile9==turn and tile6 == 0:
            return 6        
        if tile1 == tile9==turn and  tile5 == 0:
            return 5
        if tile3== tile7==turn and tile5 ==0:
            return 5
        
        if tile3 == tile2==turn and tile1 == 0:
            return 1
        if tile6 == tile5==turn and tile4 == 0:
            return 4
        if tile9 == tile8 ==turn and tile7 == 0:
            return 7
        if tile7 == tile4==turn and tile1 == 0:
            return 1
        if tile8 == tile5==turn and tile2 == 0:
            return 2
        if tile9 == tile6==turn and tile3 == 0:
            return 3
        if tile9 == tile5==turn and  tile1 == 0:
            return 1
        if tile7== tile5==turn and tile3 ==0:
            return 3
        

        
        if turn ==1:
            notturn =2
        else:
            notturn =1

        
        

        
        if tile1 == tile2==notturn and tile3 == 0:
            return 3
        if tile4 == tile5==notturn and tile6 == 0:
            return 6
        if tile7 == tile8==notturn and tile9 == 0:
            return 9
        if tile1 == tile4==notturn and tile7 == 0:
            return 7
        if tile2 == tile5==notturn and tile8 == 0:
            return 8
        if tile3 == tile6==notturn and tile9 == 0:
            return 9        
        if tile1 == tile5==notturn and  tile9 == 0:
            return 9
        if tile3 == tile5==notturn and tile7 ==0:
            return 7
        
        if tile1 == tile3==notturn and tile2 == 0:
            return 2
        if tile4 == tile6==notturn and tile5 == 0:
            return 5
        if tile7 == tile9==notturn and tile8 == 0:
            return 8
        if tile1 == tile7==notturn and tile4 == 0:
            return 4
        if tile2 == tile8==notturn and tile5 == 0:
            return 5
        if tile3 == tile9==notturn and tile6 == 0:
            return 6        
        if tile1 == tile9==notturn and  tile5 == 0:
            return 5
        if tile3== tile7==notturn and tile5 ==0:
            return 5
        
        if tile3 == tile2==notturn and tile1 == 0:
            return 1
        if tile6 == tile5==notturn and tile4 == 0:
            return 4
        if tile9 == tile8 ==notturn and tile7 == 0:
            return 7
        if tile7 == tile4==notturn and tile1 == 0:
            return 1
        if tile8 == tile5==notturn and tile2 == 0:
            return 2
        if tile9 == tile6==notturn and tile3 == 0:
            return 3
        if tile9 == tile5==notturn and  tile1 == 0:
            return 1
        if tile7== tile5==notturn and tile3 ==0:
            return 3
        




        

        if tile1 == 0 and tile2 == 0 and tile3 == 0 and tile4 == 0 and tile5 == 0 and tile6 == 0 and tile7 == 0 and tile8 == 0 and tile9 == 0 :
                return 5
        if notturn == 1 or notturn ==2:
                if tile_count(notturn) == 1:
                        if tile5 == 0:
                                
                                if  tile2==notturn or tile4==notturn or tile6==notturn or tile8==notturn:
                                        strategy_intelligent =1
                                else:
                                        strategy_intelligent =2
                                return 5
                        else :
                                strategy_intelligent = 3
                                if tile1 == 0:
                                    return 1
                                if tile3 == 0:
                                    return 3
                        
                if tile_count(notturn) == 2:

                        
                        if strategy_intelligent == 1:
                                

                                
                                if tile2 == tile6 == notturn :
                                        x = 1
                                        return 3
                                if tile2 == tile4 == notturn :
                                        x = 1
                                        return  1
                                if tile8 == tile4 == notturn :
                                        x = 1
                                        return 7
                                if tile6 == tile8 == notturn :
                                        x = 1
                                        return 9


                                if tile2 == tile8 == notturn  or tile4 == tile6 == notturn:
                                        return 1


                                if tile1 == tile6 == notturn or tile1 == tile8 == notturn or tile3 == tile4 ==notturn or tile3 == tile8 == notturn:
                                        return 2
                                if tile7 == tile2 == notturn  or tile9 == tile2 == notturn:
                                        return 4
                                if  tile7 == tile6 == notturn or tile9 == tile4 ==notturn:
                                        return 8
                                

                        if strategy_intelligent == 2:


                                if tile1 == tile9 == notturn or tile3 == tile7 == notturn:
                                        return 1


                                if tile1 == tile6 == notturn or tile1 == tile8 == notturn or tile3 == tile4 ==notturn or tile3 == tile8 == notturn:
                                        return 2
                                if tile7 == tile2 == notturn  or tile9 == tile2 == notturn:
                                        return 4
                                if  tile7 == tile6 == notturn or tile9 == tile4 ==notturn:
                                        return 8

                                
                if tile_count(notturn) == 3:
                        
                        if x == 1:
                                if tile1 == 0:
                                        return 1
                                if tile3 == 0:
                                        return 3
                                if tile7 == 0:
                                        return 7
                                if tile9 == 0:
                                        return 9
                            
                                            

        return takeNaiveMove()
                                
                        
                        

        
def validBoard():
        """ Return True if board state is valid.
                
                A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
        """
        global flag
        x = tile_count(1)
        y = tile_count(2)
        if x>= y and x < 6:
                return True
        else:
                return False

def game(gametype=1):
        """ Returns 1 if player1 wins and 2 if player2 wins
                and 0 if it is a draw.
        
                gametype defines three types of games discussed above.
                i.e., game1, game2, game3
        """
        global tile1,tile2,tile3,tile4,tile5,tile5,tile6,tile7,tile8,tile9
        global turn
        turn=1
        tile1 =0
        tile2 =0
        tile3 =0
        tile4 =0
        tile5 =0
        tile6 =0
        tile7 =0
        tile8 =0
        tile9 =0

        
        if gametype == 1 :
                for i in range(9):
                        y  =  takeNaiveMove()
                        if y==1:
                            tile1 = turn
                        if y==2:
                            tile2 = turn
                        if y==3:
                            tile3 = turn
                        if y==4:
                            tile4 = turn
                        if y==5:
                            tile5 = turn
                        if y==6:
                            tile6 = turn
                        if y==7:
                            tile7 = turn
                        if y==8:
                            tile8 = turn
                        if y==9:
                            tile9 = turn
                        
                        if win() == True:
                                return turn
                        else:
                                if turn ==1:
                                        turn =2
                                else :
                                        turn =1
                
        if gametype == 2 :
                for i in range(9):
                        if i%2 == 0:
                                y  =  takeNaiveMove()
                        else:
                                y  =  takeStrategicMove()
                        if y==1:
                            tile1 = turn
                        if y==2:
                            tile2 = turn
                        if y==3:
                            tile3 = turn
                        if y==4:
                            tile4 = turn
                        if y==5:
                            tile5 = turn
                        if y==6:
                            tile6 = turn
                        if y==7:
                            tile7 = turn
                        if y==8:
                            tile8 = turn
                        if y==9:
                            tile9 = turn
       
                        if win() == True:
                                return turn
                        else:
                                if turn ==1:
                                        turn =2
                                else :
                                        turn =1

        if gametype == 3 :
                for i in range(9):
                        y  =  takeStrategicMove()
                        if y==1:
                            tile1 = turn
                        if y==2:
                            tile2 = turn
                        if y==3:
                            tile3 = turn
                        if y==4:
                            tile4 = turn
                        if y==5:
                            tile5 = turn
                        if y==6:
                            tile6 = turn
                        if y==7:
                            tile7 = turn
                        if y==8:
                            tile8 = turn
                        if y==9:
                            tile9 = turn
                      
                        if win() == True:
                                
                                return turn
                        else:
                                if turn ==1:
                                        turn =2
                                else :
                                        turn =1

        return 0
        
def game1(n):
        """ Returns the winning probability for player1. 
        
        n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
        """
        count =0
        for i in range (n):
                a=game(1)
                if a == 1:
                        count+=1
        return count/n
        

def game2(n):
        """Returns the winning probability for player1.
        
        n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
        """
        count =0
        for i in range (n):
                a=game(2)
                if a == 1:
                        count+=1
                
        return count/n

def game3(n):
        """Returns the winning probability for player1. 
        
        n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
        """
        count =0
        for i in range (n):
                a=game(3)
                if a == 1:
                        count+=1
        return count/n
        
if __name__ == '__main__':
        n =int(input('enter'))
        prob1 = game1(n)
        prob2 = game2(n)
        prob3 = game3(n)
        print(prob1)
        print(prob2)
        print(prob3)
