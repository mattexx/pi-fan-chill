# Pi fan, chill

Simple python daemon to control PWM fan speed. Works out of the box with the official pi fan on the
pi 4b.

## Why

PWM fans don't need to be just on or off. In the case of the official pi fan, I wanted to make a
graded response to CPU temperature instead of the on/off implementation supported in Raspbian. I
have found that the official pi fan running 25-50% is more than enough to keep the pi at a nice
temperature as a result.

## How

The python daemon uses sysfs to control fan speed. This involves writing to files in
`/sys/class/pwm` which are picked up by the system with ~msec response times. This is not as fast as
using realtime C code but much simpler and easily meets needs of updating fan speed on ~1sec
interval.

## Setup

First install the fan, plugging the blue wire into a GPIO that supports hardware PWM necessary to
drive the fan at 25 kHz. You can use GPIO 12 or 18 with the default script. If you want to use GPIO
13 or 19 just change the bottom folder in the script to `pwm1`.

Now [download](https://librpip.frasersdev.net/get/download/) and
[install](https://librpip.frasersdev.net/get/install/) librpip and enable pwm-init by adding the
following right before `exit 0` in `/etc/rc.local`:

    /usr/local/bin/librpip-util/librpip-pwm-init

Next enable GPIO on your desired pin, for example for GPIO 18 (pin 12) add the following to
`/boot/config.txt`:

    dtoverlay=pwm,pin=18,func=2

Clone this project into the pi homedir:

    git clone git@github.com:mattexx/pi-fan-chill.git

Copy the service file for systemd:

    sudo cp pi-fan-chill/pwmfan.service /etc/systemd/system

Enable the systemd service:

    sudo systemctl enable pwmfan

Reboot:

    sudo reboot now

Profit!

## Config

Coming soon! For now please edit source as needed.

## References

- [GPIO Programming: Using the sysfs Interface](https://www.ics.com/blog/gpio-programming-using-sysfs-interface)
- [libprpip](https://librpip.frasersdev.net/)
- [Device tree
  readme](https://github.com/raspberrypi/linux/blob/rpi-4.19.y/arch/arm/boot/dts/overlays/README)
  (useful if you are changing GPIO pins, lookup "pwm")
