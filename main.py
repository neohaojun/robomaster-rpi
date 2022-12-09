import os
import can
import asyncio
import pyb, time
from robo import RoboMaster
# import _thread # unsupported module

##########################
# Main loop
##########################

robo = RoboMaster()


async def heartbeat(robo):
    interval = 10 # miliseconds
    last = time.ticks_ms()
    while True:
        next = last + interval
        sleep = next - time.ticks_ms()
        if sleep > 0:
            #print(sleep)
            await asyncio.sleep_ms(sleep)
            last = next
        else:
            print('ROBO: running late')
            last = time.ticks_ms()
        
        robo.cb10ms()

async def can_send(robo):
    interval = 10 # miliseconds
    last = time.ticks_ms()
    while True:
        next = last + interval
        sleep = next - time.ticks_ms()
        if sleep > 0:
            #print(sleep)
            await asyncio.sleep_ms(sleep)
            last = next
        else:
            print('CAN: running late')
            last = time.ticks_ms()
        
        while robo.com.buf.any():
            pyb.LED(2).on()
            while (robo.can1.can.info()[5] == 3):
                print('passing')
                pass # wait till TX buffer is free
            robo.can1.can.send(robo.com.get()[3], 0x201)
            pyb.LED(2).off()

async def tcp_callback(reader, writer):
    print('TCP client connected')
    while True:
        try:
            # reading the TCP stream can sometimes take up to 250ms
            # therefore we need to repeat the CAN BUS commands for 300ms
            # in that way the stream of commands is never interrupted
            pyb.LED(1).off()
            start = time.ticks_ms()
            res = await reader.readline()
            robo.process_tcp(res.rstrip())
            pyb.LED(1).on()
            end = time.ticks_ms()
            if end -start > 10:
                print('TCP: running late ' + str(end - start))
        except Exception as e:
            print(e)
            break

def main(robo):
    loop = asyncio.get_event_loop()
    loop.create_task(heartbeat(robo))
    loop.create_task(can_send(robo))
    loop.create_task(asyncio.start_server(tcp_callback, "192.168.137.10", 8123, backlog=1))
    loop.run_forever()
    loop.close()

debug = False
if debug:
    # use a thread to keep REPL available for debugging
    # the _thread module is not supposed to be used directly
    # thread=_thread.start_new_thread( robo_thread, (robo, ) )
    print(0)
else:
    os.system('sudo ifconfig can0 down')
    os.system('sudo ip link set can0 type can bitrate 1000000')
    os.system('sudo ifconfig can0 up')

    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

    main(robo)
