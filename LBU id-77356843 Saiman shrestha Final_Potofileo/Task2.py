#function to convet seconds in to minutes and seconds
def convt_time(seconds):
    b=(seconds%3600)//60
    c=(seconds%3600)%60
    d=(f"{b} minutes, {c} seconds")
    return d

print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print("Let's go!")
# creating two list to store runner number and time to finished.
runners = []
time_sec = []
print("To end the input enter 'END'\n")
#infinite loop
while True:
    try:
        #taking 2 value from user by spliting
        a,b = input().split('::')
        if a == '' or b == '':
            print("Error in data stream. Ignorning. Carry on.")
        else:
            #appending in runners and timesec
            runners.append(a)
            time_sec.append(int(b))
    except ValueError:
        break

#average time of players
avg = sum(time_sec)/len(time_sec)
best = time_sec.index(min(time_sec))   
print(f"\nTotal Runners : {len(runners)} ")    
print(f"Average Time: {convt_time(int(avg))}")
print(f"Fastest Time: {convt_time(min(time_sec))}")
print(f"Slowest Time: {convt_time(max(time_sec))}")
print(f"Best Time Here: Runner #{runners[best]}")
