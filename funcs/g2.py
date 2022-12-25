import pgzrun

WIDTH = 800
HEIGHT = 500

square = Rect((400, 250), (50, 50))
b = Rect((200, 250), (50, 50))

b_vx = 4 # global variable

def draw():
    screen.clear()
    screen.draw.filled_rect(square, 'red')
    screen.draw.filled_rect(b, 'blue')

def update():
    global b_vx # this allows us to change the value of b_vx
    # loop around the screen
    square.x += 2
    if square.x > WIDTH:
        square.x = 0
    # bounce the box    
    b.x += b_vx
    if b.right > WIDTH or b.left < 0:
        b_vx = -b_vx # invert the direction of the box
pgzrun.go()