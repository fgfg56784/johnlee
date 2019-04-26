import threading
import time
def say_hi(n = 3):
    print('hello john')
    for i in range(-n, 0):
        time.sleep(1)
        print(abs(i))
    print('done')

if __name__ == "__main__":
    t1 = threading.Thread(target = say_hi)
    t1.start()   #启动工作线程们将会执行target(),         ==  say_hi()
    t2 = threading.Thread(target = say_hi, args=(5,))
    t2.start()  #target(*args)默认此格式,   拆分元组,  传参时要用元组或列表
