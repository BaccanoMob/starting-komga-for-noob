# Autostart komga easy way

Once everything is set up and working. 

First find the location of 'startkomga.sh'. You can find out by right-click -> properties -> Location and copy that. Ideally it should look something like

`/home/YOURUSERNAME/.../komga`

Open terminal and run `sudo crontab -e`. Then type `1` and enter.

IMPORTANT NOTE: DO NOT type 2 or 3 by accident and enter (not gonna lie I was tempted), you CAN NOT CHANGE after choosing. (Im a noob so I don't know how to change)

This should open a text editor like terminal window. Scroll down by down-click and type the following in a single line.
1. `@reboot `
2. Paste the location we copied
3. Continuing the line typing `/startkomga.sh`

So it should look something like this at the end (Obviously without the ..., saying just in case)
`@reboot /home/YOURUSERNAME/.../komga/startkomga.sh`

If you reboot or whenever you turn on the Linux device it will automatically start.

IMPORTANT NOTE: Not sure of other device, my raspberry pi takes around 2.5 minutes from switching on to getting 'localhost:8080' to work. Maybe it will be faster with other device but hope you all wait for a few minutes before declaring its not working.

# Stopping the madness of autostart

Open terminal and run `sudo crontab -e`.

Scroll down by down-click and add `#` in the beginning of `@reboot ...` line or delete the line.
