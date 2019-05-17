# RaspbusryPi
A program to display London bus times on a Raspberry Pi

This project uses a Raspberry Pi 3 equipped with a [Display-O-Tron](https://shop.pimoroni.com/products/display-o-tron-hat) from Pimoroni to display countdowns until the next bus from a specified London bus stop. This was hung in our flat entrance for 3 years to ensure nobody need wait at the bus stop unnecessarily.

It polls TFL's API for the predicted bus times over the next half-hour and formats them to match the countdowns seen in LED signs at London bus stops. Multiple buses from multiple stops can be displayed, moved between using the left and right capacitive keys on the Display-O-Tron.
