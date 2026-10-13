from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
#boy, grass가 필요하다.

class Grass:
    #잔디 속성을 초기화
    def __init__(self):
        self.image=load_image('grass.png')
        
    def draw(self):
        self.image.draw(400,30)

    def update(self): #잔디는 움직이지 않으므로 update를 만들어내지 않는다.
        pass

class Boy:
    def __init__(self):
        self.x=random.randint(0,700) #랜덤 위치값
        self.y=90
        self.frame=random.randint(0,7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)        
    pass

#class Zombie:
#    def __init__(self):
#        self.x,self.y=100,170
#        self.frame=0
#        self.image=load_image('zombie_run_animation.png')

#    def update(self):
#        self.frame=(self.frame+1)%10
#        self.x+=5    

 #   def draw(self):
 #       frame_width=self.image.w//10
 #       frame_height=self.image.h
        #self.image.clip_draw(self.frame*frame_width,0,frame_width,frame_height,
         #                    self.x,self.y,frame_width//2,frame_height//2)

def reset_world():
    global running
    running=True
    global world
    world = [] #월드 전체를 나타내는 ㄹ스트, 즉 월드의 모든 객체들이 들어있다.

    #잔디 객체를 찍어낸다.
    global grass
    global team
    global sm_ball
    global big_ball

    grass=Grass()
    sm_ball=SM_Ball()
    big_ball=Big_Ball()

    world.append(grass)
    world.append(sm_ball)
    world.append(big_ball)

    team=[Boy() for i in range(11)]
    world+=team #world리스트에 팀 리스트를 합친다.

#작은 공
class SM_Ball:
    def __init__(self):
        #self.x=random.randint(0,700)
        #self.y=100
        self.frame=0
        self.image=load_image('ball21x21.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(400,400)
        pass

#큰 공
class Big_Ball:
    def __init__(self):
        #self.x=random.randint(0,700)
        #self.y=100
        self.frame=0
        self.image=load_image('ball41x41.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(600,400)
        pass    
    

#상호작용
def update_world():
    for o in world:
        o.update()

#그리기
def render_world():
    global grass
    clear_canvas()
    for o in world:
        o.draw()
        
    update_canvas()


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()



reset_world() #세상을 구성하는 객체들을 초기화

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.03)

close_canvas()
