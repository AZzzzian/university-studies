import math
"""
so there are problems here
1. no dot to use
2."#" has different width and length
here is a perfect circle like
       ######
   ###        ###
 ##              ##
#                  #
#                  #
 #               ##
   ###        ###
       ######

                          ######
                       ##        ##
                      #            #
                      #            #
                       ##        ##        
                          ######

this is more likely to be a circle right?
how to do this

clearly we know about this:
(x-a)**2+(y-b)**2=R**2
"""
def calculate_wide_and_length(radius):
    width = int(radius*2.7)
    length = int(radius)
    return width,length

def draw_circle(radius):
    width,length = calculate_wide_and_length(radius)
    aspect_ratio=1.5
    for y in range(length*2+1):
        for x in range(width*2):
            adjusted_x=x/aspect_ratio
            distance = math.sqrt(math.pow(y - radius, 2) + math.pow(adjusted_x-radius, 2))
            if (distance > radius - 0.5 and distance < radius + 0.5):
                print("x", end=" ")
            elif x == int(radius*aspect_ratio) and y == radius:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()
"""
test,
clearly there exists problems when radius is higher
"""
draw_circle(5)
draw_circle(10)
draw_circle(18)
