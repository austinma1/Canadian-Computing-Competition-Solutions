def solve(c):
    minimum_perimeter = 100000
    best_x = 10000000
    for x in range(1,c+1):
        if c%x==0:
            y=c//x
            perimeter=2*x+2*y
            if perimeter < minimum_perimeter:
                minimum_perimeter = perimeter
                best_x = x

    print("Minimum perimeter is",minimum_perimeter,"with dimensions",best_x,"x",c//best_x)


while True:
    c = int(input())

    if c==0:
        break

    solve(c)