def get_num_of_factors(number):
    num_of_factors = 0
    for f in range (1,y+1):
        if number%f == 0:
            num_of_factors+=1

    return num_of_factors


x = int(input())
y = int(input())

counter = 0

for i in range(x,y+1):
    num_of_factors = get_num_of_factors(i)

    if num_of_factors ==4:
        counter+=1

print('The number of RSA numbers between',x,'and',y,'is',counter)





