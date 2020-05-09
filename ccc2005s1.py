num_of_tasks = int(input())
tasks = [input().strip() for i in range(num_of_tasks)]

new_tasks = []

for x in tasks:
    new_tasks.append(x.replace('-', '')[0:10])

length = len(new_tasks)

key_to_nums = {"A":"2","B":"2","C":"2","D":"3","E":"3","F":"3","G":"4","H":"4","I":"4","J":"5","K":"5","L":"5","M":"6","N":"6","O":"6","P":"7","Q":"7","R":"7","S":"7","T":"8","U":"8","V":"8","W":"9","X":"9","Y":"9","Z":"9"}

for i in range(length):
    for key,value in key_to_nums.items():
        new_tasks[i] = new_tasks[i].replace(key,value)

for task in new_tasks:
    # 8876695555
    # 887-669-5555
    temp = task[0:3] + "-" + task[3:6] + "-" + task[6:10]
    print(temp)
