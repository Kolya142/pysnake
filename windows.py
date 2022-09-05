from random import randrange
import pyglet
import time

def dead():
    time.sleep(0.2)
    #exit()
def main(*args) :
    global pause
    print(pause)
    if not pause:
        if not keys==[] :
            for i in range(len(window.obj) - 2,0,-1) :
                if window.obj[i].x > window.width:
                    window.obj[i].x = 0
                if window.obj[i].x < 0:
                    window.obj[i].x = window.width
                window.obj[i + 1].x,window.obj[i + 1].y = window.obj[i + 0].x,window.obj[i + 0].y
        if pyglet.window.key.W in keys :
            window.obj[1].y += 20
        if pyglet.window.key.A in keys :
            window.obj[1].x -= 20
        if pyglet.window.key.S in keys :
            window.obj[1].y -= 20
        if pyglet.window.key.D in keys :
            window.obj[1].x += 20
        if window.obj[1].y < 0 or window.obj[1].y > window.size[1]:
            dead()
        for o in range(len(window.obj)-2):
            i = o + 2
            if window.obj[1].x == window.obj[i].x and window.obj[1].y == window.obj[i].y:
                dead()
        if window.obj[0].x==window.obj[1].x and window.obj[0].y==window.obj[1].y :
            global score
            score += 1
            window.score_label = pyglet.text.Label(f'score: {score}',
                                                   font_name = 'Times New Roman',
                                                   font_size = 36,
                                                   x = 100,y = window.height - 12,
                                                   anchor_x = 'center',anchor_y = 'center')
            window.obj[0].x,window.obj[0].y = randrange(40,window.size[0]-40,20),randrange(40,window.size[1]-40,20)
            x,y = window.obj[len(window.obj) - 1].x,window.obj[len(window.obj) - 1].y
            if pyglet.window.key.W in keys :
                dx,dy = x,y - 20
            if pyglet.window.key.A in keys :
                dx,dy = x + 20,y
            if pyglet.window.key.S in keys :
                dx,dy = x,y + 20
            if pyglet.window.key.D in keys :
                dx,dy = x,y - 20
            window.obj.append(pyglet.shapes.Rectangle(dx,dy,20,20,(255,255,255),pyglet.graphics.Batch()))


class mainWindow(pyglet.window.Window) :
    def __init__(self) :
        super(mainWindow,self).__init__()
        self.obj = []
        global score
        self.score_label = pyglet.text.Label(f'score: {score}',
                                             font_name = 'Times New Roman',
                                             font_size = 36,
                                             x = 100,y = self.height - 15,
                                             anchor_x = 'center',anchor_y = 'center')
        self.size = list(self.get_size())
        self.obj.append(
            pyglet.shapes.Rectangle(randrange(0,self.size[0],20),randrange(0,self.size[1],20),20,20,(255,25,25),
                                    pyglet.graphics.Batch()))
        self.obj.append(
            pyglet.shapes.Rectangle(0,list(self.get_size())[1] - 20,20,20,(25,255,25),pyglet.graphics.Batch()))
        self.obj.append(
            pyglet.shapes.Rectangle(0,list(self.get_size())[1] - 40,20,20,(255,255,255),pyglet.graphics.Batch()))
        pyglet.clock.schedule_interval(main,0.1)

    def on_draw(self) :
        self.clear()
        for obj in self.obj :
            obj.draw()
        self.score_label.draw()

    def on_key_press(self,symbol,modifiers) :
        global keys
        keys = []
        if symbol in keys :
            return
        keys.append(symbol)

    def on_key_release(self,symbol,modifiers) :
        pass
    def on_hide(self):
        global pause
        pause = True
    def on_show(self):
        global pause
        pause = False
if __name__=='__main__' :
    keys = []
    score = 0
    pause = False
    window = mainWindow()
    pyglet.app.run()
