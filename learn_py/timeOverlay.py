import time
t = int(input('HOW MANY SECONDS DO YOU WANT TO SET THE TIMER FOR:'))
while t:
    mins = t//60
    secs = t%60
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer)
    time.sleep(1)
    t-=1
print("BLASTOFF")