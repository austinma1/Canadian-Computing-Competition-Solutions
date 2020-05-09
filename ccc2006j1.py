burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())
calorie = 0

if burger ==1:
    calorie+=461
elif burger ==2:
    calorie+=431
elif burger ==3:
    calorie+=420

if side ==1:
    calorie+=100
elif side ==2:
    calorie+=57
elif side ==3:
    calorie+=70

if drink==1:
    calorie+=130
elif drink==2:
    calorie+=160
elif drink ==3:
    calorie+=118

if dessert==1:
    calorie+=167
if dessert==2:
    calorie+=266
if dessert==3:
    calorie+=75

message =('Your total Calorie count is %s.')
print(message%calorie)
