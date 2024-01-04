## Problem Statement
In this project, you will build a music box using Raspberry Pi 400 that can be controlled by pushbuttons and an ultrasonic sensor. Using Python to play the music, the music box will play the different sounds when different pushbuttons are pressed. A distinct sound will be played for each button, and the respective LED is turned ON for the duration of that button press. Furthermore, different music is played when the distance between the ultrasonic sensor and an obstructing solid surface or obstacle is varied. 

## List of Equipment
(a) Raspberry Pi 400 \ 
(b) Maker Hat for Raspberry Pi 400 \ 
(c) Ultrasonic Sensor HC-SR04 \
(d) 1 1kΩ and 1 1.5kΩ Resistor \
(e) USB Speaker 

### Specifications of (a)
The Raspberry Pi 400 is a compact personal computer built into a compact keyboard. Its CPU is Broadcom 1.8GHz 64-bit quad-core ARMv8, and it incorporates a purpose-built board based on Raspberry Pi 4. Fig. 1 shows the Raspberry Pi 4 and its ports:

<img width="239" align="right" src="https://github.com/yvki/INF1101RaspberryPi/assets/66511759/5db62f39-2b05-485f-abd1-6764bdd45c27">

| Port | Description |
| -- | -- |
| A | 40-pin GPIO |
| B | MicroSD Main hard drive |
| C, D | Micro HDMI ports |
| E | USB-C port for power ON/OFF |
| F, G | USB 3.0 ports |
| H | USB 2.0 port |
| I | Gigabit Ethernet port |

### Specifications of (b)
The Maker HAT Base is used to efficiently extend the Raspberry Pi 400 GPIO pins using a 40-way ribbon cable. Each GPIO pin is clearly labelled with a status LED for easier testing and troubleshooting. The onboard buzzer and pushbuttons are helpful for immediate coding without the need to build your own circuit, while external sensors can also be connected through onboard Grove ports (GPIO, UART & I2C), which comes with an integrated breadboard that allows for easier wiring. Other key features include programmable fixed tone buzzer and buttons that are internally connected to GPIO26, and GPIO17, 22, 23 and 27 respectively. 

<img width="371" alt="b" src="https://github.com/yvki/INF1101RaspberryPi/assets/66511759/814db06b-74b1-49a2-89d8-13ab269d1713">

### Maker HAT Base HAT and GPIO Extension for Raspberry Pi 400

<img width="348" alt="b1" src="https://github.com/yvki/INF1101RaspberryPi/assets/66511759/b43210c7-e4f8-499f-b2ac-9850b968e44c">

### Specifications of (c)
The HC-SR04 ultrasonic distance sensor consists of two ultrasonic transducers. One acts as a transmitter that converts the electrical signal into 40 KHz ultrasonic sound pulses, while the other acts as a receiver and listens for the transmitted pulses. 

<img width="151" align="right" src="https://github.com/yvki/INF1101RaspberryPi/assets/66511759/df181f21-22c6-4875-b9b7-70e114b51e9f">

| Type | Measurement |
| -- | -- |
| Operating Voltage | DC 5𝑉 |
| Operating Current | 15mA | 
| Operating Frequency | 40KHz | 
| Max Range | 4m | 
| Min Range | 2cm | 
| Ranging Accuracy | 3mm | 
| Measuring Angle | 15 degrees | 
| Trigger Input Signal | 10μS TTL pulse | 
| Dimension | 45 x 20 x 15mm | 

When the receiver receives these pulses, it produces an output pulse whose width is proportional to the distance of the object in front. This sensor provides excellent non-contact range detection between 2 cm to 400 cm (~13 feet) with an accuracy of 3 mm.

| Pinout | Usage | 
| -- | -- |
| VCC | Supplies power to the HC-SR04 ultrasonic sensor through connection to 5𝑉 output from Raspberry Pi 400 |
| Trig (Trigger) pin | Trigger ultrasonic sound pulses (by setting this pin to HIGH for 10μs, the sensor initiates an ultrasonic burst) |
| Echo pin | Goes high when the ultrasonic burst is transmitted and remains high until the sensor receives an echo, after which it goes low (by measuring the time that this pin stays high, the distance can be calculated) |

## Tasks
1. Modify code to blink the LED with 2 seconds ON/OFF interval 
2. Modify code for remaining pushbuttons to play sounds by linking remaining audio files (bell, bird and guitar) to their distinct GPIO pins
3. Use voltage divider and fix suitable values for the resistors to obtain an approximate 𝑉out of 3𝑉 (tolerance of ±0.05𝑉) from the default 5𝑉

## Assignments
1. Write the full code and demonstrate to the lab instructor the working of the system that plays different audio beeps based on the distance between the ultrasonic sensor and the obstacle
2. Write the full code and demonstrate to the lab instructor the working of the system that plays different music files based on the distance between the ultrasonic sensor and the obstacle
