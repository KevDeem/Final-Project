import pygame
from pygame.locals import *
import connect4
from connect4 import level_menu
from connect4settings import config

#import the settings
settings = config()
settings2 = config()

#Initializing the menu
pygame.init()

# Screen settings
screen=pygame.display.set_mode((settings.screen_width, settings.screen_height))

# fonts
font = settings.font 

#getting the structures of the text 
def text_format(message, textFont, textSize, textColor):
	newFont = pygame.font.Font(textFont, textSize)
	newText = newFont.render(message, 0, textColor)

	return newText


#Starting the main menu
def main_menu():
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
					settings.menuclick()
					if selected == "start":
						level_menu()
					if selected == "quit":
						pygame.quit()
						quit()


		#Texts in the meun
		screen.fill(settings.WHITE)
		title=text_format("CONNECT 4", font, 60, settings.RED)
		if selected == "start":
			text_start = text_format("START", font, 30, settings.GREY)
		else: 
			text_start = text_format("START", font, 30, settings.BLACK)
		if selected == "quit":
			text_quit = text_format("QUIT", font, 30, settings.GREY)
		else:
			text_quit = text_format("QUIT", font, 30, settings.BLACK)

		title_rect = title.get_rect()
		start_rect = text_start.get_rect()
		quit_rect = text_quit.get_rect()

		# Rendering the text into the screen
		screen.blit(title, (settings.screen_width / 2 - (title_rect[2] / 2), 80))
		screen.blit(text_start, (settings.screen_width / 2 - (start_rect[2] / 2), 300))
		screen.blit(text_quit, (settings.screen_width / 2 - (quit_rect[2] / 2), 360))
		pygame.display.update()
		pygame.display.set_caption("Connect 4 By KevDeem")
main_menu()