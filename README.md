# EEE4121 TCP lab 1

## Initial setup

It is assumed the code will be run on a VM or PC with mininet and the appropriate python modules installed

Before running the experiments, create a folder to store the resulting .txt files and plots. This directory should be in the same folder as the tcp.py, Run.sh and other mininet files. For example, the output directory is named outputs in the Run.sh file, but this can be changed to the name of the directory used for storing output. Specify the paths if any files are in different directories when writing commands on the terminal.

## Experiments setup
Assuming output directory has been created:

run the command `sudo mn -c` to clear the network before running each experiment on the terminal.
To run an experiment run the command `sudo ./Run.sh` on the terminal.

## Experiments
The default congestion control used is TCP reno, to use TCP BBR or TCP Cubic, change the name of the congestion control in the `cong` variable in the `Run.sh` file to either `cong=bbr` or `cong=cubic` to use the other congestion controls.

To change network characteristics or the experiment run time just change the value of the appropriate variables in the `Run.sh` file e.g. `bwNet=3` and `time=10` changes network link rate to 3Mbps and experiment run time to 10s

### Experiment 1: Host_bw = 1Gbps and maxq=100
In the `Run.sh` file ensure the variable `bwHost` is equal to 1000 and `maxq` is equal to 100. Then change the value of `cong` to "reno","bbr" or "cubic" to use the desired congestion control.

0. make the above changes to the `Run.sh` file, save and then run `sudo mn -c`

1. run the command `sudo ./Run.sh`

2. let program execute then go to results directory `cd path/to/resultsDirectory`

3. view the plots using any image viewer such as fim e.g. `fim ping.png` and view .txt files using any text editor e.g. `joe q.txt`

4. move results if necessary then repeat steps 0 to 3 using a different congestion control

NB: the average fetch time and standard deviation are shown on the terminal after the program is run, the times are in seconds(s)

NB: running the `Run.sh` file repeatedly will overwrite whatever results are in the output directory. Therefore ensure the results of each experiment are stored separately or move output to a different directory before doing another experiment.

### Experiment 2: Host_bw = 1Gbps and maxq=20
repeat the same steps as experiment 1 but change `maxq` to 20

### Experiment 3: Host_bw = 100Mbps and maxq=100
repeat the same steps as experiment 1 but change `bwHost` to 100
