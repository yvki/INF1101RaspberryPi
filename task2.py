from gpiozero import Button, LED 
import time 
import pygame 
pygame.init()

# Create the sound objects
drum = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/drum_bass_hard.wav") 
btn_drum = Button(17)
btn_drum.when_pressed = drum.play

bell = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/perc_bell.wav") 
btn_bell = Button(22)
btn_bell.when_pressed = bell.play

bird = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/misc_crow.wav") 
btn_bird = Button(24)
btn_bird.when_pressed = bird.play

guitar = pygame.mixer.Sound("/home/pi/gpio_music_box/lab/guit_harmonics.wav")
btn_guitar = Button(27)
btn_guitar.when_pressed = guitar.play


led-1 = LED(4) 
led-2 = LED(5) 
led-3 = LED(6) 
led-4 = LED(7) 

btn_drum.when_pressed = drum.play 
btn_drum.when_pressed = led-1.on 
btn_drum.when_released = led-1.off 
btn_bell.when_pressed = bell.play 
btn_bell.when_pressed = led-2.on 
btn_bell.when_released = led-2.off 
btn_bird.when_pressed = bird.play 
btn_bird.when_pressed = led-3.on 
btn_bird.when_released = led-3.off 
btn_guitar.when_pressed = guitar.play 
btn_guitar.when_pressed = led-4.on 
btn_guitar.when_released = led-4.off