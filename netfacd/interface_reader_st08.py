#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())
for i in netifaces.interfaces():
    print(netifaces.ifaddresses(i))

