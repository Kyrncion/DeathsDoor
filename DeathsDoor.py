from random import randint
import time
print('-------------------------------------------------------------------')
print('| Quick, he\'s right behind you! You must find a way out, quickly! |')
running = True
score = 0
while running:

    doors = randint(1, 3)
    time.sleep(3)
    print('-------------------------------------------------------------------')
    print('| Three doors lay ahead...                                        |')
    print('| Death sleeps behind one...                                      |')
    print('| Which door do you open..?                                       |')
    door = input('| 1, 2 or 3 = ') 
    door_num = int(door)
    if door_num == doors:
        time.sleep(1.5)
        print('-------------------------------------------------------------------')
        print('| Its Death!                                                      |')
        print('| Game over! You survived going through', score, 'doors!                  |')
        print('-------------------------------------------------------------------')
        time.sleep(6)
        running = False
    else:
        time.sleep(1.5)
        print('-------------------------------------------------------------------')
        print('| You live to see another day...                                  |')
        print('| You enter the next room...                                      |')
        score = score + 1
