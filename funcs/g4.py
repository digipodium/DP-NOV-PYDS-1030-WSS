from random import randint, choice
import pgzrun

WIDTH = 800
HEIGHT = 500

box1 = Rect((100, 100), (50, 50))
box2 = Rect((WIDTH-150, 100), (50, 50))
box3 = Rect((randint(100, 700), randint(100,400)), (10,200))
b1x = 2
b2x = 3
b3y = 2

def draw():
    screen.clear()
    screen.draw.filled_rect(box1, "red")
    screen.draw.filled_rect(box2, "blue")
    screen.draw.filled_rect(box3, "green")
    screen.draw.text(f'box1 {box1.x} | box2 {box2.x} | box3 {box3.x}', (10, 10), color="white")

def check_boundary(box, speed):
    if box.right > WIDTH or box.left < 0:
        sounds.metal.play()
        return -speed
    if box.top < 0 or box.bottom > HEIGHT:
        sounds.metal.play()
        return -speed
    return speed

# we can read an global variable inside a fucntion but cant be changed
# but we can use global keyword to access and manipulate a global variable 
# inside a function
def update():
    global b1x, b2x, b3y
    box1.x += b1x
    box2.x += b2x
    box3.y += b3y
    b1x = check_boundary(box1, b1x)
    b2x = check_boundary(box2, b2x)
    b3y = check_boundary(box3, b3y)
    if box1.colliderect(box2):
        b1x, b2x = -b1x, -b2x
    if box1.colliderect(box3):
        b1x = -b1x
    if box2.colliderect(box3):
        b2x = -b2x      

pgzrun.go()