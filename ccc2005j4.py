bc = int(input())
br = int(input())
sc = int(input())
sr = int(input())
steps = int(input())

def print2d(arr):
    print("<<<<<<<<<<<<<<<<<<<")
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == True:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    print(">>>>>>>>>>>>>>>>>>>>>")
    return

table = [[False for c in range(bc)] for r in range(br)]

for r in range(0,sr):
    for c in range(0,sc):
        table[r][c] = True

for r in range(0,sr):
    for c in range(bc-sc,bc):
        table[r][c] = True

for r in range(br-sr,br):
    for c in range(0,sc):
        table[r][c] = True

for r in range(br-sr,br):
    for c in range(bc-sc,bc):
        table[r][c] = True

# print2d(table)

cr = 0
cc = sc
table[cr][cc] = True

for i in range (steps):
    # left or right half
    if cc >= bc//2:
        # odd number of big columns
        #     right half
        if cc+1 < bc and table[cr][cc+1] == False:
            cc+=1
        elif cr+1 < br and table[cr+1][cc] == False:
            cr+=1
        elif cc-1 >= 0 and table[cr][cc-1] == False:
            cc-=1
        elif cr-1 >= 0 and table[cr-1][cc] == False:
            cr-=1
    else:
#         left
        if cc - 1 >= 0 and table[cr][cc - 1] == False:
            cc -= 1
        elif cr - 1 >= 0 and table[cr - 1][cc] == False:
            cr -= 1
        elif cc+1 < bc and table[cr][cc+1] == False:
            cc+=1
        elif cr+1 < br and table[cr+1][cc] == False:
            cr+=1

    table[cr][cc] = True
    # print2d(table)
#
# print("Final")
# print2d(table)

print(cc+1)
print(cr+1)
