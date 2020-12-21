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
