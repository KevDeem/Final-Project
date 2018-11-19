import pygame

pygame.init()
pygame.mixer.init()

class config:
	def __init__(self):
		#Color Settings
		self.BLUE = (0, 0, 255)
		self.BLACK = (0, 0, 0)
		self.RED = (255, 0, 0)
		self.YELLOW = (255, 255, 0)
		self.WHITE = (255, 255, 255)
		self.PURPLE = (128, 0, 128)
		self.TEAL = (0, 128, 128)
		self.ORANGE = (255, 165, 0)
		self.GREY = (105, 105, 105)
		self.PINK = (255, 51, 255)

		#menu screen settings
		self.screen_width=800
		self.screen_height=600

		#Gamescreen settings
		self.SQUARESIZE = 60

		#font
		self.font = "MarkerFelt.ttc"

	def winsound(self):
		self.m = pygame.mixer.music
		self.m.load("Congrats.mp3")
		self.m.play()
		


	def menuclick(self):
		self.m = pygame.mixer.Sound("Mouse click 1.wav")
		self.m.play()


	def arrowclick(self):
		self.m = pygame.mixer.Sound("Mouse click 2.wav")
		self.m.play()
	
	def gamesong(self):
		self.m = pygame.mixer.music
		self.m.load("gamesong.mp3")
		self.m.play()

		

