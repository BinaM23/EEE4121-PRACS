# EEE4121 TCP lab 1

##initial setup
It is assumed the code will be run on a VM or PC with mininet and the appropriate python modules installed
Before running the experiments, you must create a folder to store the resulting .txt files and plots. This directory should be in the same folder as the tcp.py and other .py files. For demonstration the output directory is named outputs in the run.sh file, but this can be changed to the name of the directory you will use for outputs.
Ensure all files that need to be executed including the run.sh file are in the same directory else specify the path when you invoke commands on the terminal

##Experiments setup
Assuming output directory has been created:
run the command 'sudo mn -c' to clear the network before running each experiment on the terminal
To run an experiment run the command 'sudo ./run.sh' on the terminal

##Experiments
The default congestion control used is TCP reno, to use TCP BBR or TCP Cubic, change the name of the congestion control in the 'cong' variable in the 'run.sh' file to either 'cong=bbr' or 'cong=cubic'

To change network characteristics or experiment run time just change the value of the appropriate variables in the 'run.sh' file e.g. 'bwNet=3 ' and 'time=10' changes network link rate to 3Mbps and experiment run time to 10s

###Experiment 1: Host_bw = 1Gbps and maxq=100
In the 'run.sh' file ensure the variable 'bwHost' is equal to 1000 and 'maxq' is equal to 100. Then change the value of 'cong' to "reno","bbr" or "cubic" to use the desired congestion control.

run the command 'sudo ./run.sh'

To view results 'cd path/to/resultsDirectory'
then view the plots using any image viewer such as fim e.g. 'fim ping.png'

Note: the average fetch time and standard deviation are shown on the terminal after the program is run. the times are in seconds(s)
Note: running the 'run.sh' file successively will overwrite whatever results are in the output directory. Therefore ensure results of each experiment are stored separately or move output to a different directory before running an experiment again.

###Experiment 2: Host_bw = 1Gbps and maxq=20
repeat the same steps as experiment 1 but change 'maxq' to 20

###Experiment 3: Host_bw = 100Mbps and maxq=100
repeat the same steps as experiment 1 but change 'bwHost' to 100
