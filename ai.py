from peices import Peice
from copy import deepcopy
import concurrent.futures
import time



#constants
LEVEL = 5

class AI:
    
    def __init__(self,peices):
        self.best_move = None
        self.peices = peices


    def get_score(self):
        score = 0.0
        for row in range(8):
            for col in range(8):
                
                if self.peices.is_white(row,col):
                    score+=1
                elif self.peices.is_black(row,col):
                    score-=1
                if self.peices.board[row][col] == 'X':
                    score+=.5
                elif self.peices.board[row][col] == 'Y':
                    score-=.5
        return score
        

    def get_all_moves(self,white):
        moves = []
        for row in range(8):
            for col in range(8):
                if (white and self.peices.is_white(row,col)) or (not white and self.peices.is_black(row,col)):
                   self.peices.check_moves(row,col,True,white,moves)
        return moves


    def make_move(self,move):
        
        row,col = move[:2]
        if move[2] == 'r':
            self.peices.treverse_right(row,col)
        elif move[2] == 'R':
            self.peices.treverse_right_back(row,col)
        elif move[2] == 'L':
            self.peices.treverse_left_back(row,col)
        elif move[2] == 'l':
            self.peices.treverse_left(row,col)

    
    
    def play_move(self):
        min_max(self)
        if self.best_move == None:
            print('cant make a move')
        else:
            self.make_move(self.best_move)
            self.best_move = None
        return True




def min_max(object,move = None,white = True,depth = LEVEL): #issue while mapping
    
        
    
        
    if(depth == LEVEL):
        
        all_moves = [moves for moves in object.get_all_moves(True) ]
        arg0 = [object for _ in range(len(all_moves))]
        arg1 = [False for _ in range(len(all_moves))] 
        arg2 = [depth-1 for _ in range(len(all_moves))]
        
        start = time.perf_counter()
        
        #WITH PARELLEL
        
        with concurrent.futures.ProcessPoolExecutor() as executor:
            eval = [(score,move) for score,move in zip( executor.map(min_max,arg0,all_moves,arg1,arg2),all_moves)]
                    
        
        

        #WITHOUT PARELLEL
        #eval = [(min_max(object,moves,False,depth-1),moves) for moves in all_moves ]
        
        print('move took ',time.perf_counter() - start,' sec')
        
        if eval != []:
            best_move = max(eval, key = lambda score: score[0])[1]

        object.best_move = best_move
        
        return

    else:
        temp_board = deepcopy(object.peices.board)
        object.make_move(move)



    if depth == 0 :
        object.peices.board = deepcopy(temp_board)
        return object.get_score()  



    if white:
        eval = [ min_max(object,moves,False,depth-1) for moves in object.get_all_moves(True) ]
        
        if eval != []:
            min_max_eval = max(eval)
        else:
            min_max_eval = -24

        

    elif not white:
        eval = [ min_max(object,moves,True,depth-1) for moves in object.get_all_moves(False) ]
        
        if eval != []:
            min_max_eval = min(eval)
        else:
            min_max_eval = 24

        
            
    object.peices.board = deepcopy(temp_board)
    return min_max_eval
