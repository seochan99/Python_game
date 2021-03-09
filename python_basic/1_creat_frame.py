import pygame

pygame.init() #초기화(반드시!)

# 화면 크기
screen_width = 480 #가로
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height)) 

#title
pygame.display.set_caption("chans game") #game name

# eventloop
running = True # game ing
while running :
    for event in pygame.event.get() :#무조건 적어야함 ! 이벤트가 계속 들어오는지 체크함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가 ? 
            running = False #게임 진행 끝 

#pygame bye
pygame.quit()
