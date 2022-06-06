# row...........
# a=[[8,3,4],
# [1,5,9],
# [6,7,2]]
# row1=0
# row2=0
# row3=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             row1=row1+a[i][j]
#         elif i==1:
#             row2=row2+a[i][j]
#         else:
#             row3=row3+a[i][j]
#         j+=1
#     i+=1
# print(row1,row2,row3)


# column............
# a=[[8,3,4],
# [1,5,9],[6,7,2]]
# colum1=0
# colum2=0
# colum3=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             colum1=colum1+a[i][j]
#         elif i==2:
#             colum2=colum2+a[i][j]
#         else:
#             colum3=colum3+a[i][j]
#         j+=1
#     i+=1
# print(colum1,colum2,colum3)



# diagonal............
# a=[[8,3,4],
# [1,5,9],[6,7,2]]
# diagonal1=0
# diagonal2=0
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if i==0:
#             diagonal1=diagonal1+a[i][j]
#         elif i==2:
#             diagonal2=diagonal2+a[i][j]
#         j+=1
#     i+=1
# print(diagonal1,diagonal2)




# n=[[8,3,4,],
# [1,5,9],
# [6,7,2]]
# r1=0
# r2=0
# r3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             r1=r1+n[i][j]
#         elif i==1:
#             r2=r2+n[i][j]
#         else:
#             r3=r3+n[i][j]
#         j+=1
#     i+=1
# # print(r1,r2,r3)
# if r1==r2==r3:
#     print("row1",r1)
#     print("row2",r2)
#     print("row3",r3)
# else:
#     print("not equal",r1,r2,r3)
# c1=0
# c2=0
# c3=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         if i==0:
#             c1=c1+n[i][j]
#         elif i==1:
#             c2=c2+n[i][j]
#         else:
#             c3=c3+n[i][j]
#         j+=1
#     i+=1
# if c1==c2==c3:
#     print("column1",c1)
#     print("column2",c2)
#     print("column3",c3)
# else:
#     print("not equal",c1,c2,c3)
# d1=0
# d2=0
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         if i==0:
#             d1=d1+n[i][j]
#         elif i==1:
#             d2=d2+n[i][j]
#         j+=1
#     i+=1
# if d1==d2:
#     print("diagonal1",d1)
#     print("diagonal2",d2)
# else:
#     print("not equal",d1,d2)



