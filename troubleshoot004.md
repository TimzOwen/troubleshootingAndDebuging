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


### Managing our Time

#### Getting to important tasks

Create a task board for urgent/not urgent & important/not important

Technical debt-->pending work that accumulates when we choose a quick-and-easy
                 solution instead of applying a sustainable long-term one


#### prioritizing tasks

1. make a list of all tasks that needs to be done
2. Check the real urgency of a task
3. Asses the points of each importance of each issue
4. How much effort it will take


#### Estimating the time tasks will take

Compare tasks at hand and similar tasks done before

split large tasks into smaller tasks and do the comparison

include integration time for the split projects

#### communicating expectations

understand users implicit expectations on how long it takes to fix a problem

update a user on critical issues and when it will be resolved

update users on their expected issue or use issue tracking system

[Making the best of our time](https://blog.rescuetime.com/how-to-prioritize/)


### Making our future lives easier

#### Dealing with Hard Problems

Brian Kernighan-->Unix OS Contributor and author of C - programming
    "Debugging is twice hard as writing the software in the first place"

Build simple and easy application to understand

Develop code in small digestible chunks

keep your goal clear -->write test before actual code

Document your code and

ask for help and explain the problem

#### proactive best practices

1. Dealing with bugs

2. Test changes in advance

3. make sure your code has good unit test and integration tests

4. Have a test environment for testing before deploying to users

5. Deploy softwares in phases/canaries if possible

6. set up additional infrastructure

7. include good debugging logs

8. have centralized logs collection

9. Ticketing systems

10. write documentation

11. have playbooks-->accumulated solved solutions for all to reference
