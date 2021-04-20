# How to get going.

This project should work on Linux or MacOS. I used Ubuntu 20.04 and provide some notes here. Note, this is certainly not intended as a working guide to installing an OpenFlow controller in a real production environment. This is about how to investigate it as a hobby or because you are interested in networking. Floodlight is not the most well maintained controller out there, I use it because I'm familiar with it.

1. Install Floodlight VM
2. Clone this repos
3. Follow the commands given

## Install software

### Installing Floodlight VM

The best way to do this currently (April 2021) is using a VM as the software is a little old and finicky to compile.
You will need to install virtualbox. On Ubuntu
  sudo apt install virtualbox virtualbox-ext-pack

Start virtualbox and find a VM here: http://opennetlinux.org/binaries/floodlight-vm.zip
Unzip that to get a file Floodlight-v1.1+Mininet.vmdk
Start virtualboxmanager and add the .vmdk file as a new machine (you probably want to up the memory a bit and devote a few CPUS to make it usable)
https://techathlon.com/how-to-run-a-vmdk-file-in-oracle-virtualbox/

Start the vm - it has a batman themed desktop. Within this open a terminal and type
  cd ~/floodlight
  git checkout v1.1
  git pull
  git submodule init
  git submodule update
  ant
This will take some time to build then
  java -jar target/floodlight.jar
  

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
