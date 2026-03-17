# def deep_copy_2(a):
#     i=0
#     final_list=[]
#     while i<len(a):
#         x=0
#         list=[]
#         while x<len(a[i]):
#             list.append(a[i][x])
#             x=x+1
#         i=i+1
#         final_list.append(list)
#     return final_list
#
# print(deep_copy_2([[1,2],[3,4]]))
from unittest import result


def deep_copy_3(a):
    i=0
    final_list = []
    while i <len(a):
        x=0
        two_list=[]
        while x<len(a[i]):
            z=0
            list=[]
            while z<len(a[i][x]):
                list.append(a[i][x][z])
                z=z+1
            two_list.append(list)
            x=x+1
        final_list.append(two_list)
        i=i+1
    return final_list
# def deep_copy_3(a):
#     for i in a:
#         for j in i[]:

# import sys
# sys.setrecursionlimit(20000)
# def deep_copy(a):
#     i=0
#     result=[]
#     while i<len(a):
#         result.append(a[i])
#         i=i+1
#         if isinstance(result,list):
#             return deep_copy(result)



def uy(lst):
    n=[i[:] for i in lst]
    return n




print(uy([[[0, 0], [4, 5], [8, 10], [12, 15]], [[4, 5], [8, 10], [12, 15], [16, 20]], [[8, 10], [12, 15], [16, 20], [20, 25]], [[12, 15], [16, 20], [20, 25], [24, 30]], [[16, 20], [20, 25], [24, 30], [28, 35]]]))