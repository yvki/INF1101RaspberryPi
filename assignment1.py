# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Refer to pins by the “Broadcom SOC channel number” (num inside the chip after GPIO used in RPi)
GPIO.setmode(GPIO.BCM)

# Select which GPIOs you will use
TRIG = 21 
ECHO = 20 
BUZZER = 26

GPIO.setup(BUZZER, GPIO.OUT) # Set BUZZER to OUTPUT mode
GPIO.setup(TRIG, GPIO.OUT) # Set TRIGGER to OUTPUT mode
GPIO.setup(ECHO, GPIO.IN) # Set ECHO to INPUT mode

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

# Calculates the frequency of beeping depending on the measured distance
def beep_freq():
  # Measure the distance
  dist = distance()
  # If the distance is larger than 50 cm, there is no beep
  if dist > 50:
    return -1
  # If the distance is between 50 and 30 cm, beep once a second
  elif dist <= 50 and dist >=30:
    return 1
  # If the distance is between 30 and 20 cm, beep twice a second
  elif dist < 30 and dist >= 20:
    return 0.5
  # If the distance is between 20 and 10 cm, beep four times a second
  elif dist < 20 and dist >= 10:
    return 0.25
  # If the distance is smaller than 10 cm, beep constantly
  else:
    return 0

# Main function
def main():
  try:
    # Repeat till the program is ended by the user
    while True:
      # Get the beeping frequency
      freq = beep_freq()
      # No beeping
      if freq == -1:
        GPIO.output(BUZZER, False)
        time.sleep(0.25)
      # Constant beeping
      elif freq == 0:
        GPIO.output(BUZZER, True)
        time.sleep(0.25)
      # Beeping on certain frequency
      else:
        GPIO.output(BUZZER, True)
        time.sleep(0.2) # Beep is 0.2 seconds long
        GPIO.output(BUZZER, False)
        time.sleep(freq) # Pause between beeps = beeping frequency
  # If the program is ended, stop beeping and cleanup GPIOs
  except KeyboardInterrupt:
    GPIO.output(BUZZER, False)
    GPIO.cleanup()

# Run the main function when script is executed
if __name__ == "__main__":
    main()