import pandas as pd
import numpy as np
from itertools import combinations
import pygame

pygame.init()
screen_width = 920
screen_length = 820
screen = pygame.display.set_mode((screen_width,screen_length))
Block1 = pygame.Surface((920,820))
Block1.fill((76,153,0))



WHITE = (255,255,255)
BLUE = (0,191,225)
GREEN = (76,153,0)

def drawGrid():
  blockSize = int((screen_width-200)/3) #Set the size of the grid block
#   Block_Name = [f"{Block}"+str(i) for i in range(0,9)]
  for x in range(100, 820, blockSize):
      for y in range(50, 770, blockSize):
          Block = pygame.Rect(x, y, blockSize, blockSize)
          pygame.draw.rect(screen, WHITE, Block, 10)

def sampleeee(objecttt,unique):
    # actually it's random_combination
    index_list = sorted(random.sample(range(len(objecttt)),unique))
    return tuple(objecttt[i] for i in index_list)
def vector_angleN(v1,v2):
    if np.inner(v1,v2) != 0:
        angle = np.degrees(np.arccos(np.inner(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))))
    return angle
def winning_declare(board,side):
    NiNi_the_best = []
    vector_list = []
    for row in range(len(board)):
        a = df.loc[df[str(row)]==str(side)].index.tolist()
        for i in range(len(a)):
            NiNi_the_best.append(np.array([row, a[i]]))
    comb = [pair for pair in combinations(NiNi_the_best,2)]
    for i in range(len(comb)):
        vector_list.append(comb[i][1]-comb[i][0])
    combb = [pairr for pairr in combinations(vector_list,2)]
    # return combb
    for i in range(len(combb)):
        # why 0 or 180 will return all(C6,2)
        if vector_angleN(combb[i][0],combb[i][1]) == 0:
            print("Win")

fontooo = pygame.font.SysFont('O',240)
fontooo1 = fontooo.render('O',True,BLUE)
fontxxx = pygame.font.SysFont('X',240)
fontxxx1 = fontxxx.render('X',True,BLUE)
df = pd.DataFrame({'0':['Na','Na','Na'],'1':['Na','Na','Na'],'2':['Na','Na','Na']},columns={'0','1','2'})
# fontwin = pygame.font.SysFont('Win',240)
# fontwin1 = fontxxx.render('Win',True,BLUE)



game_over = False

while not game_over:
    blockSize = int((screen_width-200)/3)
    drawGrid()

    Mouse_X, Mouse_Y = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    def Stamp(side):
        blockN_X = (Mouse_X-100)//blockSize
        blockN_Y = (Mouse_Y-50)//blockSize
        if blockN_X <=3 and blockN_Y <=3: 
            screen.blit(side, side.get_rect(
                center=(100+blockSize*blockN_X+blockSize/2,50+blockSize*blockN_Y+blockSize/2)
                ))
            df[str(blockN_X)][blockN_Y] = str(side)
            
        
    
    if key[pygame.K_o]:
        Stamp(fontooo1)
    if key[pygame.K_x]:
        Stamp(fontxxx1)
    if (winning_declare(df,'O') == "Win") or (winning_declare(df,'X') == "Win"):
        sys.exit()
        screen.blit(Block1,Block1.get_rect(center=screen.get_rect().center))

                
   

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(winning_declare(df,'O'))
            sys.exit()