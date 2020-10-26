from microbit import *

while True:
    if(button_a.is_pressed()):
            print('buttonA')
    elif(button_b.is_pressed()):
            print('buttonB')
    else:
        print('None')