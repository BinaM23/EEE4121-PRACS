#!/bin/bash

# Note: Mininet must be run as root.  So invoke this shell script
# using sudo.

#loads the 2 python modules l2 learning and firewall.py into the OF controller
echo "setting up controller and firewall"
~/pox/pox.py forwarding.l2_learning misc.firewall &

echo "creating network in other window"
gnome-terminal -- python sdn.py

echo "finished"
