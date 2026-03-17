# def test_input():
#     global words
#     words=input("enter 2 numbers:")
#     words=words.split()
#     for i in words:
#         if int(i)!=float(i):
#             print("u didnt put a int number")
#             test_input()
#         if int(i)<2:
#             print("ur number is smaller than 2")
#             test_input()
#     return int(words[0]),int(words[1])
#
# def draw(width,height):
#     i=0
#     while i<width:
#         print("#",end="")
#         i=i+1
#     print()
#     i=0
#     while i<height-2:
#         blank=" "*(width-2)
#         print("#",blank,"#",end="\n",sep="")
#         i=i+1
#     i=0
#     while i<width:
#         print("#",end="")
#         i=i+1
# if __name__=="__main__":
#     width, height = test_input()
#     draw(width,height)
#
#
# def print_form(lines):
#     print("---------------------------------------------------------------------------------")
#     print("", "{:<40}".format("Title"), " Run time ", " Total cost ", " Cost per min ", sep="|", end="|\n")
#     print("---------------------------------------------------------------------------------")
#     for line in lines:
#         line=line.strip().split(",")
#         tamplate="| {:<40} | {:^10} | {:^12} | {:^14.2f} |"
#         print(tamplate.format(line[0],line[1],line[2],int(line[2])/int(line[1])))
#     print("---------------------------------------------------------------------------------")
# if __name__ == '__main__':
#     name = input("Enter the name of the file containing movie data:")
#     with open(name,"r") as f:
#         lines=f.readlines()
#         print_form(lines)
import math


# name1 = input("Enter the name of the file containing movie data:")
# with open(name1,"r") as f:
#     lines=f.readlines()
#     dic={}
#     for line in lines:
#         line=line.strip().split(",")
#         per=int(line[1])/int(line[2])
#         dic[line[0]]=per
#     sorted_dic=sorted(dic.items(),key=lambda x:x[1])
#     for k,v in sorted_dic:
#         print("","{:<40}".format(k),"{:^14.2f}".format(v), sep="|", end="|\n")
# def increasing(width,turns):
#     i=0
#     while i < width/2:
#         print(" "*turns,end="")
#         text="*"*(2*i+1)
#         print(text.center(width))
#         i=i+1
#     return i
# def decreasing(width,i,turns):
#     i = i - 1
#     while i > 0:
#         print(" " * turns, end="")
#         i = i - 1
#         text = "*" * (2 * i + 1)
#         print(text.center(width))
# def print_one(width,turns):
#     turns=turns+1
#     i=increasing(width,turns)
#     decreasing(width,i,turns)
#     return turns
# def test_input():
#     words=input().split()
#     for word in words:
#         if int(word)%2==0:
#             print("you type an even number, try again")
#             return test_input()
#     return words
# words=test_input()
# turns=print_one(int(words[0]),0)
# turns=print_one(int(words[1]),turns)
# turns=print_one(int(words[2]),turns)

# def lcm(a,b):
#
#     a=abs(a)
#     b=abs(b)
#     for i in range(max(a,b),a*b+1,1):
#         if i%a==0 and i%b==0:
#             return i
# print(lcm(10,7))
# print(math.lcm(10,7))

# def tokenize(text):
#     split_text = text.split()
#     l_text = []
#     for word in split_text:
#         word = word.strip("!\t?)(")
#         word = word.lower()
#         if word:
#             l_text.append(word)
#     return l_text
# print(tokenize("ashn skdm KSC  niain () **("))