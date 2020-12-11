import pygame
from interface import Interface
from peices import Peice
from ai import AI

#constants
SIZE = 500




board = [[None,'x',None,'x',None,'x',None,'x'],
        ['x',None,'x',None,'x',None,'x',None],
        [None,'x',None,'x',None,'x',None,'x'],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        ['y',None,'y',None,'y',None,'y',None],
        [None,'y',None,'y',None,'y',None,'y'],
        ['y',None,'y',None,'y',None,'y',None]]







if __name__ == "__main__":
    
    win = pygame.display.set_mode((SIZE,SIZE))
    pygame.display.set_caption('Checkers AI optimization')
    clock = pygame.time.Clock()

    peices = Peice(board)
    game = Interface(win,peices)
    bot = AI(peices)

    play = True
    player_turn = True
    
    game.update()
    
    while play:
        clock.tick(60)

        if not player_turn:
            player_turn = bot.play_move()
            game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                break

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if player_turn:
                    #game.update()
                    row,col = game.get_pos(pygame.mouse.get_pos())
                    game.select(row,col)
                    player_turn = game.make_move(row,col)


    pygame.quit()
 