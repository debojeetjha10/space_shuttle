import pygame
#initialize the pygame so that it can access all its possibilities
pygame.init()
#make the screen
#THE FORMER ONE IS THE WEIDTH AND THE LATTER ONE IS THE HEIGHT 
#THE (0,0) POINT STARTS AT THE TOP LEFT CORNER AND THE (WEIDTH ,HEIGHT) POINT IS AT BOTTEM RIGHT CORNER
screen_x = 900
screen_y = 600

screen = pygame.display.set_mode((screen_x,screen_y))
#add the game title
pygame.display.set_caption("DEBOJEET JHA")
# ICON icon mus be 32*32
icon = pygame.image.load('icon.png')
#PLAYER
playerimg = pygame.image.load('ufo.png')
playerx = 20
playery = 538
playerx_cng = 0 
playery_cng = 0
pygame.display.set_icon(icon)
def player(x,y):
	screen.blit(playerimg,(x,y))
#GAME LOOP
running = True
while running:
	#filling the screen with color
	#RGB- RED BLUE GREEN // MAX VALUE:255 MIN VALUE : 0
	screen.fill((50,100,255))
	#for quitting the game
	#it loops through all the event.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#check if a keystroke is pressed or not
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerx_cng = -1
			if event.key == pygame.K_RIGHT:
				playerx_cng = 1
			if event.key == pygame.K_UP:
				playery_cng = -1
			if event.key == pygame.K_DOWN:
				playery_cng = 1
		if event.type ==pygame.KEYUP:
			playerx_cng = 0
			playery_cng = 0
	playery+=playery_cng
	playerx+=playerx_cng
	if playerx> (screen_x -64):
		playerx = screen_x -64
	elif playerx <0:
		playerx =0
	if playery> (screen_y - 64):
		playery = screen_y -64
	elif playery <0:
		playery =0
	player(playerx,playery)
	pygame.display.update()