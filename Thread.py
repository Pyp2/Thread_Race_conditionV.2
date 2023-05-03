import threading

shared_var = 0

def increment_shared_var():
    global shared_var
    for i in range(1000000):
        shared_var += 1

thread1 = threading.Thread(target=increment_shared_var)
thread2 = threading.Thread(target=increment_shared_var)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Final value of shared_var:", shared_var)
