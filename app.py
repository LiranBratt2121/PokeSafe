import time
from servo import Servo
import machine

SERVO_PORT = 16
LIMIT_SWITCH_PORT = 22

PULL_UP = False
DELAY = 0.5
END = 90
START = 0

servo = Servo(pin_id=SERVO_PORT)

limit_switch = machine.Pin(LIMIT_SWITCH_PORT, machine.Pin.IN, pull=PULL_UP)

def rotate(position: int) -> None:
    servo.write(position)

def sleep(duration: int) -> None:
    time.sleep(duration)

def run_servo_routine() -> None:
    rotate(START)
    sleep(DELAY)
    rotate(END)
    sleep(DELAY)

def is_limit_switch_pressed() -> bool:
    if PULL_UP:
        return limit_switch.value() == 0
    else:
        return limit_switch.value() == 1

if __name__ == '__main__':
    while True:
        if is_limit_switch_pressed():
            run_servo_routine()
            
        print(f'{is_limit_switch_pressed()=}')
