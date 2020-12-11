from peices import Peice
import pygame


#constants
YELLOW = (252, 202, 3)
SIZE = 500
ROW = COL = 8
SQUARE_SIZE = SIZE//COL

BLACK = (0,0,0)
WHITE = (250,250,250)
OFFWHITE = (232, 235, 233)
GREY = (128,128,128)
BLUE = (62, 122, 82)
RED = (255, 181, 186)

class Interface:

    def __init__(self,win,peices):
        self.win = win
        self.selected_men = None
        self.peices = peices


    def trigger_kill(self,row,col):
        pygame.draw.circle(self.win, RED, ((SQUARE_SIZE*(col+1))-SQUARE_SIZE//2, (SQUARE_SIZE*(row+1))-SQUARE_SIZE//2),( SQUARE_SIZE//2)-10)

    def trigger_move(self,row,col):
        pygame.draw.rect(self.win, BLUE, ((col)*SQUARE_SIZE, (row)*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    def men(self,color,row,col,king):
        if king:
            kcolor = YELLOW
        else:
            kcolor = GREY
        pygame.draw.circle(self.win, kcolor, ((SQUARE_SIZE*col)-SQUARE_SIZE//2, (SQUARE_SIZE*row)-SQUARE_SIZE//2), (SQUARE_SIZE//2)- 8)
        pygame.draw.circle(self.win, color, (((SQUARE_SIZE*col)-SQUARE_SIZE//2), ((SQUARE_SIZE*row)-SQUARE_SIZE//2)-1),( SQUARE_SIZE//2)-10)



    def draw_board(self):
            self.win.fill(BLACK)
            for row in range(ROW):
                for col in range(row % 2, COL, 2):
                    pygame.draw.rect(self.win, WHITE, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))



    def draw_mens(self):
        for row in range(1,9):
            for col in range(1,9):
                if self.peices.board[row-1][col-1] == None:
                    continue
            
                elif self.peices.board[row-1][col-1] == 'x':
                    self.men(OFFWHITE,row,col,False)
                elif self.peices.board[row-1][col-1] == 'X':
                    self.men(OFFWHITE,row,col,True)
                elif self.peices.board[row-1][col-1] == 'y':
                    self.men(BLACK,row,col,False)
                elif self.peices.board[row-1][col-1] == 'Y':
                    self.men(BLACK,row,col,True)





    def update(self):
        self.draw_board()
        self.draw_mens()
        pygame.display.update()




    def select(self,row,col):
        
        self.update() #fix required
        if self.peices.is_black(row,col):
            self.peices.check_moves(row,col,False,False,self)
            self.selected_men = (row,col)

        pygame.display.update()



    def make_move(self,row,col):
        
        if self.selected_men == None:
            return True

        r = self.selected_men[0]
        c = self.selected_men[1]

        if self.selected_men == (row+1,col-1):
            self.peices.treverse_right_back(r,c)
            self.update()
            self.selected_men = None
            return False

        elif self.selected_men == (row+1,col+1):
            self.peices.treverse_left_back(r,c)
            self.update()
            self.selected_men = None
            return False
             
        elif self.peices.board[r][c] == 'Y' and self.selected_men == (row-1,col-1):
            self.peices.treverse_right(r,c)
            self.update()
            self.selected_men = None
            return False

        elif self.peices.board[r][c] == 'Y' and self.selected_men == (row-1,col+1):
            self.peices.treverse_left(r,c)
            self.update()
            self.selected_men = None
            return False

        return True

        



    def get_pos(self,pos):
        return pos[1]//SQUARE_SIZE,pos[0]//SQUARE_SIZE