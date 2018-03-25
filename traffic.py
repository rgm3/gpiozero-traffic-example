#!/usr/bin/python
# -*- coding: utf-8 -*-

# See:
# https://gpiozero.readthedocs.io/en/stable/recipes.html#traffic-lights
# To restart after changing:
#   sudo systemctl restart traffic

from gpiozero import TrafficLights, Button
from time import sleep
from signal import pause
import random

RED = 27
YELLOW = 22
GREEN = 17
BUTTON_PIN = 4

lights = TrafficLights(RED, YELLOW, GREEN, pwm=True)
button = Button(BUTTON_PIN)

def main():
    button.when_pressed = lights.on
    button.when_released = lights.off
    lights.source = traffic_light_sequence()
    try:
        pause()
    except KeyboardInterrupt:
        quit()


def traffic_light_sequence():
    while True:
        yield (0, 0, 1) # green
        sleep(random.randrange(3,12))
        yield (0, 1, 0) # amber
        sleep(random.randrange(5,9))
        yield (0.05, 0, 0) # red
        sleep(random.randrange(3, 10))


if __name__ == "__main__":
    main()
