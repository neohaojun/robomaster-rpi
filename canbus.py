import can
from buf import FrameBuffer

class CanInterface:
    def __init__(self):
        self.can0 = can.Bus(interface = 'socketcan', channel = 'can0', bitrate=1000000)

        self.buf = FrameBuffer(64)

        self.send_caller = self.sendcb
        self.init()

    def init(self):

        print("can0 initialized")

    def send(self, message):
        micropython.schedule(self.send_caller, message)

    def sendcb(self, message):
        print(message)
        if self.can0.info()[5] < 3:
            self.can0.send(message[3], message[0])
        else:
            print("cannot send packet on can0, TX queue is full")

    def receive(self, bus, reason):
        self.can0.recv(self.itf-1, self.buf.put())