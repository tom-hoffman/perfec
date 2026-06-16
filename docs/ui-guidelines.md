# PERFEC System User Interface Guidelines

To make multiple Circuit Playgrounds work together as a musical instrument, each component's behavior should be predictable to the musician.

Software developers often follow a standard set of user (or "human") interface guidelines to create and maintain consistency.

If you are developing software for the Circuit Playground Express (CPX) to act as part of the PERFEC System, please follow the guidelines below.

Words in all caps; e.g, MAY, MUST, follow their definition in [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119).

## Active and Configuration Modes

Most PERFEC System interfaces will have two modes, commonly representing an active/playing mode and a configuration mode allowing the user to make common adjustments to the behavior of the module (e.g., selecting a MIDI note setting the tempo).

## Brightness

The overall neopixel brightness MUST be `0.2`, e.g., `neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)`.  In our experience, this is bright enough to be seen in any indoor lighting conditions, and anything brighter tends to get unpleasant to look straight at.  From this starting point, we usually keep the RGB values of the neopixels low as well (i.e., start with a RGB value of 16 rather than 255).

## Red LED

The CPX's red LED MUST indicate USB MIDI activity.  The red LED SHOULD toggle on/off when the primary MIDI message used by the module is received or sent.  A release version of a module SHOULD NOT toggle the red LED on every MIDI message received.

## Orientation

The interface MUST be designed with the USB port pointing up, the white text on the board should be upright, and button A on the left.

## Representing sequences 

When respresenting a sequence, the first neopixel (neopixel 0) MUST be the pixel directly to the left of the USB port.  The sequence MUST continue counterclockwise around the CPX.

## Representing selections

### Single selections

## config.py

With CircuitPython, each CPX connected to a computer is mounted as a USB drive, and the `.py` files can be edited (`.mpy` bytecode files aren't human readable).  This means we can create configuration files to allow the user to make changes to settings beyond what can be done with the buttons, switches, neopixels and other UI elements and sensors on the CPX.

By conventions, any setting or variable that the user might want to change should be defined and documented in a `config.py` file.  This is just a regular CircuitPython file, there's no special format.  

### Required variables

`config.py` MUST contain a `USB_NAME` variable which is used to identify the board by both the name of the USB drive when mounted as a disk (set using [`storage.label`](https://docs.circuitpython.org/en/latest/shared-bindings/storage/#storage.VfsFat.label)) and as the USB "product" designation (set using [`supervisor.set_usb_identification`](https://docs.circuitpython.org/en/latest/shared-bindings/supervisor/index.html#supervisor.set_usb_identification)). 

When multiple instances of a module will be used in the same system (e.g., multiple sequencer tracks) `USB_NAME` MAY be constructed by concatenating a root `USB_NAME` with a separate `CPX_NUMBER` variable.  For example `USB_NAME = "PLAYER" + str(CPX_NUMBER).`  
