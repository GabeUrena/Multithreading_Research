import threading

def cube (num):
    print(f'{num} cubed: {num*num*num}')

def sum (num1, num2):
    print(f'{num1} + {num2}: {num1+num2}') 


thread1 = threading.Thread(target=cube, args=(10,))
thread2 = threading.Thread(target=sum, args=(10,20,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Done.')