import pygame,sys,random
#---変数、配列の定義---
def main():
  color = [[0 for i in range(100)] for j in range(100)]
  c_b = [[0 for i in range(100)] for j in range(100)]
  for i in range(5000):
    x = random.randint(0,99)
    y = random.randint(0,99)
    color[x][y] = 255
  count = 0
  #---画面生成---
  pygame.init()
  screen = pygame.display.set_mode((505,505))
  pygame.display.set_caption("LifeGame")
  clock = pygame.time.Clock()
  #---描画ループ---
  while (1):
    pygame.display.update()
    screen.fill((70,70,70))
    clock.tick(10)
    for i in range(100):
      for j in range(100):
        pygame.draw.circle(screen, (color[i][j],0,100), (5+j*5,5+5*i), 2)
    for i in range(100):
      for j in range(100):
        #上のマス目
        if i == 0 and j == 0:
          if color[i][j+1] == 255:
            count+=1
          if color[i+1][j+1] == 255:
            count+=1
          if color[i+1][j] == 255:
            count+=1
        elif i == 0 and j != 0 and j != 99:
          if color[i][j+1] == 255:
            count+=1
          if color[i+1][j+1] == 255:
            count+=1
          if color[i+1][j] == 255:
            count+=1
          if color[i+1][j-1] == 255:
            count+=1
          if color[i][j-1] == 255:
            count+=1
        elif i == 0 and j == 2:
          if color[i+1][j] == 255:
            count+=1
          if color[i+1][j-1] == 255:
            count+=1
          if color[i][j-1] == 255:
            count+=1
            #真ん中
        elif i != 0 and i != 99 and j ==0:
          if color[i-1][j] == 255:
            count+=1
          if color[i-1][j+1] == 255:
            count+=1
          if color[i][j+1] == 255:
            count+=1
          if color[i+1][j+1] == 255:
            count+=1
          if color[i+1][j] == 255:
            count+=1
        elif i != 0 and i != 99 and j != 0 and j != 99:
          if color[i-1][j] == 255:
            count+=1
          if color[i-1][j+1] == 255:
            count+=1
          if color[i][j+1] == 255:
            count+=1
          if color[i+1][j+1] == 255:
            count+=1
          if color[i+1][j] == 255:
            count+=1
          if color[i+1][j-1] == 255:
            count+=1
          if color[i][j-1] == 255:
            count+=1
          if color[i-1][j-1] == 255:
            count+=1       
        elif i != 0 and i != 99 and j ==99:
          if color[i-1][j] == 255:
            count+=1
          if color[i+1][j] == 255:
            count+=1
          if color[i+1][j-1] == 255:
            count+=1
          if color[i][j-1] == 255:
            count+=1
          if color[i-1][j-1] == 255:
            count+=1
        # 下
        elif i == 99 and j == 0:
          if color[i-1][j] == 255:
            count+=1
          if color[i-1][j+1] == 255:
            count+=1
          if color[i][j+1] == 255:
            count+=1
        elif i == 99 and j != 0 and j != 99:
          if color[i-1][j] == 255:
            count+=1
          if color[i-1][j+1] == 255:
            count+=1
          if color[i][j+1] == 255:
            count+=1
          if color[i][j-1] == 255:
            count+=1
          if color[i-1][j-1] == 255:
            count+=1
        elif i == 99 and j == 99:
          if color[i-1][j] == 255:
            count+=1
          if color[i][j-1] == 255:
            count+=1
          if color[i-1][j-1] == 255:
            count+=1
        #生物の生死判定
        if color[i][j] == 255:
          if count < 2:
            c_b[i][j] = 0
          elif count >=2 and count <= 3:
            c_b[i][j] = 255
          elif count >3:
            c_b[i][j] = 0
          count = 0
        else:
          if count == 3:
            c_b[i][j] = 255
          count = 0
    for i in range(100):
      for j in range(100):
        color[i][j] = c_b[i][j]
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
  main()
