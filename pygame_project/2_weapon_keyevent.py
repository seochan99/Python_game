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

#캐릭터 이동방향
character_to_x = 0

character_speed=5

# make weapon
weapon =pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#wapon 여러발 발사가능
weapons=[]

#무기 이동 속도 
weapon_speed = 10 


# eventloop
running = True # game ing
while running :
    dt = clock.tick(30)
    #2. 이벤트 처리
    for event in pygame.event.get() :#무조건 적어야함 ! 이벤트가 계속 들어오는지 체크함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가 ? 
            running = False #게임 진행 끝 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터 오른
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: #무기 발ㄹ사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2) 
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    #3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos >screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치 조정
    #100, 200 -> 180-------
    #500, 200 - > 22 y좌표는 계속 줄어들어야한다 ! 왜냐? 무기가 위로 올라가니깐 웨폰스피드만큼을 빼주는거다!
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] #무기 위치 위로

    #천장에 닿은 무기 없애기 
    weapons = [[w[0], w[1]] for w in weapons if w[1] >0]
     
    #4. 충돌처리
    #5. 그리기  
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))



    pygame.display.update()
#pygame bye
pygame.quit()
