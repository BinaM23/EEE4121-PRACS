#!/usr/bin/python

# EEE4121F-B Lab 2
# SDN

# Implementing a Layer-2 Firewall using POX and Mininet


from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.clean import cleanup
import time

def treeTopo():
    net = Mininet( controller=RemoteController )
    net.addController('c0') #adds controller

    h1=net.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
    h2=net.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
    h3=net.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')
    h4=net.addHost('h4', ip='10.0.0.4', mac='00:00:00:00:00:04')
    h5=net.addHost('h5', ip='10.0.0.5', mac='00:00:00:00:00:05')
    h6=net.addHost('h6', ip='10.0.0.6', mac='00:00:00:00:00:06')
    h7=net.addHost('h7', ip='10.0.0.7', mac='00:00:00:00:00:07')
    h8=net.addHost('h8', ip='10.0.0.8', mac='00:00:00:00:00:08')

    s1=net.addSwitch('s1')
    s2=net.addSwitch('s2')
    s3=net.addSwitch('s3')
    s4=net.addSwitch('s4') 
    s5=net.addSwitch('s5')
    s6=net.addSwitch('s6')
    s7=net.addSwitch('s7')

    #links between switches
    #root=s1 #root of tree
    #l1=[s2,s5] #2nd level of tree
    #l2=[s3,s4,s6,s7] #3rd layer of tree

    #for i,layer in enumerate(l1):
    #    net.addLink(root,layer)
    #    net.addLink(layer,l2[2*i])
    #    net.addLink(layer,l2[2*i+1])

    #links between switches
    net.addLink(s1,s2)
    net.addLink(s1,s5)
    net.addLink(s2,s3)
    net.addLink(s2,s4)
    net.addLink(s5,s6)
    net.addLink(s5,s7)

    #links between hosts and switches
    net.addLink(h1,s3)
    net.addLink(h2,s3)

    net.addLink(h3,s4)
    net.addLink(h4,s4)

    net.addLink(h5,s6)
    net.addLink(h6,s6)

    net.addLink(h7,s7)
    net.addLink(h8,s7)

    info('*** network started \n') #user feedback
    net.start()

    
    CLI(net)  #comment out on final submission 
    net.pingAll()  #can comment out and do it manually
    info('*** shutting down \n')
    net.stop()

    time.sleep(10) 
    cleanup()

if __name__ == '__main__':
    setLogLevel( 'info' )
    treeTopo()
