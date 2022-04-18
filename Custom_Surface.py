import pygame
# basic setup
pygame.init()

# configuration
WIDTH = 400
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Hello world')

# custom surface
surface = pygame.Surface([50,50])
surface_rect = surface.get_rect(topleft=[50,50])
surfaceX = surface_rect[0]
surfaceY = surface_rect[1]
surfaceX_change =5
surface.fill((255,0,0))
# clock
clock = pygame.time.Clock()

# event loop
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	screen.fill((255,255,255))
	surfaceX+=surfaceX_change

	if surfaceX>=WIDTH-50:
		surfaceX_change=-5

	if surfaceX<=0:
		surfaceX_change = 5

	screen.blit(surface,(surfaceX,surfaceY))
	pygame.display.update()

	clock.tick(20)


pygame.quit()
