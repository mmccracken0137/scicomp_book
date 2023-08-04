#!/usr/bin/env python
# coding: utf-8

# # Python on microcontrollers with `circuitpython`

# ## Recap
# 
# Let's continue with our skills inventory with the foundations/applications dichotomy:
# - foundational programming skills
#     * basic mathematical operations, comparison operators
#     * iteration and recursion with loop control structures `for` and `while`
#     * keeping track of variables outside of loops (i.e., counting and summing)
#     * function definition and using functions *inside* of loops
#     * conditionals: `if`, `else`, and `elif`
#     * types: `int`, `float`, `string`, `bool`
#     * containers such as `list` and `dict`
#     * randm number generation
#     * accessing and iterating over elements in lists and dicts
#     * file I/O
#     * DEBUGGING!
#     * algorithmic thinking
# - applications
#     * basic (and semi-advanced) data visualization: histograms, scatter plots, higher-dimensions in 2-d
#     * fitting models to data and extracting results (with uncertainties)
#     * text analysis, asking questions with unstructured data
#     * simulating the solutions to ordinary differential equations, Euler Algorithm
#     * basic Monte Carlo techniques
#     * tabular data manipulation with `Pandas`, expolratory data analysis
# 
# I am running out of congratulatory things to say about the length and diversity of this list, so I'll just summarize with: **Wowzerz**.

# ***
# 
# ## Motivation
# 
# Here are some examples of things that normal, everyday people can do with microcontrollers like the ones we'll use in this lesson.
# 
# - [Raspberry Pi Pico featuring MEGA game compilation](https://hackaday.io/project/179032-raspberry-pi-pico-featuring-mega-game-compilation)
# - [TINY MECHANICAL KEYBOARD, POWERED BY PI PICO](https://hackaday.com/2021/06/09/tiny-mechanical-keyboard-powered-by-pi-pico/)
# 

# ***
# 
# ## Getting started with the ItsyBitsy 2040 and CircuitPython
# 
# In this lesson, we will work with `circuitpython` an implementation of `python` that runs on microcontrollers.  A microcontroller can be thought of as a small computer that reads/applies voltages to from/to electronic devices based on how it is programmed.  `circuitpython` allows us to use `python` to tell our microcontroller how to behave.
# 
# Most of our work will happen in Mu.  This notebook serves as a rough set of notes and in-class problems.
# 
# ### Configuring your ItsyBitsy
# 
# First we have to set up our ItsyBitsy to run `circuitpython`.
# If you get stuck, Adafruit provides a LOTS of great info [here](https://learn.adafruit.com/adafruit-itsybitsy-rp2040?gclid=Cj0KCQjwpImTBhCmARIsAKr58cyh8RAWJTX6vksQ2wjPP402KB8WYACLtVM5YsjFqXamdDtzxqffuUsaAuQjEALw_wcB)
# 
# 1. Download the ItsyBitsy-specific CircuitPython implementation from [circuitpython.org](https://circuitpython.org/board/adafruit_itsybitsy_rp2040/).  We're going to use the current version (7.2.5), but any 7.x will work for this tutorial.
# 2. Install the uf2 file on your ItsyBitsy (IB).  Plug the IB into USB.  From Adafruit: 
# > To enter the bootloader, hold down the BOOT/BOOTSEL button (highlighted in red above), and while continuing to hold it (don't let go!), press and release the reset button (highlighted in blue above). Continue to hold the BOOT/BOOTSEL button until the RPI-RP2 drive appears!
# 3. Move the uf2 file to RPI-RP2 drive that appears on your computer.  The drive will disappear and reappear with the name "CIRCUITPY".  You're (almost) ready to rock!
# 
# ### Programming for the ItsyBitsy
# 
# CircuitPython IS Python... with a lot of other microcontroller-specific capabilities built in.
# 
# To run code on the IB, we write the code as a stand-alone python program on our computer and then save it as `code.py` on the IB.  This is doable with any editor, but we'll be using `Mu` because it is optimized for `circuitpython`.
# 
# Please download `Mu` [here](https://codewith.mu/en/download).
# 
# ### Modules
# 
# `circuitpython` has some nifty built-in modules.  Here are two examples we'll use below:
# - `time` -- especially `sleep`
# - `board` -- Gives access to board features/components.  Try `dir(board)`.
# - `digitalio` 
# 
# Other modules are specific to the board we are using.  For example, the IB has a built-in NeoPixel, and Adafruit provides libraries for easy NeoPixel control.  Lots more libraries available from [circuitpython.org](https://circuitpython.org/libraries) -- please download the `zip` bundle (make sure it matches the 7.x `circuitpython` version).

# ***
# 
# ## Let's program!
# 
# In addition to being an editor, `Mu` provides a command-line interface (CLI) for the IB's serial port.  (Click the "Serial" icon at the top of the window.)  You can now type `python` code line-by-line directly to the IB!   And get serial output from the IB!  This is a great way to test out the IB's capabilities.
# 
# As with our previous `python` programs, you can always stop a program by pressing [CTRL + C] in the CLI.
# 
# Let's try the following (type or paste into Mu's Serial interface):
# 
# >```python
# >print('Hello, world!')
# >```
#     
# Your ItsyBitsy should say this back to you through the CLI!  Next, we'll try a 2-line program.  Note that the indentation of the second line is still **important**!
# 
# >```python
# >for i in range(10):
# >    print('Hello, world!')
# >```
# 
# Next, try this three-liner:
# 
# >```python
# >for i in range(10):
# >    print('Hello, world!')
# >    time.sleep(1)
# >```
# 
# ZONK!  That *shouldn't* work for you!  Can you fix it by importing the `time` module?
# 
# ***
# 
# Before we move on to uploading programs to the microcontroller, let's take a look at the built-in accessories that our board knows about.  We can do this by importing the `board` module.  Paste the following two lines in the CLI:
# 
# >```python
# >import board
# >dir(board)
# >```

# ***
# 
# Now let's move onto some microcontroller-specific uses.  For each block of code below, enter the code into the `Mu` editor.  Save the code and then copy it to the IB as `code.py`.  You may need to reset the Serial monitor or the board to get the code to run.  Don't forget to check the Serial monitor for errors (or you can use the "Check" feature in `Mu` before transferring your code).
# 
# One of the output components that is built into your ItsyBitsy is an LED.  The program below initializes the LED and then flashes it at a constant rate using an indefinite loop.  Note that the condition of the `while` loop is "True"... which is *always* true, so this loop will run forever (or until you power off the board).

# >```python
# >import board
# >import digitalio
# >import time
# >
# >led = digitalio.DigitalInOut(board.LED)
# >led.direction = digitalio.Direction.OUTPUT
# >
# >while True:
# >    led.value = True
# >    print(led.value)
# >    time.sleep(0.5)
# >    led.value = False
# >    print(led.value)
# >    time.sleep(0.5)
# >```

# ***
# 
# This next program from Kattni Rembor accesses the on-board neopixel, a sophisticated (and very bright) RGB LED.  The neopixel is actually three LEDs in one package, but the `neopixel` module provides some handy ways to access and control it.
# 
# >```python
# ># SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
# ># SPDX-License-Identifier: MIT
# >"""CircuitPython status NeoPixel red, green, blue example."""
# >import time
# >import board
# >import neopixel
# >
# >pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
# >
# >pixel.brightness = 0.3
# >
# >while True:
# >    pixel.fill((255, 0, 0))
# >    time.sleep(0.5)
# >    pixel.fill((0, 255, 0))
# >    time.sleep(0.5)
# >    pixel.fill((0, 0, 255))
# >    time.sleep(0.5)
# >```

# ***
# 
# The previous programs were examples of generating output (albeit not very rich output).  This last example program demonstrates how the board can read analog input. The ItsyBitsy uses a 16-bit Analog-to-Digital-Converter (ADC) to read an analog voltage on one of its input pins anc convert it to a digital value between $0$ and $2^{16}-1 = 65535$.  Your instructor will show you how to wire a potentiometer to one of the analog input pins on your board.  The block of code below will read the analog voltage on this pin and print the digital value to screen four times per second.
# 
# >```python
# >import time
# >import board
# >from analogio 
# >import AnalogIn
# >
# >analog_in = AnalogIn(board.A1)
# >
# >while True:
# >    print(analog_in.value)
# >    time.sleep(0.25)
# >```

# ***
# 
# ## In-class problems 
# 
# The excercises below will require you to do some light electronics work.  Your instructor will provide you with the necessary components, but you should probably do your work in the lab in case you have questions about wiring.  Please complete one of the following problems.  You may work with a partner.
# 
# ### Regulars
# 
# 1. Wire a 10-k$\Omega$ potentiometer so that its outer legs jumper $5$~V and ground pins of the ItsyBitsy, and its center leg connects to one of the board's analog input pins.  Write a program that fades the NeoPixel from red to green based on the voltage from the center pin of the potentiometer.
# 1. Wire a 10k-$\Omega$ potentiometer so that its outer legs jumper $5$~V and ground pins of the ItsyBitsy, and its center leg connects to one of the board's analog input pins. Connect an LED on one of the digital output pins.  Flash the LED on/off with a frequency controlled by the center pin of the potentiometer.
# 
