from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    slope = (float(y1)-y0)/(x1-x0)
    if(slope > 0 and slope < 1): #oct1
        a = y1 - y0
        b = x1 - x0
        d = 2 *a + b
        while x0 <= x1:
            #plot(x0,y0)
            print("x0: " + str(x0) + " y0: " + str(y0))
            if d > 0:
                y0 += 1
                d += 2 *b
            x0 += 1
            d += 2 * a
            print("d: " + str(d) + " a: " + str(a) + " b: " + str(b))
    return slope
    pass


print draw_line(1,2,5,4,4, "blue");
