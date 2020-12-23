
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

