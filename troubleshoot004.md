## Managing Computer Resources


#### Memory Leaks and prevention

This is when a chunk of memory no longer needed os not released

Garbage collector-->in charge of freeing memory no longer in use

Memory profiler-->Figure out how memory is being used

#### Disk space

Needed for :

    Data stored by application

    Installed binaries and libraries

    cache information

    logs

    Temporary files

    backups

sudo lsof | grep deleted   -------->List all current open files and check the condition


#### Network saturation

Factors determining data access over a network

    Latency-->Delay between sending a byte of data from one point and receiving it on another

    Bandwith-->how much data can be sent or received in a second

iftop-->cmd to check which program is using alot of data

Traffic shaping-->marking data packets sent over a network with different priorities
                to avoid huge chunks of data use all of the bandwidth


#### Dealing with memory leaks

Use a terminal called uxterm to check misbehavior of an app

scroll buffer--->configured with the terminal to allows qick view of the last commands

use top--->to check memory usage

use memory profiler to check specific programs memory usage and control

Decorator--->Add extra behavior to functions without having to modify the code

##### Managing Resources

[Python concurrency](https://realpython.com/python-concurrency/)

[Threaded Asynchronous](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)

[Pluralsight Memory usage](https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python)

[Troubleshooting network problems](https://www.linuxjournal.com/content/troubleshooting-network-problems)
