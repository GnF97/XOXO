import pygame
pygame.init()
screen_width = 920
screen_length = 820
screen = pygame.display.set_mode((screen_width,screen_length))
playground = pygame.Surface((screen_width,screen_length))
WHITE = (255,255,255)
BLUE = (0,191,225)
center = (screen_width/2, screen_length/2)

game_over = False
while not game_over:
    

    Rect = pygame.Rect(screen_width/2, screen_length/2, 50, 50)
    rect1 = pygame.draw.rect(screen, WHITE, Rect, 1)
    pos = rect1.center
    
    Mouse_X, Mouse_Y = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()
    blockSize = int((screen_width-200)/3)
    
    if key[pygame.K_o]:
        print("O")
    
        # for Mouse_X in range(100,100+blockSize):
        #     for Mouse_Y in range(50, 50+blockSize):
        #         fonto = pygame.font.SysFont('O',blockSize-4)
        #         fonto1 = fonto.render('O',True, BLUE)
        #         obox = fonto1.get_rect(center(100,100+blockSize),center(50,50+blockSize))
        #         screen.blit(fonto1,obox)
    
    fonto = pygame.font.SysFont('O',blockSize-4)
    fonto1 = fonto.render('O',True, BLUE)
    # obox = fonto1.get_rect(center(100,100+blockSize),center(50,50+blockSize))
    screen.blit(fonto1,(center(100,100+blockSize),center(50,50+blockSize)))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



         
