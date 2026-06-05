# Setting Up the PERFEC Two Channel Drum Machine

## What Are We Making?

A two channel drum machine made out of five Circuit Playground Express (CPX) microcontrollers.  "Two channel" in this case means the drum machine will play a beat made up of two different sampled sounds, playing different but synchronized rhythms.  The most obvious example of this is a kick and snare drum pattern, but we've provided thirty sample drum and percussion sounds, and you can add your own.  You can add more channels by adding more CPXs.  

This drum machine is based around two Euclidian sequencers.  A sequencer is a device or program which signals to an electronic instrument when to play a note or sample.  A Euclidian sequencer uses Euclid's Algorithm to evenly distribute a given number of played notes (triggers) over a total number of steps.  This type of sequencer is commonly used to generate a wide range of traditional rhythms from around the world, particularly polyrhythms, and it lets you quickly generate interesting beats with just the two buttons on a CPX.

## What You Need

* 5 Circuit Playground Express boards;
* a computer connected to the internet that is configured to act as the USB host;
* at least five open USB ports you can connect to the computer, whether on a hub, directly on the PC, or a combination of the two;
* 
