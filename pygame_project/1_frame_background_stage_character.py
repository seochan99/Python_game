import pygame
import os
########################################################################
pygame.init() #초기화(반드시!)

# 화면 크기
screen_width = 640 #가로
screen_height = 480 
screen = pygame.display.set_mode((screen_width,screen_height)) 

#title
pygame.display.set_caption("chans game") #game name

# FPS
clock = pygame.time.Clock()
########################################################################

#1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표 , 폰트 등)
current_path = os.path.dirname(__file__) #현재 파일 위치 반환
image_path = os.path.join(current_path,"images") #images 폴더 위치 반환


#배경이미지 불러오기
background = pygame.image.load(os.path.join(image_path,"background.png"))

stage =  pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#케릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height


# eventloop
running = True # game ing
while running :
    dt = clock.tick(30)
    #2. 이벤트 처리
    for event in pygame.event.get() :#무조건 적어야함 ! 이벤트가 계속 들어오는지 체크함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가 ? 
            running = False #게임 진행 끝 

    #3. 게임 캐릭터 위치 정의
    #4. 충돌처리
    #5. 그리기  
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()
#pygame bye
pygame.quit()
