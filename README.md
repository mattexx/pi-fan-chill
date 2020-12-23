# Pi fan, chill

Simple python daemon to control PWM fan speed.

## Why

There are many valid use cases for fine-tuned PWM fan control, including with the official pi fan.
In the case of the official pi fan, I wanted a graded response to CPU temperature instead of the
on/off implementation supported in Raspbian, since I find the fan a little noisy at 100%.

## How

The python daemon uses sysfs to control fan speed. This involves writing to files in
`/sys/class/pwm` which are picked up by the system with ~msec response times. This is not as fast as
using realtime C code but much simpler and easily meets needs of updating fan speed on ~1sec
interval.

## Setup

First install the fan, plugging the blue wire into a GPIO that supports hardware PWM necessary to
drive the fan at 25 kHz. You can use GPIO 12 or 18 with the default script. If you want to use GPIO
13 or 19 just change the bottom folder in the script to `pwm1`.

Next enable GPIO on your desired pin, for example pin 12 (GPIO 18):

    dtoverlay=pwm,pin=18,func=4

Clone this project into the pi homedir:

    git clone git@github.com:mattexx/pi-fan-chill.git

Copy the service file for systemd:

    sudo cp pi-fan-chill/pwmfan.service /etc/systemd/system

Enable the systemd service:

    sudo systemctl enable pwmfan

Reboot:

    sudo reboot now:

Profit!

## Config

Coming soon! For now please edit source as needed.
