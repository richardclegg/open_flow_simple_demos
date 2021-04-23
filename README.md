# How to get going.

This project should work on Linux or MacOS. I used Ubuntu 20.04 and provide some notes here. Note, this is certainly not intended as a working guide to installing an OpenFlow controller in a real production environment. This is about how to investigate it as a hobby or because you are interested in networking. Floodlight is not the most well maintained controller out there, I use it because I'm familiar with it. Opendaylight is more modern but a little more effort to set up.

1. [Install floodlight](install_floodlight.md) 
2. [Install mininet](install_mininet.md)
3. [Install pox](install_pox.md)
4. Clone this repos

## Working with mininet

This is very simple. It must be run as root so typically you need sudo to get it to work

    sudo mn 

is enough to get you running. This sets up the simplest toplogogy two hosts h1,h2 connected via switch s1. You will now be at the mininet prompt

    mininet> h1 ping h2

will have host h1 ping host h2. In general typing a hostname and a command runs that command on that hostname e.g

    mininet> h1 ls

lists files from h1 (it will look the same from everywhere). There is a special command

    mininet> pingall
    
that makes every host contact every other host. Exit mininet with Ctrl-D. You usually should clean up afterwards just to be safe so 

    sudo mn -c
    
should clean up anythign that did not get properly cleaned in the exit process.


### Mininet toplogies

There are a few topology generators. A nice one I use in the video on Computerphile is "tree"

    sudo mn --topo tree,depth=3,fanout=2 

Warning, do not try this with too much depth and fanout. It gets big quickly.

You can also generate your topology programatically from python. An example is included in this repos if you have checked it out. Run

    sudo mn --custom minitop.py --topo CPtopology 

from a directory containing the file minitop.py (in this repos) will create the topology in the python file that I demonstrated in the Computerphile video.

### Starting a POX based openflow controller

Now to work with a POX based openflow controller. These are controllers "handcrafted" in python. 




