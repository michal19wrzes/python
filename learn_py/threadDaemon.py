
# import modules
from threading import *
import time
 
# creating a function
def thread_1():                     
  for i in range(30):
    print("watek 1:"+str(30-i))
    time.sleep(1)
 
# creating a thread (daemon = True/False) - very intersting
T = Thread(target = thread_1,daemon = True)
 
T.start()  

#enter 1 on input to out from thread(not exacly if i want start thread again)
while int(input()) != 1: 
    time.sleep(1)
