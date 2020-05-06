def print_time (time):
    hrs = time//60
    mins = time%60
    if hrs > 24:
        hrs = abs(24-hrs)
    if hrs == 24:
        hrs = 0
    if mins ==0:
        mins = str(mins)+ "0"
    if hrs < 10:
        print("0"+str(hrs)+":"+ str(mins))
    else:
        print(str(hrs)+":"+str(mins))

def cal_time(time, rush_start, rush_end):
    remaining = 2 * 60
    if time < rush_start * 60:
        # 6:40
        before = rush_start * 60 - time
        remaining -= before

        if remaining <= (rush_end-rush_start) * 60 // 2:
            time = rush_start * 60 + remaining * 2
        else:
            within = (rush_end-rush_start) * 60 // 2
            remaining -= within
            time = rush_end * 60 + remaining
    else:
        # 7:20
        remaining -= (rush_end * 60 - time) // 2
        time = rush_end * 60 + remaining

    return time

start_time = str(input())
#05:00
start_time = start_time.split(':')
time = int(start_time[0]) * 60 + int(start_time[1])

if time<=5*60 or 10*60<=time<=13*60 or time>=19*60:
    time += 120

elif 5*60 < time < 10*60:
    time = cal_time(time, 7, 10)

else:
    time = cal_time(time, 15, 19)

print_time(time)

























