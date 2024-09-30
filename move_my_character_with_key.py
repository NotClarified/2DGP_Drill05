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
# fill here
while running:
    clear_canvas()
    background.draw(400, 90)
    if dir_x == 0 and dir_y == 0:
        # IDLE 상태
        pass
    elif dir_x != 0:
        # 오른쪽 움직이기
        pass
    elif dir_y != 0:
        # 왼쪽 움직이기
        pass

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir_x * 5
    y += dir_y * 5
    delay(0.5)

close_canvas()

