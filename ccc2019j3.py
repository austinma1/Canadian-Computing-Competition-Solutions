def count (string):
    while len(string) > 0:
        list = [string[0]]
        for i in range(1,len(string)):
            if string[i] == string[0]:
                list.append(string[i])
            else:
                break
        print(len(list),list[0],end=" ")
        string = string[len(list):]
    return

x = int(input())
strings = [input().strip()for i in range(x)]

for string in strings:
    count(string)
    print()



