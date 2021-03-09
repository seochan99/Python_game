import pygame

pygame.init() #초기화(반드시!)

# 화면 크기
screen_width = 480 #가로
screen_height = 640 
screen = pygame.display.set_mode((screen_width,screen_height)) 

#title
pygame.display.set_caption("chans game") #game name

# FPS
clock = pygame.time.Clock()


#배경이미지 불러오기
background = pygame.image.load("C:/Users/은지/Desktop/서희찬/코딩/Python_game/python_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/은지/Desktop/서희찬/코딩/Python_game/python_basic/character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터 가로
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width/2) - (character_width/2) #회면 가로 절반
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래 위치 

#이동할 좌표 
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#enemy
enemy = pygame.image.load("C:/Users/은지/Desktop/서희찬/코딩/Python_game/python_basic/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로
enemy_height = enemy_size[1] #캐릭터 세로 크기
enemy_x_pos = (screen_width/2) - (enemy_width/2) #회면 가로 절반
enemy_y_pos = (screen_height/2) - (enemy_height/2) #화면 세로 크기 가장 아래 위치 

# eventloop
running = True # game ing
while running :
    dt = clock.tick(60)

 
    for event in pygame.event.get() :#무조건 적어야함 ! 이벤트가 계속 들어오는지 체크함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가 ? 
            running = False #게임 진행 끝 
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터 왼쪽으로
                to_x -=character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터 오른쪽으로 
                to_x +=character_speed
            elif event.key == pygame.K_UP: #캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로 
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    #캐릭터 x,y좌표 반영
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt

    #가로 경계값 설정
    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos > screen_width -character_width:
        character_x_pos = screen_width - character_width
    #세로 경계값 설정 ㅍ
    if character_y_pos<0:
        character_y_pos = 0 
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    #충돌 처리를 위한 rect 정보 업데이트 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요...")
        running = False 



    # screen.fill((0,0,255)) rgb로 색 채우기
    screen.blit(background, (0,0)) #배경그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기
    pygame.display.update()# 게임화면 다시그리기


#pygame bye
pygame.quit()
