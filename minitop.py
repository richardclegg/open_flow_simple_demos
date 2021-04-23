#!/usr/bin/env python

# This code creates a topology in mininet. 
# To run it try 

from mininet.topo import Topo

class CPTopology( Topo ):
    "Simple topology example for computerphile"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )


topos = { 'CPtopology': ( lambda: CPTopology() ) }
