
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
