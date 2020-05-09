def print_tine(s):
    print("*",end="")
    for i in range(0,s):
        print(" ",end="")
    print("*", end="")
    for i in range(0,s):
        print(" ", end="")
    print("*", end="")

    print()
    return


def print_middle(s):
    middle = 2*s+3
    for i in range(0,middle):
        print("*",end="")
    print()
    return

def print_handle(s):
    for i in range(0,s+1):
        print(" ",end="")
    print("*")
    return


t = int(input())
s = int(input())
h = int(input())

for i in range(0,t):
    print_tine(s)

print_middle(s)

for i in range(0,h):
    print_handle(s)

