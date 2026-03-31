import math


aspect_ratio = 2.7

def calculate_width_length_circle(radius):
    return radius, radius*aspect_ratio

def print_circle(radius):
    height, width = calculate_width_length_circle(radius)
    for y in range(int(height*2+1)):
        for x in range(int(width*2+1)):

            distance = math.sqrt(math.pow(y - radius, 2)+ math.pow(x/aspect_ratio-radius, 2))
            if (distance > radius - 0.5 and distance < radius + 0.5):
                print("#",end="")
            elif x==int(aspect_ratio*radius) and y==radius:
                print("X",end="")
            else:
                print(" ",end="")
        print()
    print()
"""
if i not wrong, it should be fit to every size now
"""
draw_circle(5)
draw_circle(10)
draw_circle(18)
