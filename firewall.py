
from asyncio import events
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
# TODO Add your imports here 

import csv

log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

#TODO Add your global variables here 
host_Addresses=[] #array of hosts to block using firewall

with open(policyFile) as csvFile:
    reader=csv.reader(csvFile) #file reader
    next(reader) #skips to row
    for row in reader: #loop over each row in file
        host_Addresses.append(row[1]) #get MAC addresses
csvFile.close()

#modify the number of hosts blocked can be changed around
host_Addresses2=host_Addresses[0:1] #can choose which hosts to block 

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        #TODO Add your logic here 
        for address in host_Addresses2:
            blocked=of.ofp_match()
            blocked.d1_src=EthAddr(address)
            ofFlow_mod=of.ofp_flow_mod()
            ofFlow_mod.match=blocked
            event.connection.send(ofFlow_mod)


        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    #    Starting the Firewall module
    
    core.registerNew(Firewall)
