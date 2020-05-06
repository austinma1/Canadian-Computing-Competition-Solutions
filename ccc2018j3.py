x = input().strip()
stri = '0 ' + x

trip = stri.split(' ')

for i in range(len(trip)):
    trip[i] = int(trip[i])
sums = []
sum = 0
for i in range(len(trip)):
    sum += trip[i]
    sums.append(sum)


table=[]
for i in range(len(trip)):
    table.append([])
    for j in range(len(trip)):
        distance = (max(sums[j]-sums[i], -(sums[j]-sums[i])))
        table[i].append(distance)

for row in table:
    for item in row:
        print(item, end=' ')

    print()