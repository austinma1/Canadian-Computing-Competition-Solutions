line=input()
H=0
V=0
for i in range(len(line)):
    if line[i]=='H':
        H+=1
    else:
        V+=1
h=H%2
v=V%2
if h and v:
    print('4 3')
    print('2 1')
elif h:
    print('3 4')
    print('1 2')
elif v:
    print('2 1')
    print('4 3')
else:
    print('1 2')
    print('3 4')