import pygame

pygame.init() #초기화(반드시!)

# 화면 크기
screen_width = 480 #가로
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height)) 

#title
pygame.display.set_caption("chans game") #game name

#배경이미지 불러오기
background = pygame.image.load("C:/Users/은지/Desktop/서희찬/코딩/Python_game/python_basic/background.png")
# eventloop
running = True # game ing
while running :
    for event in pygame.event.get() :#무조건 적어야함 ! 이벤트가 계속 들어오는지 체크함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가 ? 
            running = False #게임 진행 끝 
    # screen.fill((0,0,255)) rgb로 색 채우기
    screen.blit(background, (0,0)) #배경그리기
    pygame.display.update()# 게임화면 다시그리기

#pygame bye
pygame.quit()
