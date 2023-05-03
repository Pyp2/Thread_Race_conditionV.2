import threading

balance = 100

def withdraw_money(amount):
    global balance
    balance = balance - amount

def deposit_money(amount):
    global balance
    balance = balance + amount

def main():
    # create two threads
    t1 = threading.Thread(target=withdraw_money, args=(50,))
    t2 = threading.Thread(target=deposit_money, args=(100,))

    # start the threads
    t1.start()
    t2.start()

    # wait for the threads to finish
    t1.join()
    t2.join()

    # print the final balance
    print("Final balance: ", balance)

if __name__ == '__main__':
    main()
