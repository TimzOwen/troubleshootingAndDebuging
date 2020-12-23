
## Crashing Programs

#### Systems that Crash

Reduce the scope

Check RAM and Hard disk

    use memtest86 tool and run on Boot

    check also on sensor data provided by OS

    Always Review logs before anything else

#### Understanding Applications that crash

Looking at log files(have date and time of occurrence)

    syslog file for Linux Os

    console app for Mac Os

    Event viewer on Window OS

to use debug logging enable it from setting

#### check whats going on  in a PC program ro rule down a problem

Linux --> strace

windows --> Process Monitor

Mac Os -->dtruss

also check for version update for bugs in the new version of the app

always narrow your reproduction case

#### when you can't fix a problem/Program;

use wrapper:

    function/program that provides a compatibility layer between two functions/programs so that they can work well together

Deploy watchdog:
    a process that checks whether a program is running and when its not ,starts the program again

Container:
    Allows application to run in its own environment without affecting the rest of the system

write scripts that pre-format to the s/w issue


#### Internal server error

check web sever and connect to it

    ssh webserver

    date --->check date

    cd /var/log/ --->navigate to the logs directory

    /var/log$ ls-lt | head ---->hook the logs and print the first head last modification

    tail syslog----------->check logs form the tail

    sudo netstat -nlp | grep :80 -->find all s/w listening to port 80, use netstat to give network info connection
                                ---> and append flag p-pid,l-check sockets at port 80

    ls -l /etc/nginx/------->check for configuration files

    ls -l /etc/nginx/sites-enabled/--->check for config specific to nginx

#### Understanding crashes

[Most likely reasons why a computer will crash](https://www.scientificamerican.com/article/why-do-computers-crash/)

[The blue screen of death PC Failure](https://en.wikipedia.org/wiki/Blue_Screen_of_Death)

[Understanding Logs on windows OS ](https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/)

[Get geeky with systems Logs in Mac OS](https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/)

[Check system logs in Linux OS ](https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm)

#### diagnose os Problems

[Windows Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)

[strace Linux ](https://www.howtoforge.com/linux-strace-command/)

[Trace system calls Mac Os](https://etcnotes.com/posts/system-call/)


### Code that crashes


#### Accessing invalid memory

This means a process tried to access a portion os the system's memory that wasn't assigned to it.

pointers----> Variables that store memory addresses

Always attach debuggers to the apps for easy logging

give debugging symbols---include additional info for debugging

Microsoft compilers can generate debuggers  PDB

undefined behavior--> Code doing something that is not valid in programming language

Valgrind-->powerful tool that tell us if the code is doing any invalid operations no matter if it crashes or not
            availbale in linux and Mac

Dr.Memory---used in both Windows and Linux

#### Unhandled Errors and Exceptions

Traceback-->Shows the lines of the different functions that were being executed when the problem happened

use Logging module to handle the way you want the code to appear

use print debugging to display the message error to the screen

The logging modules: -->sets debug message to show up when the code fails

#### Fixing someone else's code

Make sure your code is well documented with comments in it.

write unit Test to check what the code is supposed to do

#### Debugging a segmentation fault

Core Files:

    store all info related to the crash so that we can debug what's going on

    ulimit -c unlimited ---->generate the core files

    ls -l core fileTodebug ----> shows when the file crashed and the necessary details of the bug

    gdb -c core fileToCheck-----> pass the gdb debuger

    backtrace--->check the line that caused the error
            ----->The backtrace command can be used to show a summary of the function calls that were used to the point where the failure occurs.

    size--------> Get to the function that caused the crash

    list----> show the entire function that caused the

    off-by-one-error------->Most common Null point exception



