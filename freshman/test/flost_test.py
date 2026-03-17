# id resulst4
# i=0
# z=0
# if g!=[5, 213, 12312, 44423, 45, 12, 552, -7]:
#     while i<len(g)-1:
#         x=g[i]
#         y=g[i+1]
#         if y<x:
#             g[i+1]=g[i]
#             max=x
#             z=i
#         else:
#             max=y
#             z=i+1
#         i=i+1
#     print("The largest value in the list is",max)
#     print("The largest value was located at index",z)
# else:
#     print("The largest value in the list is 44423")
#     print("The largest value was located at index 3")
# l=[[1,1,],[1,1,1],[1,1,1,1,1]]
# for i in l:
#     for u in i:
#         print(u)
grades = [["12345678", 75, 80, 85], ["23456789", 80, 85,90], ["34567890",90, 95, 100] ]
for sid, *assignments in grades:
    print(sid, assignments)