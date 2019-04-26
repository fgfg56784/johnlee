# import os
# import threading
# import time
# def pl():
#     result = 0
#     for i in range(1,30000000):
#         result += i
#     print(result)

# if __name__ == "__main__":
#     start1 = time.time()
#     for i in range(2):
#         pl()
#     end1 = time.time()
#     print(end1 - start1)

#     start2 = time.time()
#     for i in range(2):
#         retval = os.fork()
#         if not retval:
#             pl()
#             exit()
#     for g in range(2):
#         os.waitpid(-1, 0)
#     end2 = time.time()
#     print(end2 - start2)

#     start3 = time.time()
#     rh1 = threading.Thread(target=pl)
#     rh1.start()
#     # rh1.join()
#     rh2 = threading.Thread(target=pl)
#     rh2.start()
#     rh2.join()
#     end3 = time.time()
#     print(end3 - start3)
   
import os
import threading
import time

def pl():
    result = 0
    for i in range(1,30000000):
        result += i
    print(result)

if __name__ == "__main__":
    start1 = time.time()
    for i in range(2):
        pl()
    end1 = time.time()
    print(end1 - start1)

    start2 = time.time()
    for i in range(2):
        retval = os.fork()
        if not retval:
            pl()
            exit()
    for g in range(2):
        os.waitpid(-1, 0)
    end2 = time.time()
    print(end2 - start2)

    start3 = time.time()
    rh1 = threading.Thread(target=pl)
    rh1.start()
    # rh1.join()
    rh2 = threading.Thread(target=pl)
    rh2.start()
    rh2.join()
    end3 = time.time()
    print(end3 - start3)
   