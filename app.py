import time
from servo import Servo
from picozero import Button

BUTTON_PORT = 6
SERVO_PORT = 16
LIMIT_SWITCH_PORT = 22

DELAY = 1  # Seconds
START = 20
END = START + 90

should_open = True

servo = Servo(pin_id=SERVO_PORT)
limit_switch = Button(BUTTON_PORT)

def rotate(position: int) -> None:
    servo.write(position)

def sleep(duration: int) -> None:
    time.sleep(duration)

def rotate_to_end() -> None:    
    rotate(END)

def rotate_to_start() -> None:
    rotate(START)
    
if __name__ == '__main__':
    while True:
        if limit_switch.is_pressed:
            if should_open:
                rotate_to_start()
                sleep(DELAY)
                print(f'Rotate To Start, {should_open=}')
                should_open = False
            else:
                rotate_to_end()
                sleep(DELAY)
                print(f'Rotate To End, {should_open=}')
                should_open = True
                
