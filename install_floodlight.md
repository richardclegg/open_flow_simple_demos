
### Install floodlight 

Honestly floodlight is a little bit of a nuisance to install right now as it is a little old and is choosy about what version of Java it installs with.

### Installing Floodlight VM

One easy to do this currently (April 2021) is using a VM. You will only get floodlight v1.2 though. However you will get mininet also installed.
You will need to install virtualbox. On Ubuntu
    sudo apt install virtualbox virtualbox-ext-pack virgualbox-guest-dkms

- Start virtualbox and find a VM here: http://opennetlinux.org/binaries/floodlight-vm.zip
- Unzip that to get a file Floodlight-v1.1+Mininet.vmdk
- Start virtualboxmanager and add the .vmdk file as a new machine (you probably want to up the memory a bit and devote a few CPUS to make it usable and guest additions to get the graphics settings right) See https://techathlon.com/how-to-run-a-vmdk-file-in-oracle-virtualbox/

Start the vm - it has a batman themed desktop. Within this open a terminal and type

    cd ~/floodlight
    git pull origin v1.2
    git submodule init
    git submodule update
    ant
    
This will take some time to build then

    java -jar target/floodlight.jar
    
It should start a floodlight controller. You can stop it with Ctrl-C or check it by browsing on firefox within the VM to: http://127.0.0.1:8080/ui/index.html

### Installing floodlight without using a VM

So floodlight master version will only install using jdk1.8 from oracle (not the open jdk version -- I don't know why). To get this you must sign up for an oracle account, download and install this version. This is honestly a complete nuisance to do and the steps will vary wildly on your system. On mine I untarred a repository in /usr/java/jdk1.8.0_291 then set java and javac using update alternatives and finally 

    export JAVA_HOME=/usr/java/jdk1.8.0_291/jre/       
If you have it right you should see something like

    java -version
    java version "1.8.0_291"
    Java(TM) SE Runtime Environment (build 1.8.0_291-b10)
    Java HotSpot(TM) 64-Bit Server VM (build 25.291-b10, mixed mode)

And similar for 

    javac -version
    
After all that you can do
    
    git clone git@github.com:floodlight/floodlight.git
    cd floodlight
    git pull origin master
    git submodule init
    git submodule update
    mvn package -DskipTests

Honestly though it is actually quite a struggle to get it to work. After all this
   
    java -jar target/floodlight.jar

You can then go with a browser to http://127.0.0.1:8080/ui/pages/index.html
