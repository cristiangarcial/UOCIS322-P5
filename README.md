# UOCIS322 - Project 4 #
Brevet time calculator.

## Overview

## Author: Cristian Garcia Leon, cgarcial@uoregon.edu ##

# Project Part 4
A website based on the RUSA algorithm for calculating open and close times
based on a milepost, called brevet distance, and control posts along the way.

My implementation of the algorithm shifts the output time by minutes per Ali's suggestion.

If the user inputs a control point of more than 120% of the brevet distance it will return -1.

First, we get the the offset for a particular brevet distance. We also need to subtract
the previous brevet distances so we don't do include the total distance for a particular section.

We use four tables for getting the time from the previous brevet sections and the minimum and maximum speed
for each section.

We then separate the offset by hour and minutes and then conver the hours to minutes and shift our starting time
and then return the output.

When I was doing testing, I notice that when the control distance and the brevet distance were the same at 200km and 400km my algorithm was off by 10min and 20min. That edge case is accounted for the in the code.


# Project Part 5
This project has been updated to include a submit and display button. When a user presses the submit button a message is displayed on the webpage notify the user that the data was submitted successfully. The distance in kms, the open, and close times are collected using the .each javascript function. Then that information is send with post to flask brevet.py. Then in flask brevet.py the information is loaded in and added to the database. When the user presses the diplay button, a new webpage is loaded and displays the information that was collected.
