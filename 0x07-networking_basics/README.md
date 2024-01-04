# 0x07. Networking basics #0

# Tasks

### 0-OSI_model
- How is the OSI model organized?
- 1    Alphabetically
- 2    From the lowest to the highest level
- 3    Randomly

### 1-types_of_network
* What type of network are Holberton iMacs connected to?
- 1    Internet
- 2    WAN
- 3    LAN

* What type of network could connect an office in one building to another office in a building a few streets away?
- 1    Internet
- 2    WAN
- 3    LAN

* What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?
- 1    Internet
- 2    WAN
- 3    LAN

### 2-MAC_and_IP_address
* What is a MAC address?
- 1    The name of a network interface
- 2    The unique identifier of a network interface
- 3    A network interface

* What is an IP address?
- 1    Is to devices connected to a network what postal address is to houses
- 2    The unique identifier of a network interface
- 3    Is a number that network devices use to connect to networks

### 3-UDP_and_TCP
* Which statement is correct for the TCP box:
- 1    It is a protocol that is transferring data in a slow way but surely
- 2    It is a protocol that is transferring data in a fast way and might loss data along in the process

* Which statement is correct for the UDP box:
- 1    It is a protocol that is transferring data in a slow way but surely
- 2    It is a protocol that is transferring data in a fast way and might loss data along in the process

* Which statement is correct for the TCP worker:
- 1    Have you received boxes x, y, z?
- 2    May I increase the rate at which I am sending you boxes?

### 4-TCP_and_UDP_ports
**Note that a specific IP + port = socket.**

* Write a Bash script that displays listening ports:
- 1    That only shows listening sockets
- 2    That shows the PID and name of the program to which each socket belongs

### 5-is_the_host_on_the_network
* Write a Bash script that pings an IP address passed as an argument.
- Accepts a string as an argument
-nDisplays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
- Ping the IP 5 times

It is interesting to look at the time value, which is the time that it took for the ICMP request to go to the 8.8.8.8 IP and come back to my host. The IP 8.8.8.8 is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.

Next time you feel that your connection is slow, try the ping command to see what is going on! 

---
