from gpiozero import Button, LED
btn = Button(17)
led = LED(4)
btn.when_pressed = led.on
btn.when_released = led.off

# Blink led at 2 sec interval 
while True: 
    led.on () 
    time.sleep(2)
    led.off()
    time.sleep(2)