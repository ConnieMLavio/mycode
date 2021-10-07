#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    line_count = 0  # set counter to 0 to start counting
    for line in configlist:
        if line !="\n":
           line_count +=1

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("The number of lines in the file is: ", line_count)
## print(line_count)
