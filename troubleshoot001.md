
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
