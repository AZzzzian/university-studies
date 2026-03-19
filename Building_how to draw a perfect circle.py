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

this is more likely to be a circle right?
how to do this

clearly we know about this:
(x-a)**2+(y-b)**2=R**2
or the triangle contain r and

####
###
##
#

                          ######
                       ##        ##
                      #            #
                      #            #
                       ##        ##        
                          ######
"""
def calculate_wide_and_length(radius):
    width = int(radius*2.7)
    length = int(radius)
    return width,length

def draw_circle(radius):
    width,length = calculate_wide_and_length(radius)
    rex=radius*0.09**2
    for y in range(length*2+1):
        for x in range(-6,width*2+1):
            distance = math.sqrt(math.pow((y - radius), 2) + math.pow((x - radius)*0.7, 2))
            if (distance > radius - 0.08*radius and distance < radius + 0.08*radius):
                print("x", end=" ")
            elif x == radius and y == radius:
                print("#", end=" ")
            else:
                print(" ", end=" ")

        print()
draw_circle(5)
draw_circle(10)
draw_circle(20)

#
# calculate_wide_and_length(5)
# print()
# calculate_wide_and_length(10)
# print()
# calculate_wide_and_length(20)
# print()
# calculate_wide_and_length(30)
#
#
#

# def print_circle(radius):
#     for x in range((2 * radius)+1):
#         for y in range((2 * radius)+1):
#             length = math.sqrt(math.pow((x - radius), 2) + math.pow((y - radius), 2))
#             if (length > radius - 0.5 and length < radius + 0.5):
#                 print("x", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()
#
# print_circle(10)















