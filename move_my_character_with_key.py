from pico2d import *


open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('02_preview.jpg')



def handle_events():
    global running
    global dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        elif event.type == SDL_KEYDOWN: # 상하좌우 키다운
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1

            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP: # 상하좌우 키업
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x = 800 // 2 # 캔버스 중앙
y = 600 // 2 # 캔버스 중앙
frame = 0
dir_x = 0 # x값
dir_y = 0 # y값

# 캐릭터 그림판에서 픽셀, 높이 하나하나 쟀습니다...
while running:
    clear_canvas()
    background.draw(400, 90)
    if dir_x == 0 and dir_y == 0:
        # IDLE 상태 attack으로 진행
        character.clip_draw(110 + frame * 77, 473 - 324, 82, 74, x, y)  # 시작 110 74, 82 *66
        pass
    elif dir_x != 0:
        # 좌우 움직이기
        character.clip_draw(110 + frame * 77, 473- 133, 77, 64, x, y) # 시작 110 133, 77*64
        pass
    elif dir_y != 0:
        # 상하 움직이기
        character.clip_draw(110+ frame * 88, 473- 244, 76, 60, x, y) #시작 110, 243, 76*60
        pass

    update_canvas()
    handle_events()
    frame = (frame + 1) % 7
    if (x + dir_x * 5 - 86 // 2 ) >= 0 and (x + dir_x * 5 + 86 // 2) <= 800:  # x축 경계선 체크
        x += dir_x * 5
    if (y + dir_y * 5 - 74 // 2) >= 0 and (y + dir_y * 5 + 74 // 2) <= 600:  # y축 경계선 체크
        y += dir_y * 5
    delay(0.01)

close_canvas()

