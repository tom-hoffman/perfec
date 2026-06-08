# Setting Up the PERFEC Two Channel Drum Machine

## What Are We Making?

A two channel drum machine made out of five Circuit Playground Express (CPX) microcontrollers.  "Two channel" in this case means the drum machine will play a beat made up of two different sampled sounds, playing different but synchronized rhythms.  The most obvious example of this is a kick and snare drum pattern, but we've provided thirty sample drum and percussion sounds, and you can add your own.  You can add more channels by adding more CPXs.  

This drum machine is based around two Euclidian sequencers.  A sequencer is a device or program which signals to an electronic instrument when to play a note or sample.  A Euclidian sequencer uses Euclid's Algorithm to evenly distribute a given number of played notes (triggers) over a total number of steps.  This type of sequencer is commonly used to generate a wide range of traditional rhythms from around the world, particularly polyrhythms, and it lets you quickly generate interesting beats with just the two buttons on a CPX.

## What You Need:

* 5 Circuit Playground Express boards;
* a computer connected to the internet that is configured to act as the USB MIDI host (more on this in a minute);
* at least five open USB ports you can connect to the computer, whether on a USB hub, directly on the PC, or a combination of the two;
* five micro USB cables.

This will also be easier if you can temporarily mount everything in place:
* a piece of cardboard, foam core, etc. about 11" by 14";
* masking tape, poster tack, etc.

By itself, your drum machine will quietly click using the tiny built in speaker on the CPX.  Once it is clicking away, to get a more satisfying sound level you will want:

* alligator clip wires, like those which come with a CPX class set;
* some kind of *powered* speakers (like computer speakers) or headphones with a built in or separate input cable you can clip onto.

If you want a more permanent setup, we will be posting 3d printable panels and instructions for securely attaching CPXs and jack sockets.

## Setting up a Computer as a USB MIDI Host

USB is the Universal Serial Bus, the standard way computers are connected to peripherals as well as a low voltage power source.  MIDI is the Musical Instrument Digital Interface, which is the protocol musical instruments talk to each other.  USB-MIDI means we're using USB to send and receive MIDI messages (there are many other ways to send MIDI as well).  This method requires a computer to act as the "host" of what is essentially a small network of Circuit Playgrounds.  

In practice, this host is usually a PC, Mac, Raspberry Pi or tablet.  It is possible with a more powerful microcontrollers like the RP2040 as well.

### Using a DAW on Mac or Windows.

Sadly, on Mac and Windows, this doesn't "just work."  On these systems, USB-MIDI hosting is usually handled through a Digital Audio Workstation (DAW) such as GarageBand, FL Studio, Logic or Ableton.  If you're used to using these, then your PERFEC System CPXs should show up and communicate like other MIDI devices.  On the other hand, we haven't tested this much, as we don't have DAWs set up at school.  We have not figured out how to set up a Mac or Windows PC to act as a USB-MIDI host without using a DAW.

### Chromebooks?

We have not really tried this.  It is probably possible on a non-locked down, that is a personal, Chromebook, using the Linux subsystem and following the instructions below..

### Setting up a USB-MIDI Host on a Rasperry Pi or other Linux PC

If you've already got five Circuit Playgrounds, there's a pretty good chance you've got a Raspberry Pi lying around, and we generally use these and Linux PCs as the USB-MIDI host.  In particular you can eventually just integrate a Raspberry Pi into a case with the CPXs to make a complete, portable drum machine.  

One of the keys to this entire project has been [these excellent instructions on setting up a Rasberry Pi as a USB-MIDI host by Fabio Barbon at Neumatica Studio](https://neuma.studio/rpi-as-midi-host/).  They provide pre-configured images for the Raspberry Pi 2B/3B/4B that don't require anything beyond installing the images on a microSD card.  In our experience these work fine.

If you have a different Rasberry Pi (e.g., Raspberry Pi 5), or *any other computer running a Debian-based Linux distribution* such as Raspbian or Ubuntu, then you can also simply use part of the ["detailed instructions"](https://neuma.studio/raspberry-pi-as-usb-bluetooth-midi-host/) to manually add USB-MIDI host capability.  The instructions are *very* clear and the process is fairly easy if you have any experience with copy/pasting commands into a terminal window.  

If you're using a Rasberry Pi, the detailed instructions include preliminary steps to connect over WiFi and SSH to a fresh Rasberry Pi with a minimal installation.  we find it easier and less intimidating just do a full desktop install and perform these steps directly on the Raspberry Pi.  You can disable the graphical interface later to get faster USB performance if you need to. 

If you are doing this with a regular Linux or Raspbian desktop, you can scroll down through the instructions and start with the commands:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install ruby git
```
These are right above the section header **CONFIGURING AUTOMATIC MIDI CONNECTION**  Continue until you get to **MIDI BLUETOOTH SETUP**.

## Setting Up CircuitPython on the CPX

### OPTIONAL: Update your Firmware

In your PERFEC System, your Circuit Playgrounds will probably get frequently shut down and restarted without being properly unmounted, as much as you try to remember to eject.  We *think* the most recent CPX firmware handles this a bit better, but we've not done any A/B testing, and it may be our imagination or some other change in how we use the CPX.  You might safely skip this step and then come back if you find your CPXs are frequently reverting to write protected or otherwise misbehaving beyond what the simple disk repair process can fix.

* [Go to the CircuitPython download page for the Circuit Playground Express](https://circuitpython.org/board/circuitplayground_express/).

<img src="https://github.com/user-attachments/assets/bf8e881e-7d60-4c54-a2ac-c003f5cf7926" />

* Scroll down to the firmware section, It should look like this (the latest version will probably have changed since we wrote this):

<img width="400" height="373" alt="image3" src="https://github.com/user-attachments/assets/78cdbcca-9777-4dd5-8fb8-852a09fd2814" />

* Click on `DOWNLOAD UPDATER U2F` on the Adafruit page. Now plug in a Circuit Playground. You should get a notification that a device has been plugged in. Follow the directions in the 3rd paragraph above. The drive will probably be called "CPLAYBOOT" rather than "BOOT." 

* After you’ve done this there should be a file on the CPLAYBOOT drive called “INFO_UF2” and it should have the version number as the download page.

<img width="279" height="184" alt="image4" src="https://github.com/user-attachments/assets/0c20c10b-3aea-4df0-8637-511b1733b4ea" />

### Installing a Supported CircuitPython

Because most PERFEC System boards use pre-compiled code, you'll have to download a version of CircuitPython specifically supported by the PERFEC System (or pre-compile the libraries to work with another version, if you know how to do that). 

Currently we recommend CircuitPython 10.1.4.  

[Download CircuitPython 10.1.4](https://adafruit-circuit-python.s3.amazonaws.com/bin/circuitplayground_express/en_US/adafruit-circuitpython-circuitplayground_express-en_US-10.1.4.uf2)

You can then follow the rest of the [instructions from Adafruit to install CircuitPython](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart).

Repeat the above steps for each CPX in your PERFEC System.  We recommend plugging in one CPX at a time and ejecting its drive and unplugging before moving to the next board.  Note that once you have the files downloaded, you can drag and drop the files to copy them onto all your CPXs.  This goes pretty quickly.  

### Installing PERFEC System Software

These steps install the Perfec System code.  Again we recommend to work on one board at a time in this step so you don't get the boards too mixed up during the installation step.

In this process we will be setting up:

* 1 x PERFEC Clock (MIDI clock)
* 2 x PERFEC Euclidian (Euclidian sequencer)
* 2 x PERFEC Player (sample player)

For each board, follow these steps:

* Plug in one CPX, with CircuitPython installed.
  
* After several seconds, a removable drive should appear. By default, these are called CIRCUITPY, but if you've installed other PERFEC System software on it before, it might be different.
 
* Open the removable drive.
  
* Open boot_out.txt and read the first line with the required version, either CircuitPython 10.0.3 or CircuitPython 10.1.4.  If it is a different version, you will need to install 10.0.3 or 10.1.4 as instructed above.
  
* Go to the release page for the component you are installing:
  * [PERFEC Clock](https://github.com/tom-hoffman/perfec_clock/releases)
  * [PERFEC Euclidian](https://github.com/tom-hoffman/perfec_euclidian/releases)
  * [PERFEC Player](https://github.com/tom-hoffman/perfec_player/releases)

* Choose the latest release and download `Source code (zip)` to somewhere you can find it.  If there are multiple zip files, select the one with the version number that matches with the version number of CircuitPython you are using (as described above).

<img src="https://github.com/user-attachments/assets/aafdc1c0-495c-44ec-8037-eb3607601b91" />

* Navigate to the downloaded zip file on your computer.
  
* Unzip the file.

  <img width="400" src="https://github.com/user-attachments/assets/cdff0569-ec7d-48c3-ba9d-ed0e0179ce73" />
  
* Open the unzipped folder. There may be a few layers of folders, continue until you see code.py and other files.
  
* Delete all files and folders already on the Circuit Playground. After deleting the files the Circuit Playground should flash green.
  
* Drag all the files from the unzipped folder to CIRCUITPY. Note that code.py and other .py and .mpy files should be directly in CIRCUITPY, not enclosed in another folder.
  
* After the files copy, the Circuit Playground’s neopixels should change to something other than all green, or solid white, or flashing red or yellow.

[Board setup video](https://drive.google.com/file/d/12MoxouWFVcWB8Zqwr7Qv0dZnY8s5SNPT/view?usp=sharing)

[Initial connection check video](https://drive.google.com/file/d/1d4w4niO3vPf2-eCwLhLkHZQjL8RvQ5ET/view?usp=drive_link)

[Basic configuration video](https://drive.google.com/file/d/13d3uO_K4CJEDPUeYtaqOHzr7q6M80wJf/view?usp=sharing)

[Sample player video](https://drive.google.com/file/d/10Y_XM5Sd7_rTTCjH-fuyVWu2JzwqtLyi/view?usp=sharing)
