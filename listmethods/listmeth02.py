#!/usr/bin/env python3
proto= ["ssh","http","https"]
protoa=["ssh","http","https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2=[22,80,443,53] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

print("This lists dogs sizes")
dogsize=["small","medium","large"]
dogsmall=["Yorkie","Chihuahua","Boston Terrier"]
dogmed=["JRT","Cocker Spaniel"]
doglrg=["Bulldog","Rottweiler","Husky"]
print(dogsize)
dogsize.append ("xl large") # this will add "xl large" to end of list
print(dogsize)
dogsize.insert(1,dogsmall) # this will insert small dog names after "small"
print(dogsize)


