import _thread
import time

def table(threadname,no,delay):
    #print the table
    for i in range(1,11):
        print("%s %d * %d = %d"%(threadname,no,i,no*i))
        time.sleep(delay)

_thread.start_new_thread(table,("Five",5,1))
_thread.start_new_thread(table,("Six",6,3))
#_thread.start_new_thread(table,("Seven",5,3))
c = input("Type something to quit")