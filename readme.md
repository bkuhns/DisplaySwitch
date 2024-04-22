# DisplaySwitch

A very simple tool written in python for switching Windows' display configuration through a REST service. This effectively alternates between the "Extend" and "Second screen only" options in Windows' "Project" menu.

## Setup

### Install dependencies

`python -m pip install Flask`

### Produce a runnable .exe

If you want a single .exe file to run, install `PyInstaller` then build the .exe:

`python -m pip install PyInstaller`

`python -m PyInstaller DisplaySwitch.py --onefile --noconsole`

### Run at startup

To run at startup so the service is always available:

 1. Press `Win`+`R`, type `shell:startup`, hit enter. This will open Windows Explorer at your startup folder.
 2. Right-click in the background of this folder and select `New` then `Shortcut`
 3. Browse for the DisplaySwitch.exe you produced earlier.

## Notice

This script uses the Flask development server, NOT a production server. This could be a security risk.

## Motivation

I use my PC as both a desktop workstation with two monitors at a desk, and as a video game console through a TV; but I play games on either. Because games really like to use the primary display, having a single extended display across both my monitors and TV is frustrating. It's cumbersome trying to get a game to draw to the correct screen I want to play on at the time. So, I wanted to find a way to make my two display configurations explicit. Only use my monitors or only use my TV.

If you open the "project" menu (`Win`+`P`) in Windows, you'll see the options for "Extend" but also "Second screen only". At least on Nvidia graphics cards, the HDMI input is treated as a "second screen". My monitors, connected over DisplayPort, are _not_ considered "secondary". So, I discovered I could configure the "Extend" configuration to disable the TV and the "Second screen only" configuration to disable my monitors. Now when I switch between "Extend" and "Second screen only", I can alternate the display output between my monitors and my TV. Now games get the correct primary display based on the current display configuration.

But, when it's late at night and I'm already relaxing on the couch, I don't want to have to go to my desk (in another room) to hit `Win`+`P` and pick the correct option so I can play a game on the TV. So, I set out to automate this somehow. That's when I learned about the Windows command, [`DisplaySwitch`](https://ss64.com/nt/displayswitch.html). The Python script in this repo is a REST wrapper around the `DisplaySwitch` command. Now I can remotely switch between my two distinct display configurations from my phone.
