# How to get going.

This project should work on Linux or MacOS. I used Ubuntu 20.04 and provide some notes here. Note, this is certainly not intended as a working guide to installing an OpenFlow controller in a real production environment. This is about how to investigate it as a hobby or because you are interested in networking. Floodlight is not the most well maintained controller out there, I use it because I'm familiar with it. Opendaylight is more modern but a little more effort to set up.

1. [Install floodlight](install_floodlight.md) 
2. Clone this repos
3. Follow the commands given

### Installing Mininet

If you want to play with mininet separate to Floodlight then it is easy enough. On Ubuntu it is easy to configure this should be as simple as

    sudo apt install mininet

You can test it with:

    sudo mn

This should get you to a mininet prompt. You can test it with 

    h1 ping h2    

Ctrl-C will stop the ping. Ctrl-D will log you out.
  
## Working through examples

Clone this repository somewhere.

    git clone git@github.com:richardclegg/open_flow_simple_demos.git

If you are in the VM you will need to use instead  

    git clone https://github.com/richardclegg/open_flow_simple_demos.git 
