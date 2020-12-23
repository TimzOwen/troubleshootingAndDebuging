### Slowness in computing

Improve on Bottle neck

clear the processes and apps running in background and are not in use

check for usage in resources

    Linux OS:

        top

        iotop/iftop-->check s/ws using most resources

    Mac OS:

        Activity Monitor

    Windows:

        Resource Monitor

        performance Monitor

How Computers use Resources.

    store data in cache:-->Faster to retrieve the data

    web proxy---> store data in web for each access to avoid querying the internet each time

    DNS---> implement a local cache

    swap--->where data is stored by os when RAM is full and the data is not needed at the moment and put on the disk

    Memory leak----> state where memory not in use is not being released

#### possible causes of slowness.

slow when booting up

    reduce on start up programs

Large Files

    reduce the file sizes

use logging to log out

    Logrotate--->check for logs

Reboot


#### Diagnose web server to check why slow

Login

    check if its loading slowly

used cmd:

    ab -n 500 andela.com ---->do 500 request on andela website
    
connect to the web server

    ssh webserver---will ask for authentication

look for Top

    top

change preference

    nice--> start a priority0

    renice-->reoder a priority

use PID

    for pid in $(pidof ffmpeg); do renice 19 $pid done------->use for to script the automation


check all process

    ps ax | less   ---> check current processes running and join with less to enable scrolling
    
find unknown locaiton of file

    locate----> locate static/001

    killall -STOP ffmped(a runnig program during documenting the code)------>stop the process but not killing it

Run one process at a time:

    for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done ;done

#### Monitoring Tools

[System's internal](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)

[Linuxperf](http://www.brendangregg.com/linuxperf.html)

[bread egg use method](http://brendangregg.com/usemethod.html)

[Activity monitor in MAc](https://support.apple.com/en-us/HT201464)

[Monitor in Windows](https://www.windowscentral.com/how-use-performance-monitor-windows-10)

[How to use Resource monitor windows](https://www.digitalcitizen.life/how-use-resource-monitor-windows-7)

[System internals](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)

[Computer cache](https://en.wikipedia.org/wiki/Cache_(computing))

[Linux commands](https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/)


#### Writing efficient Code

use profiler:

    Tool that measures the resources that our code is using , giving us a better understanding of what's going on.

gprof---> used to analyze C programs
cProfile-->Analyze Python programs

Expensive action--->Tasks that take long to complete

#### using the right data structures
List--> sequence of elements
Dictionaries -->Store key values pair


#### Dealing with expensive Loops

Have to read your data first before looping to save on resources

always rem to break out of loops

#### Keeping local results

create a local cache to avoid getting data each and every time repetitively

create simple variables to make sure we don't keep operations that are not necessary

#### Dealing with slow scripts
check time execution:
    time ./scriptToBeChecked.py  "2020-01-20 |Example|test1"
    Real--->Amount of actual time it took to execute the command
    USer--->time spent doing operation in the user space
    Sys-->time spent doing system-level operations

Write out the output:
    pprofile -f callgrind -o profile.out ./scriptToBeChecked.py  "2020-01-20 |Example|test1"
checkout the ouput in GUI:
    kcachegrind profile.out

[Improve your Code](https://en.wikipedia.org/wiki/Profiling_(computer_programming))


#### parallelizing Operations

Threads---> Allows us to run multiple parallel tasks inside a process

#### slowly growing in complexity



CSV-->SQLite-->Database server-->Dynamic Cache infront of a server

varnish--->speed up the load of  web on request

Load balancer-->Distribute server among requests and service

#### Dealing with Complex system

Find a bottle neck causing your system to under perform

Have a good monitoring infrastructure


#### Using Threads to make things go Faster

Threads--->Makes things work faster

Executor--->Process in charge of Distributing the work among different workers

Future module-->provide a couple of different executors;one for using threads and another using processes

using processes always takes shorter time to execute than Threads because the CPU is well utilized

[Using Concurrency to utilize programs](https://realpython.com/python-concurrency/)

[Complex slow systems](https://realpython.com/python-concurrency/)

[Yielding more fast systems](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)


