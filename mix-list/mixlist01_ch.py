#!/usr/bin/env python3

# display only the IP addresses to the screen.
iplist=[5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# display 1 - use "+" to string ip addresses
print("IP addresses: " + iplist[3] + " and " + iplist[4])

# display 2 - comma separator
print("IP addresses:",iplist[3],"and", iplist[4])

# display 3 - 'f-string'
print(f"IP addresses: {iplist[3]} and {iplist[4]}")

# Show which solution I like best
print("I like Display 1 best")
