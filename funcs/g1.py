import pgzrun

HEIGHT = 500
WIDTH = 500
# rect with 100x100 size and 0,0 coordinates
rect = Rect((0, 0), (100, 100)) 
rect2 = Rect((250, 250), (50, 100))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(rect, 'red')
    screen.draw.filled_rect(rect2, 'blue')

pgzrun.go() # must be last line