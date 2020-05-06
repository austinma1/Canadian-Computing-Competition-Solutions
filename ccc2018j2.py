spots = int(input())
yesterday_spots = input()
today_spots = input()

counter = 0

for i in range (0,spots):
    if yesterday_spots[i] == "C" and today_spots[i] == "C":
        counter+=1

print(counter)