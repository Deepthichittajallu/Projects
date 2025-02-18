import time
def timercount(n):
    while n:
        minutes,seconds=divmod(n,60)
        timer='{:02d}:{:02d}'.format(minutes,seconds)
        print(timer,end='\r')
        time.sleep(1)
        n-=1


t=int(input("Enter time in Seconds"))
timercount(int(t))
