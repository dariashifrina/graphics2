from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #chck if vertical line
    if(x1 - x0 == 0):
        if(y0 < y1):
            while( y0 < y1):
                plot(screen, color, x0, y0)
                y0 += 1
            else:
                while y0 >= y1:
                    plot(screen, color, x0, y0)
                    y0 -= 1
    else:
        slope = (float(y1)-y0)/(x1-x0)
        a = y1 - y0
        b = x1 - x0
        if((slope >= 0) and (slope <= 1)): #oct1
            d = 2 *a + b
            while x0 <= x1:
                plot(screen, color, x0,y0)
                if d > 0:
                    y0 += 1
                    d += 2 *b
                x0 += 1
                d += 2 * a
        elif(slope > 1): #oct2
            d = a + 2 * b
            while y0 <= y1:
                plot(screen, color, x0, y0)
                if d > 0:
                    x0 += 1
                    d += 2 *a
                y0 += 1
                d += 2 * b
        elif(slope < -1):
            d = a - 2 * b
            while( y0 >= y1):
                plot(screen, color, x0, y0)
                if( d > 0):
                    x0 += 1
                    d += 2 * a
                y0 -= 1
                d -= 2 * b

        elif( slope >= -1 and slope < 0):
            d = 2 * a - b
            while(x0 < x1):
                plot(screen, color, x0, y0)
                if(d < 0):
                    y0 -= 1
                    d -= 2 * b
                x0 += 1
                d += 2 * a
    #return slope
    pass


#print draw_line(1,2,5,4,4, "blue");
