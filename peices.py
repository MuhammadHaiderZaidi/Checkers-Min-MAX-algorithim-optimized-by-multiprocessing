#from interface import Interface

class Peice:

    def __init__(self,board):
        self.board = board
        self.white_moves = {}
        self.black_moves = {}
        self.empty_cells = {}




    def is_king(self,row,col):
        return self.board[row][col] == 'Y' or self.board[row][col] == 'X'

    def is_white(self,row,col):
        return self.board[row][col] == 'x' or self.board[row][col] == 'X'
    
    def is_black(self,row,col):
        return self.board[row][col] == 'y' or self.board[row][col] == 'Y'





    def check_moves(self,row,col,ai_trun,white,object = None): #black y , white x

        if white:

            check1 = 'y'
            check2 = 'Y'
        else:

            check1 = 'x'
            check2 = 'X'

        
        if not white or self.board[row][col] == 'X': #white is king or black

            if row>0 and col>0 and self.board[row-1][col-1] == None:
                if ai_trun:
                    object.append((row,col,'L'))
                else:
                    object.trigger_move(row-1,col-1)


            if row>0 and col<7 and self.board[row-1][col+1] == None:
                if ai_trun:
                    object.append((row,col,'R'))
                else:
                    object.trigger_move(row-1,col+1)
                    

        if not white:

            if row>1 and col>1 and (self.board[row-1][col-1] == check1) and self.board[row-2][col-2] == None:
                if ai_trun:
                    object.append((row,col,'L'))
                else:
                    object.trigger_kill(row-1,col-1)
                    

            if row>1 and col<6 and (self.board[row-1][col+1 ] == check1) and self.board[row-2][col+2] == None:
                if ai_trun:
                    object.append((row,col,'R'))
                else:
                    object.trigger_kill(row-1,col+1)
                    




        if white or self.board[row][col] == 'Y': #if black is king or white 
    
            if row<7 and col<7 and self.board[row+1][col+1] == None:
                if ai_trun:
                    object.append((row,col,'r'))
                else:
                    object.trigger_move(row+1,col+1)
                    

            if row<7 and col>0 and self.board[row+1][col-1] == None:
                if ai_trun:
                    object.append((row,col,'l'))
                else:
                    object.trigger_move(row+1,col-1)
                      
            
        if white:

            if row<6 and col>1 and (self.board[row+1][col-1 ] == check1) and self.board[row+2][col-2] == None:
                if ai_trun:
                    object.append((row,col,'l'))
                    
            
            if row<6 and col<6 and (self.board[row+1][col+1] == check1) and self.board[row+2][col+2] == None:
                if ai_trun:
                    object.append((row,col,'r'))
                    



        if self.is_king(row,col):

            if row>1 and col>1 and (self.board[row-1][col-1] == check1 or self.board[row-1][col-1] == check2) and self.board[row-2][col-2] == None:
                if ai_trun:
                    object.append((row,col,'L'))
                else:
                    object.trigger_kill(row-1,col-1)
                    

            if row>1 and col<6 and (self.board[row-1][col+1 ] == check1 or self.board[row-1][col+1 ] == check2) and self.board[row-2][col+2] == None:
                if ai_trun:
                    object.append((row,col,'R'))
                else:
                    object.trigger_kill(row-1,col+1)
                    

            if row<6 and col>1 and (self.board[row+1][col-1 ] == check1 or self.board[row+1][col-1 ] == check2) and self.board[row+2][col-2] == None:
                if ai_trun:
                    object.append((row,col,'l'))
                else:
                    object.trigger_kill(row+1,col-1)
                    
            
            if row<6 and col<6 and (self.board[row+1][col+1] == check1 or self.board[row+1][col+1] == check2) and self.board[row+2][col+2] == None:
                if ai_trun:
                    object.append((row,col,'r'))
                else:
                    object.trigger_kill(row+1,col+1)
                    









    def treverse_left(self,row,col): #l
        
        if row<7 and col>0 and self.board[row+1][col-1] == None:
            st = self.board[row][col]
            self.board[row][col] = None
            self.board[row+1][col-1] = st
            row+=1
            col-=1
        else:
            row,col = self.kill_left(row,col )
            
        if self.board[row][col] == 'x' and row == 7:
            self.board[row][col] = 'X'
                

                    
    def treverse_right(self,row,col): #r
        
        if row<7 and col<7 and self.board[row+1][col+1] == None:
            st = self.board[row][col]
            self.board[row][col] = None
            self.board[row+1][col+1] = st
            row+=1
            col+=1
        else:
            row,col = self.kill_right(row,col )

        if self.board[row][col] == 'x' and row == 7:
            self.board[row][col] = 'X'




    def treverse_left_back(self,row,col ): #L

        if row>0 and col>0 and self.board[row-1][col-1] == None: #fix moving indexes issues
                st = self.board[row][col]
                self.board[row][col] = None
                self.board[row-1][col-1] = st
                row-=1
                col-=1
        else:
            row,col = self.kill_left_back(row,col )

        if self.board[row][col] == 'y' and row == 0:
            self.board[row][col] = 'Y'



    def treverse_right_back(self,row,col ): #R
    
        if row>0 and col<7 and self.board[row-1][col+1] == None:
            st = self.board[row][col]
            self.board[row][col] = None
            self.board[row-1][col+1] = st
            row-=1
            col+=1
        else:
            row,col = self.kill_right_back(row,col )

        if self.board[row][col] == 'y' and row == 0:
            self.board[row][col] = 'Y'

    
    
    def kill_left(self,row,col):

        if self.board[row][col] == 'Y':

            check1 = 'x'
            check2 = 'Y'
            check3 = 'X'
        else:
            check1 = 'y'
            check2 = 'X'
            check3 = 'Y'

        while True:
            if row<6 and col>1 and( (self.board[row+1][col-1] == check1 and self.board[row+2][col-2] == None) or (self.board[row][col] == check2 and self.board[row+1][col-1] == check3 and self.board[row+2][col-2] == None)):
                st = self.board[row][col]
                self.board[row][col] = None
                self.board[row+1][col-1] = None
                self.board[row+2][col-2] = st
                row+=2
                col-=2
                row,col = self.kill_right(row,col )

                if self.board[row][col] == 'Y' or self.board[row][col] == 'X':
                    row,col = self.kill_left_back(row,col )
                    row,col = self.kill_right_back(row,col )

                continue

            break

        return row,col
        




    def kill_right(self,row,col ):
        
        
        if self.board[row][col] == 'Y':

            check1 = 'x'
            check2 = 'Y'
            check3 = 'X'
        else:
            check1 = 'y'
            check2 = 'X'
            check3 = 'Y'


        while True:
            if row<6 and col<6 and ( (self.board[row+1][col+1] == check1 and self.board[row+2][col+2] == None) or (self.board[row][col] == check2 and self.board[row+1][col+1] == check3 and self.board[row+2][col+2] == None) ):
                st = self.board[row][col]
                self.board[row][col] = None
                self.board[row+1][col+1] = None
                self.board[row+2][col+2] = st
                row+=2
                col+=2
                row,col = self.kill_left(row,col )

                if self.board[row][col] == 'Y' or self.board[row][col] == 'X':
                    row,col = self.kill_left_back(row,col )
                    row,col = self.kill_right_back(row,col )
                
                continue

            break

        return row,col
                

                    

    def kill_left_back(self,row,col): 
        
        if self.board[row][col] == 'X':

            check1 = 'y'
            check2 = 'X'
            check3 = 'Y'
        else:
            check1 = 'x'
            check2 = 'Y'
            check3 = 'X'

        while True:
            if row>1 and col>1 and( (self.board[row-1][col-1] == check1 and self.board[row-2][col-2] == None) or (self.board[row][col] == check2 and self.board[row-1][col-1] == check3 and self.board[row-2][col-2] == None)):
                st = self.board[row][col]
                self.board[row][col] = None
                self.board[row-1][col-1] = None
                self.board[row-2][col-2] = st
                row -= 2
                col -= 2
                row,col = self.kill_right_back(row,col )

                if self.board[row][col] == 'Y' or self.board[row][col] == 'X':
                    row,col = self.kill_right(row,col)
                    row,col = self.kill_left(row,col )
                
                continue

            break

        return row,col



    def kill_right_back(self,row,col ):
        if self.board[row][col] == 'X':
            check1 = 'y'
            check2 = 'X'
            check3 = 'Y'
            
            
        else:
            check1 = 'x'
            check2 = 'Y'
            check3 = 'X'
            
        


        while True:
            if row>1 and col<6 and ( (self.board[row-1][col+1] == check1 and self.board[row-2][col+2] == None) or (self.board[row][col] == check2 and self.board[row-1][col+1] == check3 and self.board[row-2][col+2] == None)):
                st = self.board[row][col]
                self.board[row][col] = None
                self.board[row-1][col+1] = None
                self.board[row-2][col+2] = st
                row -=2
                col +=2
                row,col = self.kill_left_back(row,col )
                if self.board[row][col] == 'Y' or self.board[row][col] == 'X':
                    row,col = self.kill_right(row,col)
                    row,col = self.kill_left(row,col )
                
                continue

            break

        return row,col

