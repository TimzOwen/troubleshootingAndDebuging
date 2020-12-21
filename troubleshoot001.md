
### Introduction to debugging

Troubleshooting:

    The process of identifying, analyzing, and solving a problem

Debugging:

    the process of identifying, analyzing, and removing bugs in a system

#### debugging tools

Tools for debugging a network:

    tcpdump
    
    wireshark

Types and number of resources used in a system
    ps

    top

    free

check systems calls made by a program

    strace

    ltrace-->library calls made by a s/w

#### steps to solving a problem

reproduction case:-->clear desc of how and when the problem appear

system calls-->calls that the programs running on your computer make to the running kernel

    1. Getting information

    2. Finding the root cause of the problem

    3. Perform the necessary remediation

    strace -o : -->store the output into a file

    strace -o failure.strace

    less strace.failure

#### Understanding the problem

To solve a problem from the user:

    1->What were you trying to do

    2->What did you follow

    3->what was the expected Result

    4->what was the actual result
    

Reproduction case:--> Verifying if the problem exist or not

Heisenbug: --> The observe effect

Viewing logs:

    Windows-->use Event Viewer

    Mac OS-->/Library/Logs

    Linux-->/var/log/syslog.xsession-errors

Check I/O that uses most processes

    iotop

    iostat

    vmstat

    ionice--->cmd to reduce i/o usage and distribute it to other services in the computer

    iftop--->check network over usage esp when backing up a server or data

    rsync---cmd used to backup data

        -bmwlimit---traffic for bandwidth reduction

    Trickle-->program to limit bandwidth usage

    nice--->control power and CPU usage

Dealing with intermittent issues:

    make sure to log out debug messages to ease debugging process

Failing scripts:


### Binary search

uses the sub division rule to find and locate the problem

    the divide and locate rule (Base 2 binary search)

Git bisect: Allows trial for commits in division

Check for invalid data:

    cat file.csv | ./import.py --server tes ---> switch to another server

    wc -l ---> Counts the total number of lines in code/file

    tail -20 --->prints the last 20 lines

    head -15---->prints the first 15 lines
    
    head -50 contacts.csv | import.py --server test ---->Test the first half of the code and check for errors
