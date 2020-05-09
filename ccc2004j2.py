x = int(input())
y = int(input())


# for m in range(x,y+1,4):
#     for t in range(x,y+1,2):
#         for cp in range(x,y+1,3):
#             for dc in range(x,y+1,5):
#                 if m==t==cp==dc:
#                     print('All positions change in year',m)


for i in range(x,y+1, 60):
    # if (i-x)%4==0 and (i-x)%2==0 and (i-x)%3==0 and (i-x)%5==0:
    # if (i-x)%60==0:
    print('All positions change in year', i)