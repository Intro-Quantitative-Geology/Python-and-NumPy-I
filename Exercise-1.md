# Laboratory exercise 1
In this first exercise, you should test your new knowledge of Python by performing the following tasks.

## Problem 1 - Volcano slicing
For this problem, we will use the volcano data file `Data/GVP-Volcano-Lat-Lon-Elev.csv`. As you may recall, this file contains the volcano ID number, latitude, longitude and elevation for Holocene volcanoes in the [Smithsonian Institution's volcano database](http://volcano.si.edu/). I would like you to analyze this file by calculating various values from the data file. Please copy and paste **ALL** of the commands you used to load in the data file and as well as your calculated values for the following.

1. What are the minimum and maximum latitudes for all volcanoes?
2. What is the average elevation for the first 50 volcanoes in the data file?
3. What is the standard deviation in elevation for the last 500 volcanoes in the data file?
4. What is the latitude, longitude and elevation of the volcano in the middle of the array of the data file?
5. What is the longitude of the last volcano in the data file? You will receive bonus points if you find a clever way of finding the last longitude in only one command.

**For this problem, please provide a copy of ALL commands used to load in the data file and as well as the calculated values.**

## Problem 2 - Plotting everything but the kitchen sinc (?)
For this exercise you need to produce a plot of the `sinc()` function from 0 to 8π, but you cannot use the `sinc()` function that is part of NumPy or the Python math library. Instead, calculate the sinc function is as the sin(π*x)/(π*x). This function is the continuous inverse Fourier transform of the rectangular pulse of width 2π and height 1.

1. You should create a 1-D array `x` that goes from 0 to 8π by increments of 0.1 and a variable `y` that is the `sinc(x)`.
2. Plot the values of `y` as a function of `x` with grid lines in the background of the plot (see `help(plt.grid)` for guidance), label the axes appropriately and give the plot a title.
3. In between commands, please provide comments describing the purpose of each line you have typed.

**For this problem, please submit a printout of ALL of the Python commands you entered and a copy of the plot that was generated.**

## Problem 3 - "Decoding" other people's code
We haven't written our own script files yet, but often it is easier to put a list of Python commands into a script file, rather than typing them all in separately in a terminal window. Typically, you also don't start writing a Python code from scratch when you want to do calculations and/or real science. Most of the time someone else has already written a code that is similar to what you want to do, and your goal is to modify the code to suit your needs. Step one is to figure out what the code is supposed to do before you start tinkering. For this exercise, take a look at the example Python script [Mohr-circle-D-P-2D.py](Source/Mohr-circle-D-P-2D.py) and save a copy in your `Lab-1` directory. If you navigate to the `Lab-1` directory, you can run the script by typing

```bash
$ ipython Mohr-circle-D-P-2D.py
```

Please run the code and answer the following questions:

1. What is the purpose of this code, what does it do, and does it appear to work properly?
2. What are the commands you recognize in the code?
3. What are the commands you do not recognize?
4. Are the comments sufficient for "decoding" this code as a new user? Why or why not?

**For this exercise, please submit a printout of your typed responses to the questions above.**

## What to submit
For each of the problems above, put the requested lists of commands, plots and/or answers into a Microsoft Word, OpenOffice or PDF document and submit it using the Exercise 1 submission link in Moodle.
