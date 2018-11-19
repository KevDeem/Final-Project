import numpy as np 
import pygame
import sys
import math
from connect4settings import config


#Getting the settings
settings = config()
settings2 = config()

#global variables
ROW_COUNT = 0
COLOUM_COUNT = 0
color1 = 0
color2 = 0

#menuscreen settings
screen_menu=pygame.display.set_mode((settings.screen_width, settings.screen_height))

#font for the menu
font = settings.font


#Funtion to create the texts
def text_format(message, textFont, textSize, textColor):
	newFont=pygame.font.Font(textFont, textSize)
	newText=newFont.render(message, 0, textColor)
	return newText


#Player 1 winning
def player_1():
	global width
	menu = True
	selected = "start"

	while menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			#Actions in the main menu
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					settings.arrowclick()
					selected = "start"

				elif event.key == pygame.K_DOWN:
					settings.arrowclick()
					selected = "quit"

				if event.key == pygame.K_RETURN:
					pygame.mixer.music.stop()
					if selected == "start":
						settings.menuclick()
						level_menu()

					if selected == "quit":
						settings.menuclick()
						pygame.quit()
						quit() 

		#Texts in the menu
		#screen_menu.fill(WHITE)
		title=text_format("PLAYER 1 WINS!", font, 60, settings.WHITE)
		if selected == "start":
			text_start = text_format("REPLAY", font, 30, settings.GREY)
		else: 
			text_start = text_format("REPLAY", font, 30, settings.WHITE)
		if selected == "quit":
			text_quit = text_format("QUIT", font, 30, settings.GREY)
		else:
			text_quit = text_format("QUIT", font, 30, settings.WHITE) 

		title_rect = title.get_rect()
		start_rect = text_start.get_rect()
		quit_rect = text_quit.get_rect() 

		# Rendering the text into the screen
		screen_menu.blit(title, (width / 2 - (title_rect[2] / 2), 80))
		screen_menu.blit(text_start, (width / 2 - (start_rect[2] / 2), 240))
		screen_menu.blit(text_quit, (width / 2 - (quit_rect[2] / 2), 280))
		pygame.display.update()
		pygame.display.set_caption("Connect 4 By KevDeem")


#Player 2 win


def player_2():
	global width
	menu = True
	selected = "start"

	while menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			#Actions in the main menu
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					settings.arrowclick()
					selected = "start"

				elif event.key == pygame.K_DOWN:
					settings.arrowclick()
					selected = "quit"

				if event.key == pygame.K_RETURN:
					if selected == "start":
						settings.menuclick()
						level_menu()

					if selected == "quit":
						settings.menuclick()
						pygame.quit()
						quit() 

		#Texts in the meun
		title=text_format("PLAYER 2 WINS!", font, 60, settings.WHITE)
		if selected == "start":
			text_start = text_format("REPLY", font, 30, settings.GREY)
		else: 
			text_start = text_format("REPLY", font, 30, settings.WHITE)
		if selected == "quit":
			text_quit = text_format("QUIT", font, 30, settings.GREY)
		else:
			text_quit = text_format("QUIT", font, 30, settings.WHITE) 

		title_rect = title.get_rect()
		start_rect = text_start.get_rect()
		quit_rect = text_quit.get_rect()

		# Rendering the text into the screen
		screen_menu.blit(title, (width / 2 - (title_rect[2] / 2), 80))
		screen_menu.blit(text_start, (width / 2 - (start_rect[2] / 2), 300))
		screen_menu.blit(text_quit, (width / 2 - (quit_rect[2] / 2), 360))
		pygame.display.update()
		pygame.display.set_caption("Connect 4 By KevDeem")


#menu to choose difficulty
def level_menu():
	settings2.gamesong()
	display = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	global ROW_COUNT
	global COLOUM_COUNT

	menu=True
	selected = ["small", "medium", "large"]
	selected_index = 0

	while menu:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			#going throught the available options in the array
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					settings.arrowclick()
					if selected_index != 0:
						selected_index -= 1

				elif event.key == pygame.K_DOWN:
					settings.arrowclick()
					if selected_index != len(selected) - 1:
						selected_index += 1

				#actions in the manu
				if event.key == pygame.K_RETURN:
					settings.menuclick()
					if selected[selected_index] == "small":
						ROW_COUNT = 6
						COLOUM_COUNT = 7
						color_1_menu()

					elif selected[selected_index] == "medium":
						ROW_COUNT = 8
						COLOUM_COUNT = 9 
						color_1_menu()

					elif selected[selected_index] == "large":
						ROW_COUNT = 12
						COLOUM_COUNT = 13    
						color_1_menu() 

		#creating the ui for the menu
		screen_menu.fill(settings.WHITE)
		title = text_format("CHOOSE BOARD SIZE", font, 60, settings.BLACK)
		if selected[selected_index] == "small":
			text_easy = text_format("SMALL", font, 30, settings.GREY)
		else: 
			text_easy = text_format("SMALL", font, 30, settings.BLACK)

		if selected[selected_index] == "medium":
			text_medium = text_format("MEDIUM", font, 30, settings.GREY)
		else:
			text_medium = text_format("MEDIUM", font, 30, settings.BLACK)

		if selected[selected_index] == "large":
			text_hard = text_format("LARGE", font, 30, settings.GREY)
		else:
			text_hard = text_format("LARGE", font, 30, settings.BLACK)

		#getting the rect parameters for screen_menu.blit
		title_rect = title.get_rect()
		easy_rect = text_easy.get_rect()
		medium_rect = text_medium.get_rect()
		hard_rect = text_hard.get_rect()

		#render the text into the screen
		screen_menu.blit(title, (settings.screen_width / 2 - (title_rect[2] / 2), 80))
		screen_menu.blit(text_easy, (settings.screen_width / 2 - (easy_rect[2] / 2), 300))
		screen_menu.blit(text_medium, (settings.screen_width / 2 - (medium_rect[2] / 2), 360))
		screen_menu.blit(text_hard, (settings.screen_width / 2 - (hard_rect[2] / 2), 420))
		pygame.display.update()


#Funtion for player 1 to choose colours
def color_1_menu():
	global color1
	menu=True
	selected = ["PINK", "RED", "TEAL"]
	selected_index = 0

	while menu:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

			#going through the available options in the array
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					settings.arrowclick()
					if selected_index != 0:
						selected_index -= 1

				elif event.key == pygame.K_DOWN:
					settings.arrowclick()
					if selected_index != len(selected) - 1:
						selected_index += 1

				#actions in the menu
				if event.key == pygame.K_RETURN:
					settings.menuclick()
					if selected[selected_index] == "PINK":
						color1 = settings.PINK
						color_2_menu()
					elif selected[selected_index] == "RED":
						color1 = settings.RED
						color_2_menu()
					elif selected[selected_index] == "TEAL":
						color1 = settings.TEAL
						color_2_menu()

		
		screen_menu.fill(settings.WHITE)
		title = text_format("PLAYER 1 CHOOSE COLOR", font, 50, settings.BLACK)
		if selected[selected_index] == "PINK":
			text_pink = text_format("PINK", font, 30, settings.GREY)
		else: 
			text_pink = text_format("PINK", font, 30, settings.PINK)
		if selected[selected_index] == "RED":
			text_red = text_format("RED", font, 30, settings.GREY)
		else:
			text_red = text_format("RED", font, 30, settings.RED)
		if selected[selected_index] == "TEAL":
			text_teal = text_format("TEAL", font, 30, settings.GREY)
		else:
			text_teal = text_format("TEAL", font, 30, settings.TEAL)

		#getting the rect for the screen_menu.blit
		title_rect = title.get_rect()
		pink_rect = text_pink.get_rect()
		red_rect = text_red.get_rect()
		teal_rect = text_teal.get_rect()

		# Rendering the text into the screen
		screen_menu.blit(title, (settings.screen_width / 2 - (title_rect[2] / 2), 80))
		screen_menu.blit(text_pink, (settings.screen_width / 2 - (pink_rect[2] / 2), 300))
		screen_menu.blit(text_red, (settings.screen_width / 2 - (red_rect[2] / 2), 360))
		screen_menu.blit(text_teal, (settings.screen_width / 2 - (teal_rect[2] / 2), 420))
		pygame.display.update()



#function for player 2 to choose colors
def color_2_menu():
	global color2
	menu=True
	selected = ["ORANGE", "YELLOW", "PURPLE"]
	selected_index = 0

	while menu:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

			 #going through the available options in the array
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					settings.arrowclick()
					if selected_index != 0:
						selected_index -= 1

				elif event.key == pygame.K_DOWN:
					settings.arrowclick()
					if selected_index != len(selected) - 1:
						selected_index += 1

				 #Action in the menu
				if event.key == pygame.K_RETURN:
					settings.menuclick()
					if selected[selected_index] == "ORANGE":
						color2 = settings.ORANGE
						game()

					elif selected[selected_index] == "YELLOW":
						color2 = settings.YELLOW
						game()

					elif selected[selected_index] == "PURPLE":
						color2 = settings.PURPLE
						game()

		#UI
		screen_menu.fill(settings.WHITE)
		title = text_format("PLAYER 2 CHOOSE COLOR", font, 50, settings.BLACK)
		if selected[selected_index] == "ORANGE":
			text_orange = text_format("ORANGE", font, 30, settings.GREY)
		else: 
			text_orange = text_format("ORANGE", font, 30, settings.ORANGE)
		if selected[selected_index] == "YELLOW":
			text_yellow = text_format("YELLOW", font, 30, settings.GREY)
		else:
			text_yellow = text_format("YELLOW", font, 30, settings.YELLOW)
		if selected[selected_index] == "PURPLE":
			text_purple = text_format("PURPLE", font, 30, settings.GREY)
		else:
			text_purple = text_format("PURPLE", font, 30, settings.PURPLE)


		#getting the rect for the screen_menu.blit
		title_rect = title.get_rect()
		orange_rect = text_orange.get_rect()
		yellow_rect = text_yellow.get_rect()
		purple_rect = text_purple.get_rect()

		# Rendering the text into the screen
		screen_menu.blit(title, (settings.screen_width / 2 - (title_rect[2] / 2), 80))
		screen_menu.blit(text_orange, (settings.screen_width / 2 - (orange_rect[2] / 2), 300))
		screen_menu.blit(text_yellow, (settings.screen_width / 2 - (yellow_rect[2] / 2), 360))
		screen_menu.blit(text_purple, (settings.screen_width / 2 - (purple_rect[2] / 2), 420))
		pygame.display.update()


def game():	
	global color1
	global color2
	global width

	
	#creating the board
	def board():
		global ROW_COUNT
		global COLOUM_COUNT

		#making the board have 0 as values in each list
		board = np.zeros((ROW_COUNT, COLOUM_COUNT))
		return board
	

	#function for the pieces
	def pieces(board, row, coloum, piece):
		board[row][coloum] = piece
	
	#checking if row is full
	def location(board, coloum):
		return board[ROW_COUNT - 1][coloum] == 0
	  
	
	#checking where to put the next piece that gets dropped
	def next_row(board, coloum):
		for r in range(ROW_COUNT):
			if board[r][coloum] == 0:
		
				return r
				

	#printing the board upside down so that it could be filled from the bottom up
	def print_board(board):
		print(np.flip(board, 0))
	
	
	#checking if there are 4 pieces of the same colour
	def win(board, piece):
		#check horizontal
		for c in range(COLOUM_COUNT - 3):
			for r in range(ROW_COUNT):
				if board [r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board [r][c + 3] == piece:
					return True
	
		#check vertical
		for c in range(COLOUM_COUNT):
			for r in range(ROW_COUNT - 3):
				if board [r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board [r + 3][c] == piece:
					return True
	
		#check right diagonal
		for c in range(COLOUM_COUNT - 3):
			for r in range(ROW_COUNT - 3):
				if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
					return True
	
		#check left diagonal
		for c in range(COLOUM_COUNT - 3):
			for r in range(3, ROW_COUNT):
				if board [r][c] == piece and board[r - 1][c + 1]  == piece and board[r - 2][c + 2] == piece and board [r - 3][c + 3] == piece:
					return True
	
	
	#Drawing the board into the screen
	def draw_board(board):
		#Drawing the individual rectangles according to the difficulty
		for c in range(COLOUM_COUNT):
			for r in range(ROW_COUNT):
				#drawing the blue rectangle board 
				pygame.draw.rect(screen, settings.BLUE, (c * settings.SQUARESIZE, r * settings.SQUARESIZE + settings.SQUARESIZE, settings.SQUARESIZE, settings.SQUARESIZE))
				#drawing the empty circles
				pygame.draw.circle(screen, settings.BLACK, (int(c * settings.SQUARESIZE + settings.SQUARESIZE / 2),  int(r * settings.SQUARESIZE + settings.SQUARESIZE + settings.SQUARESIZE / 2)), RADIUS)

		#Making the colored circles according to which player the circle belongs to
		for c in range(COLOUM_COUNT):
			for r in range(ROW_COUNT):
				if board[r][c] == 1:
					pygame.draw.circle(screen,  color1, (int(c * settings.SQUARESIZE + settings.SQUARESIZE / 2), height - int(r * settings.SQUARESIZE + settings.SQUARESIZE / 2)), RADIUS)
				elif board[r][c]== 2:
					pygame.draw.circle(screen, color2, (int(c * settings.SQUARESIZE + settings.SQUARESIZE / 2), height -  int(r * settings.SQUARESIZE + settings.SQUARESIZE / 2)), RADIUS)
		pygame.display.update()
	
	
	board = board()
	print_board(board)
	game_end = False
	turn = 0
	
	pygame.init()
		
	#Screen variables
	width = COLOUM_COUNT * settings.SQUARESIZE
	height = (ROW_COUNT + 1) * settings.SQUARESIZE
	size = (width, height)
	
	#radius for the circle
	RADIUS = int(settings.SQUARESIZE / 2 - 5)
	
	#screen settings
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Connect 4")
	draw_board(board)
	pygame.display.update()


	while not game_end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			
			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(screen, settings.BLACK, (0, 0, width, settings.SQUARESIZE))
				posx = event.pos[0]
				#drawing the current player circle into the screen
				if turn == 0:
					pygame.draw.circle(screen, color1, (posx, int(settings.SQUARESIZE / 2)), RADIUS)
				else:
					pygame.draw.circle(screen, color2, (posx, int(settings.SQUARESIZE / 2)), RADIUS)

			pygame.display.update()
	
			if event.type == pygame.MOUSEBUTTONDOWN:
				settings.arrowclick()

				#Player 1
				if turn == 0:
					#checking the position of the cursor
					posx = event.pos[0]
					coloum = int(math.floor(posx / settings.SQUARESIZE))
					
					#checking if the clicked position has any empty spots
					if location(board, coloum):
						row = next_row(board, coloum)
						pieces(board, row, coloum, 1)
						draw_board(board)
					
					#checking if player 1 has won
					if win(board, 1): 
						print("player 1 win")
						settings2.winsound()
						player_1()

				#player 2
				else:
					#checking the position of the cursor
					posx = event.pos[0]
					coloum = int(math.floor(posx / settings.SQUARESIZE))
	
					if location(board, coloum):
						row = next_row(board, coloum)
						pieces(board, row, coloum, 2)
						draw_board(board)
	
					if win(board, 2):
						print("player 2 win")
						settings2.winsound()
						player_2()	
			
				#printing the board into the repl
				print_board(board)
				

				turn += 1 
				turn = turn % 2
	
			
	
#Author for the game https://www.youtube.com/channel/UCq6XkhO5SZ66N04IcPbqNcw

#author for the menu https://www.sourcecodester.com/tutorials/python/11784/python-pygame-simple-main-menu-selection.html

#Special thanks to Ms. Monica, Asoka, and Michael Berlian for helping me everyday so I can finish this work








