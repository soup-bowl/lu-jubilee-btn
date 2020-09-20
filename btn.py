from time import sleep
from gpiozero import Button, LED

button = Button("BOARD22", False, None)
light  = LED("BOARD7")

def led_blink(count):
    for x in range(count):
        light.on()
        sleep(0.25)
        light.off()
        sleep(0.25)

def btn_press():
    print("Button pressed.")
    light.on()
    sleep(2)
    light.off()

# Operation area.

print("Light test.")
led_blink(5)

print("Test done, waiting for command...")
while True:
    button.wait_for_press()
    btn_press()
