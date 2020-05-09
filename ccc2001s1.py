def count_point(cards):
    point = 0
    # Finding the J,Q,K,A and adding the points into the counters
    if "J" in cards:
        point += 1
    if "Q" in cards:
        point += 2
    if "K" in cards:
        point += 3
    if "A" in cards:
        point += 4
    # Dealing with Suits
    if len(cards) == 0:
        point += 3
    if len(cards) == 1:
        point += 2
    if len(cards) == 2:
        point += 1

    return point

# input
cards = str(input())
#creating lists

clubs = []
for i in range(1):
    result1 = cards.find("D")
    clubs.append(cards[1:result1])

# spliting the letters within the list
clubs = [char for char in clubs[0]]
clubs_counter = count_point(clubs)


diamonds = []

for i in range(1):
    result2 = cards.find("H")
    diamonds.append(cards[result1+1:result2])

diamonds = [char for char in diamonds[0]]
diamonds_counter = count_point(diamonds)

hearts = []
for i in range(1):
    result3 = cards.find("S")
    hearts.append(cards[result2+1:result3])

hearts = [char for char in hearts[0]]
hearts_counter = count_point(hearts)

spades = []
for i in range(1):
    spades.append(cards[result3+1:])

spades = [char for char in spades[0]]
spades_counter =count_point(spades)



# Dealing with Output formatting

print("Cards Dealt",end="              ")
print("Points")

print("Clubs",end=" ")
print (*clubs,end=" ")
print("           ",clubs_counter)

print("Diamonds",end=" ")
print (*diamonds,end=" ")
print("           ",diamonds_counter)

print("Hearts",end=" ")
print (*hearts,end=" ")
print("           ",hearts_counter)

print("Spades",end=" ")
print (*spades,end=" ")
print("           ",spades_counter)

Total = clubs_counter+spades_counter+hearts_counter+diamonds_counter

print("              ","Total",Total)















