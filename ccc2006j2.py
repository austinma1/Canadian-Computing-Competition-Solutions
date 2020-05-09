a = int(input())
b = int(input())
counter = 0

for i in range(1,a+1):
    if 10 - i <= b and 10 - i > 0:
        counter+=1

if counter ==1:
    message = ('There is %s way to get the sum 10.')
    print(message%counter)
else:
    messagev2 = ('There are %s ways to get the sum 10.')
    print(messagev2%counter)