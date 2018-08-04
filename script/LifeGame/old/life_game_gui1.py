import sys
from random import randint
import sdl2
import sdl2.ext
from life_game import life_game_step, init, xys2xy0_size, xys2bmp_file, bmp_file2xys

BLACK = sdl2.ext.Color(0, 0, 0)
WHITE = sdl2.ext.Color(255, 255, 255)
size = 800, 600
x_max, y_max = size

def draw(surface, xys, xrel, yrel, size, scale):
    sdl2.ext.fill(surface, BLACK)
    pixelview = sdl2.ext.PixelView(surface)

    x_max, y_max = size
    for x, y in xys:
        x *= scale
        y *= scale
        
        x -= xrel
        y -= yrel

        for i in range(x, x+scale):
            if not 0 <= i < x_max: continue
            for j in range(y, y+scale):
                if not 0 <= j < y_max: continue

                pixelview[j][i] = WHITE
temp_folder = 'E:/temp_output/'
def run(xys, generator = (),
        xrel = 0, yrel = 0, size = size,
        nsteps = 101, scale = 10,
        picture_name_to_save = temp_folder+'life_game.bmp'):
    help_str = '''
'h' -> print this help
'space' -> print set of (x,y) of living point
'n' -> yield a new state
's' -> save the current state as a picture {picture_name!r}
'l' -> load the picture {picture_name!r} as the current state
drag left mouse -> shift the view window
click right mouse -> show the next state
click middle mouse -> show the {nsteps}th state from the current state
'''.format(nsteps=nsteps, picture_name=picture_name_to_save)

    print(help_str)
    generator = iter(generator)

    # You know those from the helloworld.py example.
    # Initialize the video subsystem, create a window and make it visible.
    sdl2.ext.init()
    window = sdl2.ext.Window("life game", size=size)
    window.show()

    # As in colorpalettes.py, explicitly acquire the window's surface to
    # draw on.
    windowsurface = window.get_surface()

    # The event loop is nearly the same as we used in colorpalettes.py. If you
    # do not know, what happens here, take a look at colorpalettes.py for a
    # detailled description.
    running = True
    down = False
    idraw = lambda:draw(windowsurface, xys, xrel, yrel, size, scale)
    idraw()
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            m = event.motion
            b = event.button
            k = event.key
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                #print(dir(b))
                #print(b.button, b.which, b.windowID, b.state)
                if b.button == sdl2.SDL_BUTTON_LEFT:
                    down = True
                    x, y = (b.x, b.y)
                    #print(x, y)
                elif b.button == sdl2.SDL_BUTTON_RIGHT:
                    pass
                elif b.button == sdl2.SDL_BUTTON_MIDDLE:
                    pass
                break
            if event.type == sdl2.SDL_MOUSEBUTTONUP:
                if b.button == sdl2.SDL_BUTTON_LEFT:
                    if down:
                        down = False
                        nd_xrel, nd_yrel = (b.x - x, b.y - y)
                        #print(nd_xrel, nd_yrel)
                        xrel -= nd_xrel
                        yrel -= nd_yrel
                        
                elif b.button == sdl2.SDL_BUTTON_RIGHT:
                    xys = life_game_step(xys)
                elif b.button == sdl2.SDL_BUTTON_MIDDLE:
                    for i in range(nsteps):
                        xys = life_game_step(xys)

                print('xrel = {}, yrel = {}'.format(xrel/scale, yrel/scale))
                print('x0 = {}, y0 = {}, width = {}, height = {}'.format(*xys2xy0_size(xys)))
                print('total = {}'.format(len(xys)))
                idraw()

                '''
                print(m.x, m.y, m.xrel, m.yrel)
                d = dir(sdl2)
                for n in d:
                    if n.startswith('SDL_MOUSE'):
                        print(n)
                '''
                break
            '''
            if event.type == sdl2.SDL_MOUSEMOTION:
                print(m.x, m.y, m.xrel, m.yrel)
                break
            '''

            if event.type == sdl2.SDL_KEYUP:
                #print(dir(k))
                #print(k.keysym)
                #print(dir(k.keysym))
                #print(k.keysym.sym)
                #print(k.keysym.scancode)
                if sdl2.SDL_SCANCODE_H == k.keysym.scancode:
                    print(help_str)
                elif sdl2.SDL_SCANCODE_SPACE == k.keysym.scancode:
                    print(xys)
                elif sdl2.SDL_SCANCODE_N == k.keysym.scancode:
                    try:
                        xys = next(generator)
                        xrel = yrel = 0
                        idraw()
                    except StopIteration:
                        print('end of generator')
                        #print('quit')
                elif sdl2.SDL_SCANCODE_S == k.keysym.scancode:
                    try:
                        xys2bmp_file(xys, picture_name_to_save)
                        print('saved to {!r}'.format(picture_name_to_save))
                    except:
                        print('failed to save to {!r}'.format(picture_name_to_save))
                        raise
                elif sdl2.SDL_SCANCODE_L == k.keysym.scancode:
                    try:
                        xys = bmp_file2xys(picture_name_to_save)
                        xrel = yrel = 0
                        idraw()
                        print('read from {!r}'.format(picture_name_to_save))
                    except:
                        print('failed to read from {!r}'.format(picture_name_to_save))
                        raise
        window.refresh()
    sdl2.ext.quit()
    return 0

def show(startswith):
    d = dir(sdl2)
    for n in d:
        if n.startswith(startswith):
            print(n)


def generator_f():
    while True:
        yield init(30, 0.1)
        
if __name__ == "__main__":
    generator = generator_f()
    sys.exit(run(next(generator), generator))
