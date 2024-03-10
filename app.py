import time
from servo import Servo
from picozero import Button
from neopixel import NeoPixel
from machine import Pin

BUTTON_PORT = 6
SERVO_PORT = 16
LEDS_PORT = 28
LED_AMOUNT = 8


DELAY = 1  # Seconds
START = 20
END = START + 90

should_open = True

servo = Servo(pin_id=SERVO_PORT)
limit_switch = Button(BUTTON_PORT)
leds = NeoPixel(Pin(LEDS_PORT), LED_AMOUNT)

def rotate(position: int) -> None:
    servo.write(position)

def sleep(duration: int) -> None:
    time.sleep(duration)

def rotate_to_end() -> None:    
    rotate(END)

def rotate_to_start() -> None:
    rotate(START)
    
def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

if __name__ == '__main__':
    while True:
        demo(leds)
        
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

