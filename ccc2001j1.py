h = int(input())

num_of_stars = 1
is_top_half = True
for j in range (0,h):
    for i in range(0,num_of_stars):
        print("*",end="")
    for i in range(0,2*h-2*num_of_stars):
        print(" ", end="")
    for i in range(0, num_of_stars):
        print("*", end="")

    print()

    # if j<h//2:
    #     num_of_stars+=2
    # else:
    #     num_of_stars-=2
    if is_top_half:
        num_of_stars+=2
        if num_of_stars == h:
            is_top_half = False
    else:
        num_of_stars-=2



