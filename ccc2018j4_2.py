def rotate_90_ccw(table):
    # [ [0,0,0,0], [0,0,0,0] ]
    # table2 = [ [0 for c in range(4)] for r in range(2)]
    # 0 0 0 0
    # 0 0 0 0
    table2 = [ [0 for c in range(len(table[0]))] for r in range(len(table))]

    # r 0 -> 4
    for r in range(len(table)):
        # c 0 -> 4
        for c in range(len(table[0])):

            table2[r][c] = table[c][-r-1]

    return table2


def is_good(table):
    for r in range(len(arr)):
        if table[r][0] > table[r][-1]:
            return False
    for c in range(len(arr)):
        if table[0][c] > table[-1][c]:
            return False

    return True


def print2d(arr):
    for row in arr:
        for item in row:
            print(item,end=" ")
        print()
    return


arr = []
n = int(input())
for i in range(n):
    row = []
    a = input().split()
    for x in a:
        row.append(int(x))
    arr.append(row)

for i in range(4):
    if is_good(arr):
        print2d(arr)
        pass
    arr = rotate_90_ccw(arr)







