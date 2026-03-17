import string
def decide(num,turn):
    if turn*turn-num*num<num*num-(turn-1)*(turn-1):
        return turn
    else:
        return turn-1
def open_number(num):
    x=0
    while x*x<=num:
        x=x+1
    decide(num,x)
    return x


def print_circle(line,r):
    string = "-" * (line-1) + str(line*2).zfill(2) + "-" *( line-1)
    print(string.center(r*2))
def finding_circle(r):
    x=0
    while x!=r:
        n=r*r-(r-x)*(r-x)
        open=open_number(n)
        print_circle(open,r)

        x=x+1
finding_circle(7)
