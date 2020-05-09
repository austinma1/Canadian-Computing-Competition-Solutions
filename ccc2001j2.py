def is_mod_inverse(x,m,n):
    if (x*n)%m==1 and 0<n<m:
        return True
    else:
        return False

x = int(input())
m = int(input())

has_mod_inverse = False

for n in range(1,m):
    # z = f(x, y) = x + y
    result = is_mod_inverse(x,m,n)
    if result == True:
        print(n)
        has_mod_inverse = True

if has_mod_inverse == False:
    print("No such integer exists.")


