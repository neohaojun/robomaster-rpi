import can
from buf import FrameBuffer

class CanInterface:
    def __init__(self, itf):
        self.itf = itf
        self.can0 = can.Bus(interface = 'socketcan', channel = 'can0', bitrate=1000000)

        self.buf = FrameBuffer(64)

        self.send_caller = self.sendcb
        self.init()

    def init(self):
        can = self.can0
        can.init(mode=pyb.CAN.NORMAL, extframe=False, prescaler=3, sjw=1, bs1=15, bs2=2, auto_restart=True) # 1mbps @216Mhz
        can.setfilter(bank=self.itf-1, mode=pyb.CAN.MASK32, fifo=self.itf-1, params=(0x0, 0x0))
        can.rxcallback(self.itf-1, self.receive)
        print("CAN " + str(self.itf) + " initialized")

    def close(self):
        self.can0.rxcallback(self.itf-1, None)
        self.can0.deinit()

    def send(self, message):
        micropython.schedule(self.send_caller, message)

    def sendcb(self, message):
        print(message)
        if self.can0.info()[5] < 3:
            self.can0.send(message[3], message[0])
        else:
            print("cannot send packet on CAN" + str(self.itf) + ", TX queue is full")

    def receive(self, bus, reason):
        self.can0.recv(self.itf-1, self.buf.put())      