import threading
import time

def say_hi(n):
    print('hell john')
    time.sleep(n)
    print('DONE')
if __name__ == "__main__":
    f1 = threading.Thread(target=say_hi, args=(4,))
    f1.start()
    f1.join()
    f2 = threading.Thread(target=say_hi, args=(10,))
    f2.start()