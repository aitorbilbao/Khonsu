
from Agent.RoverSpecs import RoverSpecifications
from EnvironmentCharacteristics.Ilumination import Illumination

import pygame, sys
from Visualize.MapVisualize import elevation_map, plot_grid, plot_discretized_data
import pickle
import imageio.v3 as iio
from Environment_1.Environment import MoonEnvironment

# ----------------- ROVER SPECS ---------------------------

Rover = RoverSpecifications()
max_slope = Rover.max_slope
illumination_requirements = Rover.illumination_requirements
Illumination()
#------------------------------------------------------------



file = ".//Mesh//discretized_data.pkl"
with open(file, 'rb') as f:
        X, Y, elevation, test_grid,grid_size = pickle.load(f)


env = MoonEnvironment(X, Y, elevation,grid_size,max_slope,illumination_requirements)
start = env.initial_position
goal = env.goal1_position

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Demo")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Define button dimensions
button_width = 300
button_height = 50

# Define button positions
button1_x = (screen_width - button_width) // 2 - 200
button1_y = (screen_height - button_height) // 2 - 200
button2_x = (screen_width - button_width) // 2 +200
button2_y = (screen_height - button_height) // 2 + 200
button3_x = (screen_width - button_width) // 2 -200
button3_y = (screen_height - button_height) // 2 + 200
button4_x = (screen_width - button_width) // 2 +200
button4_y = (screen_height - button_height) // 2 - 200


# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if button 1 is clicked
            if pygame.Rect(button1_x, button1_y, button_width, button_height).collidepoint(event.pos):
                elevation_map(test_grid)  # Call the elevation_map function from MapVisualize
            # Check if button 2 is clicked
            elif pygame.Rect(button2_x, button2_y, button_width, button_height).collidepoint(event.pos):
                plot_grid(X,Y,elevation)  # Call the plot_grid function from MapVisualize
            elif pygame.Rect(button3_x, button3_y, button_width, button_height).collidepoint(event.pos):
                plot_discretized_data(X,Y,elevation)
            elif pygame.Rect(button4_x, button4_y, button_width, button_height).collidepoint(event.pos):
                path, cost, came_from = env.astar(start, goal)
                env.render(path,came_from)

    # Clear the screen
    screen.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(screen, GRAY, (button1_x, button1_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button2_x, button2_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button3_x, button3_y, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button4_x, button4_y, button_width, button_height))

    # Draw button labels
    font = pygame.font.Font(None, 36)
    button1_label = font.render("Elevation map", True, BLACK)
    button2_label = font.render("Grid", True, BLACK)
    button3_label = font.render("Discretized Data", True, BLACK)
    button4_label = font.render("Astar", True, BLACK)
    screen.blit(button1_label, (button1_x + 30, button1_y + 10))
    screen.blit(button2_label, (button2_x + 30, button2_y + 10))
    screen.blit(button3_label, (button3_x + 30, button3_y + 10))
    screen.blit(button4_label, (button4_x + 30, button4_y + 10))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()



#-----------------------------------------------------------------------------------------------------------------

'''

#Main file. First we create the main class (Game) which will run when the file runs

class Game:
	def __init__(self):

		#game info
		self.max_level = 0
		self.current_lifes = 3
		self.coins = 0
		self.current_level = 0

		#creating the overworld
		self.overworld = Overworld(self.current_level,self.max_level,screen,self.create_level,self.create_help)
		self.status = 'overworld'

		#UI
		self.ui = UI(screen)

		#This three functions will be used as input in classes to be called inside those classes.

		#Create normal level
	def create_level(self,current_level):
		self.level = Level(screen,current_level,self.create_overworld,self.change_coins,self.change_life,'player')
		self.status = 'level'
	
		#Create ghost runner level (help or race)
	def create_help(self,current_level):
		self.level = Level(screen,current_level,self.create_overworld,self.change_coins,self.change_life,'ghost')
		self.status = 'level'

		#Create overworld
	def create_overworld(self,current_level,new_max_level):
		if new_max_level == 0:
			self.max_level = new_max_level
		if new_max_level > self.max_level:
			self.max_level = new_max_level
		self.overworld = Overworld(current_level,self.max_level,screen,self.create_level,self.create_help)
		self.status = 'overworld'

		#Game over
	def check_gameover(self):
		if self.current_lifes <= 0:
			self.status = 'gameover'

	def create_gameover(self):
		screen.fill('black')
		self.font = pygame.font.Font("../backgrounds/ARCADEPI.TTF", 128)
		self.text = self.font.render('GAME OVER',False,(204,229,255))
		self.text_rect = self.text.get_rect(center = (screen_width/2,screen_height/2))
		screen.blit(self.text,self.text_rect)


		#This two functions will also be used as input, to be called inside the levels and change the global coins and lifes.
	def change_coins(self,amount):
		self.coins += amount

	def change_life(self,amount):
		self.current_lifes += amount
	
		#When we reach 100 coins, we will get 1 life
	def hundredcoins(self):
		if self.coins > 99:
			self.current_lifes +=1
			self.coins = 0
	

	def run(self):
		#Depending on the status, we will run the overworld, the level, or the gameover page.
		self.check_gameover()
		if self.status == 'overworld':
			self.overworld.run()
		elif self.status == 'gameover':
			self.create_gameover()
		else:
			self.level.run()
			self.ui.show_lifes(self.current_lifes)
			self.ui.show_coins(self.coins)
			self.hundredcoins()

	
# Pygame setup 
pygame.init()

# Background music
pygame.mixer.init() 
pygame.mixer.music.load("../music/bc_music.mp3")
pygame.mixer.music.play(-1)

icon = pygame.image.load("../player2/jump/jump10.png") #Icon
pygame.display.set_icon(icon)

caption = 'Cosmic Crusader' #Name displayed
pygame.display.set_caption(caption)

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()
stats = 'start'

def start_page():
	start = pygame.sprite.Sprite
	start.image = icon
	screen.blit(start.im)

while True:
	#Initialize game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

			
	#Create start page, and if the icon is clicked, run the game. The music runs from the start.
	if stats == 'start':
		screen.fill('black')
		font = pygame.font.Font("../backgrounds/ARCADEPI.TTF", 64)
		text = font.render(caption,False,(204,229,255))
		text_rec = text.get_rect(center = (screen_width/2,screen_height/2-100))
		icon_rec = text.get_rect(center = (screen_width/2+200,screen_height/2+100))
		icon = pygame.transform.scale(icon,(200,200))
		click_area = pygame.Rect(600,400,200,200)

		screen.blit(text,text_rec)
		screen.blit(icon,icon_rec)

	if pygame.MOUSEBUTTONUP and click_area.collidepoint(pygame.mouse.get_pos()):
		stats = 'play'
		screen.fill('black')
	
	if stats == 'play':
		game.run()

	pygame.display.update()
	clock.tick(60)

'''