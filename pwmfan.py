#!/usr/bin/env python

import psutil
import time


def temperature_to_duty_cycle(temp):
    if temp >= 75:
        # 100%
        return "40000"
    elif temp >= 70:
        # 75%
        return "30000"
    elif temp >= 65:
        # 50%
        return "20000"
    elif temp >= 60:
        # 25%
        return "10000"
    else:
        # 0%
        return "0"

def main():
    print("Starting PWM fan")
    # enable pwm
    with open("/sys/class/pwm/pwmchip0/pwm0/period", "w") as f:
        f.write("40000")
    with open("/sys/class/pwm/pwmchip0/pwm0/enable", "w") as f:
        f.write("1")
    while True:
        # get temperature
        temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
        duty_cycle = temperature_to_duty_cycle(temp)
        # set duty cycle
        with open("/sys/class/pwm/pwmchip0/pwm0/duty_cycle", "w") as f:
            f.write(duty_cycle)
        time.sleep(1)

if __name__ == "__main__":
    main()
