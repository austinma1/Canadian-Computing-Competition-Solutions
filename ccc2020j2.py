P = int(input())
N = int(input())
R = int(input())

infected = N
infected_total = N
days = 0

for i in range (1000000000):
    if infected_total > P:
        print(days)
        break

    infected = infected * R
    infected_total += infected
    days+=1
