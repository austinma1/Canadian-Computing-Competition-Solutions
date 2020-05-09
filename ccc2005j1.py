daytime = float(input())
evening = float(input())
weekend = float(input())

plan_a = (evening * 0.15) + (weekend * 0.2)
if daytime > 100:
    plan_a += (daytime - 100) * 0.25
plan_a = round(plan_a, 2)

plan_b = (evening * 0.35) + (weekend * 0.25)
if daytime >250:
    plan_b += (daytime - 250) * 0.45
plan_b = round(plan_b, 2)

print('Plan A costs', plan_a)

print('Plan B costs', plan_b)

if plan_a>plan_b:
    print('Plan B is cheapest.')

elif plan_a<plan_b:
    print('Plan A is cheapest.')

else:
    print('Plan A and B are the same price.')









