from Listener import Listener
from pynput.keyboard import Key, Controller
import serial

listener = Listener(serial.Serial(port = "COM5", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE))
keyboard = Controller()

commands = listener.start()

for command in commands:

    if(command == 'buttonA'):
        keyboard.press(Key.space)
    elif(command == 'buttonB'):
        keyboard.press(Key.down)
    else:
        keyboard.release(Key.down)
        keyboard.release(Key.space)