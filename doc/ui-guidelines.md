# PERFEC System User Interface Guidelines

To make multiple Circuit Playgrounds work together as a musical instrument, each component's behavior should be predictable to the musician.

Software developers often follow a standard set of user (or "human") interface guidelines to create and maintain consistency.

If you are developing software for the Circuit Playground Express (CPX) to act as part of the PERFEC System, please follow the guidelines below.

## Active and Configuration Modes

Most PERFEC System interfaces will have two modes, commonly representing an active/playing mode and a configuration mode allowing the user to make common adjustments to the behavior of the module (e.g., selecting a MIDI note setting the tempo).

## Brightness

The default neopixel brightness SHOULD be `0.2`, e.g., `neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)`.

## Orientation

The interface MUST be designed with the USB port pointing up, the white text on the board should be upright, and button A on the left.

## Representing sequences 

When respresenting a sequence, the first neopixel (neopixel 0) MUST be the pixel directly to the left of the USB port.  The sequence MUST continue counterclockwise around the CPX.

## Representing selections

### Single selections

T
