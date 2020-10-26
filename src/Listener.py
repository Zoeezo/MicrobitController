from time import sleep
import serial

class Listener():

    def __init__(self, serialPort):
        self.serialPort = serialPort

    def start(self):
        self.listening = True
        self.paused = False

        while self.listening:

            if(self.serialPort.in_waiting > 0): 
                serialString = self.serialPort.readline().decode('utf-8').rstrip()
                yield serialString 
  
            while self.paused: 
                sleep(1)  

    def pause(self):
        self.paused = True
     
    def resume(self):
        self.paused = False

    def stop(self):
        self.listening = False