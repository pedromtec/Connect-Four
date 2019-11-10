import pygame
import sys
import math
from board import Board
from minimax import get_best_move
import matplotlib.pyplot as plt
import time

RED = (170, 0, 0) #red
BLACK = (0,0,0)
BLUE = (0,100,255)
YELLOW = (230,230, 0)

game_over = False

def draw_board(board):
	for c in range(Board.COLUMNS):
		for r in range(Board.ROWS):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(Board.COLUMNS):
		for r in range(Board.ROWS):		
			if board.get(r, c) == Board.PLAYER:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board.get(r, c) == Board.OPONENTE: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()

pygame.init()
pygame.display.set_caption('ConnectFour')

SQUARESIZE = 100

width =  Board.COLUMNS * SQUARESIZE
height = (Board.ROWS+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)

board = Board()

draw_board(board)

pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)
turn = 0
rodadas = []
tempo = []
numero_de_nos = []
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if board.player == Board.PLAYER:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN and board.player == Board.PLAYER:
            posx = event.pos[0]
            col = int(math.floor(posx//SQUARESIZE))
            board.drop_piece(col)
            print(board)
        elif board.player == Board.OPONENTE:
            turn+=1
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            label = myfont.render("  Thinking... ", 1, YELLOW)
            screen.blit(label, (40,10))
            pygame.display.update()
            before = time.time()
            move = get_best_move(board)
            rodadas.append(turn)
            tempo.append(time.time() - before)
            numero_de_nos.append(move[1])
            print(move)
            board.drop_piece(move[0][0])
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            print(board)
        
        if board.winner:
            game_over = True
            if board.winner == Board.PLAYER:
                label = myfont.render("You won!!", 1, RED)
                screen.blit(label, (40,10))
            else:
                label = myfont.render("You Lose!!", 1, YELLOW)
                screen.blit(label, (40,10))
        draw_board(board)
        if game_over:
            pygame.time.wait(3000)
'''            
plt.plot(rodadas, tempo) 
  
# function to show the plot 
plt.show() 
'''

print(rodadas)
print(tempo)
print(numero_de_nos)