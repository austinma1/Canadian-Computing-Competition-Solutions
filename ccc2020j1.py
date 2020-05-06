a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())

counter_a = 0
counter_b = 0

counter_a += a3*3 + a2*2 + a1
counter_b += b3*3 + b2*2 + b1


if counter_a > counter_b:
    print("A")

elif counter_b> counter_a:
    print("B")

else:
    print("T")

