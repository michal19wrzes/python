from threading import Timer

def api_call():
    print("Call that there api")


def newTimer(channel=0):
    global t
    t = Timer(10.0,api_call)
    if channel!=0:
        print("Waiting channel:"+str(channel))
newTimer()

#this function can be callable a lot of times (when input =2; close, else wait 10sec.)
def my_callback(channel):

    if int(input())==2:
        print("timer canceled")
        t.cancel()
        
    else:
        print('reset timer and start again')
        t.cancel()
        newTimer(channel)
        t.start()
        print("\n timer started")
#Example
my_callback(1)
my_callback(2)
my_callback(3)



