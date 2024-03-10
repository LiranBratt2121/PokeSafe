import time
from servo import Servo
from picozero import Button

BUTTON_PORT = 5
SERVO_PORT = 16
LIMIT_SWITCH_PORT = 22

NORMALY_OPEN = False
DELAY = 0.5 #seconds
START = 20
END = START+90


servo = Servo(pin_id=SERVO_PORT)

limit_switch = Button(BUTTON_PORT)

def rotate(position: int) -> None:
    servo.write(position)

def sleep(duration: int) -> None:
    time.sleep(duration)

def run_servo_routine() -> None:
    rotate(START)
    sleep(DELAY)
    rotate(END)
    sleep(DELAY)

def toggle_servo() -> None:
    if (place == END):
        rotate(START)
        place = START
    else:
        rotate(END)
        place = END

def rotate_to_end() -> None:
    rotate(END)

def rotate_to_start() -> None:
    rotate(START)
    
if __name__ == '__main__':
    while True:
        limit_switch.when_released = rotate_to_start
        limit_switch.when_pressed = rotate_to_end

        sleep(0.2)
        print(f'{limit_switch.value}')

