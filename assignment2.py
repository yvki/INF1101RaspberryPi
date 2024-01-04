# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Import required libraries to play wav file
import pygame

# Refer to pins by the “Broadcom SOC channel number” (num inside the chip after GPIO used in RPi)
from GPIO import Button
GPIO.setmode(GPIO.BCM)

# Select which GPIOs and buttons you will use
TRIG = 21 
ECHO = 20

btn1 = Button(17)
btn2 = Button(22)
btn3 = Button(23)
btn4 = Button(27)

# Set button to INPUT mode 
# read value using GPIO.input, return False if button is pressed
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set TRIGGER to OUTPUT mode
GPIO.setup(TRIG, GPIO.OUT)
# Set ECHO to INPUT mode
GPIO.setup(ECHO, GPIO.IN)

# Measures the distance between a sensor and an obstacle and returns the measured value
def distance():
  GPIO.output(TRIG, True) # set TRIGGER to HIGH
  time.sleep(0.00001) # wait 10 microseconds
  GPIO.output(TRIG, False) # set TRIGGER back to LOW
 
  # Create variable start and assign it current time
  pulse_start = time.time()
  # Create variable stop and assign it current time
  pulse_end = time.time()
  # Refresh start value until the ECHO goes HIGH = until the wave is send
  while GPIO.input(ECHO) == 0:
    pulse_start = time.time()
 
  # Assign the actual time to stop variable until the ECHO goes back from HIGH to LOW = the wave came back
  while GPIO.input(ECHO) == 1:
    pulse_end = time.time()
 
  # Calculate the time it took the wave to travel there and back
  pulse_duration = pulse_end - pulse_start
  # Calculate the travel distance by multiplying the measured time by speed of sound
  distance = pulse_duration * 17150
  distance = round(distance, 1)

  # Print the distance to see if everything works correctly
  # print('Distance : {0:5.1f}cm'.format(distance))
  print('Distance:',distance,'cm')
  # Return the actual measured distance
  return distance

# Play music depending on the measured distance
def got_music():
  # Measure the distance
  dist = distance()
  # If the distance is larger than 50 cm, there is no music
  if dist > 50:
    return 0
  # If the distance is between 50 and 30 cm, play music#1
  elif dist <= 50 and dist >=30:
    return 1
  # If the distance is between 30 and 20 cm, play music#2
  elif dist < 30 and dist >= 20:
    return 2
  # If the distance is between 20 and 10 cm, play music#3
  elif dist < 20 and dist >= 10:
    return 3
  # If the distance is smaller than 10 cm, play music#4
  else:
    return 4

pygame.init()
pygame.display.set_mode(pygame.display.list_modes()[-1])
pygame.mixer.init()

def play_file1():
    pygame.mixer.music.load("/home/pi/gpio_music_box/lab/drum_bass_hard.wav") 
    pygame.mixer.music.play()

def play_file2():
    pygame.mixer.music.load("/home/pi/gpio_music_box/lab/perc_bell.wav")
    pygame.mixer.music.play()

def play_file3():
    pygame.mixer.music.load("/home/pi/gpio_music_box/lab/misc_crow.wav")
    pygame.mixer.music.play()

def play_file4():
    pygame.mixer.music.load("/home/pi/gpio_music_box/lab/guit_harmonics.wav")
    pygame.mixer.music.play()

# Main function
def main():
  # Program should end (exit) when the user press a pushbutton 
  complete = False
  while complete == False:
    input_state1 = GPIO.input(17)
    input_state2 = GPIO.input(22)
    input_state3 = GPIO.input(23)
    input_state4 = GPIO.input(27)
    # Print on the screen that the program ended
    if input_state1 == False:
      complete = True
      print('Exited program with button 17.')
      GPIO.cleanup()
    elif input_state2 == False:
      complete = True
      print('Exited program with button 22.')
      GPIO.cleanup()
    elif input_state3 == False:
      complete = True
      print('Exited program with button 23.')
      GPIO.cleanup()
    elif input_state4 == False:
      complete = True
      print('Exited program with button 27.')
      GPIO.cleanup()
    else:
      music = got_music()
      if music == 0:
        time.sleep(0.25)
      elif music == 1:
        play_file1()
        time.sleep(0.25)
      elif music == 2:
        play_file2()
        time.sleep(0.25)
      elif music == 3:
        play_file3()
        time.sleep(0.25)
      elif music == 4:
        play_file4()
        time.sleep(0.25)

# Run the main function when script is executed
if __name__ == "__main__":
    main()