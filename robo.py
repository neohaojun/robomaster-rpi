import canbus
from crc import Crc
from com import Command
import time

class RoboMaster():
    def __init__(self):

        self.crc = Crc()
        self.can1 = canbus.CanInterface(1)
        self.com = Command(self)

        self.linear = Linear()
        #self.angular = Angular()

        self.timcount  = 0

        self.tim2 = pyb.Timer(2)
        self.tim2.init(freq=10)
        #self.tim2.callback(self.cb)

    def cb(self, t):       
        self.linear.reset()
        
    def cb10ms(self):
        self.timcount += 1
        self.linear.reset()

        start = time.ticks_ms()
        
        self.com.add_10ms()
        
        if self.timcount % 4 == 0:
            self.com.add_40ms()

        if self.timcount % 9 == 0:
            self.com.add_90ms()

        if self.timcount % 100 == 0:
            self.com.add_1sec()

        #if self.timcount % 1000 == 0:
        #    self.com.add_10sec()

        if self.timcount == 1001:
            self.timecount = 1

        end = time.ticks_ms()
        #if end -start > 1:
        #    print('Time taken: ' + str(end - start))
        #print(str(self.timcount) + ' ' + str(self.linear.x))


class Linear():
    def __init__(self):
        print('Linear init')
        self.t0 = time.ticks_ms()
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.moving = 0

    def reset(self):            
        #print(self.y)    
        if self.moving and time.ticks_diff(time.ticks_ms(), self.t0) > 300:
            print('reset')
            self.x = 0.0
            self.y = 0.0
            self.z = 0.0
            self.moving = 0

    def set(self, x, y, z):
        self.t0 = time.ticks_ms()
        self.x = self.check_value(x)
        self.y = self.check_value(y)
        self.z = self.check_value(z)
        self.moving = 1

    def check_value(self, value):
        if value > 1.0 or value < -1.0:
            value = 0.0

        if value == 1.0:
            value = 0.9998
        elif value == -1.0:
            value = -0.9998

        return value
