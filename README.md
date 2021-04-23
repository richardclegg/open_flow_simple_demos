# How to get going.

This project should work on Linux or MacOS. I used Ubuntu 20.04 and provide some notes here. Note, this is certainly not intended as a working guide to installing an OpenFlow controller in a real production environment. This is about how to investigate it as a hobby or because you are interested in networking. Floodlight is not the most well maintained controller out there, I use it because I'm familiar with it even though it is very old now. Similarly I use pox here as a demo not because it is useful in a production environment. Opendaylight is more modern but more effort to set up.

1. [Install floodlight](install_floodlight.md) 
2. [Install mininet](install_mininet.md)
3. Install pox

This should be as simple as

    git clone http://github.com/noxrepo/pox

5. Clone this repository somewhere.

    git clone git@github.com:richardclegg/open_flow_simple_demos.git

If you are in the VM you will need to use instead  

    git clone https://github.com/richardclegg/open_flow_simple_demos.git 

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
    
should clean up anything that did not get properly cleaned in the exit process.


### Mininet toplogies

There are a few topology generators. A nice one I use in the video on Computerphile is "tree"

    sudo mn --topo tree,depth=3,fanout=2 

Warning, do not try this with too much depth and fanout. It gets big quickly.

You can also generate your topology programatically from python. An example is included in this repos if you have checked it out. Run

    sudo mn --custom minitop.py --topo CPtopology 

from a directory containing the file minitop.py (in this repos) will create the topology in the python file that I demonstrated in the Computerphile video.

### Starting a POX based openflow controller

Now to work with a POX based openflow controller. These are controllers "handcrafted" in python. 

Within the directory containing pox you can do 

    ./pox.py samples.pretty_log misc.of_tutorial

A stripped down version of the code I used in the video is in this repos. To run it copy it into the pox repository in pox/misc subdirectory. You could then do.

    ./pox.py samples.pretty_log misc.of_tutorial

This will start a controller on your localhost 127.0.0.1 listing on port 6633. You connect this to mininet with:

    sudo mn --topo tree,depth=3,fanout=2  --controller remote --switch ovsk
    
Note that this simple controller is a little old now and only works with openflow v1.2. You may see the pox controller throw some errors related to dns but you can also see now that in mininet you can do

    mininet> h1 ping h2
    
When you are finished shut down mininet and the pox controller. Don't forget to clear mininet with

    sudo mn -c
   
If you want to use the code I used in the computerphile video you would need to copy simplehub.py into the pox directory subdirectory pox/misc and run

    

### Working with floodlight

If you want to do the same with floodlight then in the directory you installed floodlight.

    java -jar target/floodlight.jar

In a browser window you should now be able to browse to http://127.0.0.1:8080/ui/pages/index.html
    
This will show you various bits of information about the floodlight controller.

Now if you set up mininet you should also tell it to use OpenFlow 1.3 so that floodlight can get controller information: You could try a simple tree

    sudo mn --topo tree,depth=3,fanout=4 --controller remote --switch ovsk,protocols=OpenFlow13

If you go to your web browser at http://127.0.0.1:8080/ui/pages/topology.html you should be able to see a nice tree topology. If you experiment you can get quite large topologies going. If you experiment with the code in minitop.py you can create your topology programatically.


    


