# main.py -- put your code here!
import pyb
from pyb import UART
from pyb import Pin
from pyb import Timer
from pyb import LED

import time

p = Pin('A0')  # X1 has TIM2, CH1
tim = Timer(2, freq=50)
ch = tim.channel(1, Timer.PWM, pin=p)

uart = pyb.UART(2, 9600)

led = LED(3)
while True:

    if uart.any():
        data = uart.readline()
        print("reseived:",data)
        # if data.decode().startswith('on'):
        #     led.on()
        # elif data.decode().startswith('off'):
        #     led.off()

        pyb.LED(4).on()
        ch.pulse_width_percent(3)
        time.sleep_ms(300)  # sleep for 500 milliseconds
        pyb.LED(4).off()

        pyb.LED(3).on()
        ch.pulse_width_percent(7)
        pyb.LED(3).off()
        # print('shot')


        uart.write('shot')

#
# from pyb import Pin
#
# p_in = Pin('B3',Pin.PULL_UP)
# value = p_in.value()
# print(value)
