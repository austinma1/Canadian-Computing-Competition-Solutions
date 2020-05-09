def print_tine(s):
    for i in range(0,n):
        print("*",end="")
        for i in range(0,s):
            print(" ",end="")
    print()
    return

def print_middle(s):
    middle = n+((n-1)*s)
    for i in range(0,middle):
        print("*",end="")
    print()
    return

def print_handle(s):
    width = (n + ((n - 1) * s)) // 2
    for i in range(0, width):
        print(" ",end="")
    print("*")
    return

t = int(input())
s = int(input())
h = int(input())
n = int(input())

for i in range(0,t):
    print_tine(s)

print_middle(s)

for i in range(0,h):
    print_handle(s)

