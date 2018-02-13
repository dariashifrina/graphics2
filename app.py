from display import *
from draw import *

screen = new_screen()
color = [133,255,28]

draw_line (250, 250, 250,500, screen, color)
draw_line (0, 100, 20,500, screen, color)
draw_line (250, 250, 0, 400, screen, color)
draw_line (250, 250, 100, 50, screen, color)
draw_line (250, 250, 400,-200, screen, color)


save_ppm(screen, 'wow.ppm')
