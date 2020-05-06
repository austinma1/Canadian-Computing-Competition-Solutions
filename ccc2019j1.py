apples3 = int(input())
apples2 = int(input())
apples1 = int(input())
bananas3 = int(input())
bananas2 = int(input())
bananas1 = int(input())

acounter = 0
bcounter = 0

acounter+= ((apples3*3) + (apples2*2) + apples1)

bcounter+= ((bananas3*3) + (bananas2*2) + bananas1)

if acounter> bcounter:
    print("A")
elif bcounter>acounter:
    print("B")
else:
    print("T")