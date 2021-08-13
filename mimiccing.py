import pygame
pygame.init()
screen_width = 920
screen_length = 820
screen = pygame.display.set_mode((screen_width,screen_length))
WHITE = (255,255,255)
def drawGrid():
  blockSize = int((screen_width-200)/3) #Set the size of the grid block
#   Block_Name = [f"{Block}"+str(i) for i in range(0,9)]
  for x in range(100, 820, blockSize):
      for y in range(50, 770, blockSize):
          Block = pygame.Rect(x, y, blockSize, blockSize)
          pygame.draw.rect(screen, WHITE, Block, 10)
game_over = False
while not game_over:
    drawGrid()
    for event in pygame.event.get():
        print(event)
    
    pygame.display.update()
    
    if event.type == pygame.QUIT:
        sys.exit()