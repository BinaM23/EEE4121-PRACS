#!/bin/bash

set -e

echo "Start of experiment..."

#change these varibales to change network characteristics and experiment run time(default=30s)
time=30
bwHost=100 #change to 100 when repeating steps 8-10 i.e. step12
bwNet=2
delay=100 
dir=outputs #directory to store the .txt files and plots, must be made in same folder as tcp.py file
maxq=100 #change to 20 when repeating steps 8-10 i.e. step11
cong="bbr" #can change to bbr or cubic, default is reno

case "$cong" in 
	"cubic")
	python tcp.py --bw-host $bwHost --bw-net $bwNet --delay $delay --dir $dir --time $time --maxq 		$maxq --cong cubic  
	;;
	"bbr")
	python tcp.py --bw-host $bwHost --bw-net $bwNet --delay $delay --dir $dir --time $time --maxq 		$maxq --cong bbr --qman fq
	;;
	*) #TCPreno is done by default
	python tcp.py --bw-host $bwHost --bw-net $bwNet --delay $delay --dir $dir --time $time --maxq 		$maxq
	;;
esac

echo "Done"

echo "starting plots..."
python plot_queue.py -f $dir/q.txt -o $dir/queue.png #plots and data in outputs directory
echo "queue plot done, starting ping plot..."
python plot_ping.py -f $dir/ping.txt -o $dir/ping.png
echo "Done, results available in directory:${dir}"
