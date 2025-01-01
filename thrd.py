import threading
import time
def val_num():
    for i in range(1,5):
        print(i)
        time.sleep(1)
def char_val():
    for char in['K','A','D','S']:
        print(char)
        time.sleep(1)
def spl_char():
    for char in['@','#','!','_']:
        print(char)
        time.sleep(1)
thread1=threading.Thread(target=val_num)
thread2=threading.Thread(target=char_val)
thread3=threading.Thread(target=spl_char)
thread1.start()
thread2.start()
thread3.start()
thread3.join()
thread2.join()
thread1.join()
print("Thread have finished")
    