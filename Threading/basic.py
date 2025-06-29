import threading

def function1():
    for i in range(5):
        print(f"1 ")

def function2():
    for i in range(5):
        print(f"2 ")

def function3():
    for i in range(5):
        print(f"3 ")

# function1()
# function2()
# function3()

t1= threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

t1.start()
t2.start()
t3.start()
t1.join()  # Wait for thread 3 to finish
print("All threads started")