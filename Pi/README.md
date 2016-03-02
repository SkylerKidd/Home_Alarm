## Pi Setup
### Materials
+ [Raspberry Pi 2](http://www.amazon.com/gp/product/B00MV6TAJI) (other models work)
+ 2000 mA Micro USB Power Supply (comes with Pi linked above)
+ 8GB Micro SD Card (comes with Pi linked above)
+ [PIR Sensor](http://www.amazon.com/Adafruit-LK-918O-SANV-FBACA-PIR-Motion-Sensor/dp/B00JOZTAC6/)
+ Breadboard
+ Male-to-Female jumper wires
+ Ethernet cable or Wifi USB Adapter (adapter comes with Pi linked above)
+ *(Optional)* USB mouse and keyboard
+ *(Optional)* HD Monitor
+ *(Optional)* HDMI Cable (comes with Pi linked above)

### Installation
Follow the installation instructions for [NOOBS or Raspbian](https://www.raspberrypi.org/downloads/) onto the Micro SD Card.

Put the SD card into the Pi. Now connect the power supply, Ethernet/WiFi USB Adapter, and monitor/mouse/keyboard if you have them.

Open terminal and run ```sudo apt-get update``` to update the package lists. Then run ```sudo apt-get git-core``` to install git.

Clone the repo (```git clone [repo]```) to whatever directory you want to work out of, then cd to the /Home_Alarm/Pi/ folder.

Make sure you have a working internet connection.

Remove ".example" from the config filename and replace the example with your password.

### Hardware Setup
These are the GPIO pins for the Raspberry Pi 2:
<img src="gpio-numbers-pi2.png" width="396">

Now we will connect the PIR pins to the GPIO using the jumper cables and breadboard. Reference the above image when connecting the following pins:
+ Ground pin -> Ground pin (Black)
+ Digital out -> GPIO 7
+ +5v pin -> 5v pin (Red)

### Usage
From Terminal, make sure you're in the /Home_Alarm/Pi/ folder.

Now, you can simply run the ```python motion_sense.py``` command and watch your app work! :D
