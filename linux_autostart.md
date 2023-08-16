# Autostart komga easy way

Once everything is set up and working. 

First find the location of 'startkomga.sh'. You can find out by right-click -> properties -> Location and copy that. Ideally it should look something like

`/home/YOURUSERNAME/.../komga`

Open terminal and run `cd /etc/systemd/system`. This should move directories to the location where we will setup the autostart service

Write `sudo nano komga.service` and press enter. This should open a text editor like terminal window. Write the following 
```
[Unit]
Description=Komga
After=network-online.target

[Service]
ExecStart=/usr/bin/java -jar /home/YOURUSERNAME/.../komga/komga.jar
WorkingDirectory=/home/YOURUSERNAME/.../komga
Type=simple
Restart=always
User=YOURUSERNAME

[Install]
WantedBy=multi-user.target
```
Description can be changed to whatever it is to your liking but remember the path should be as in your device (that is for these `/home/YOURUSERNAME/.../komga/`) and also replace the USERNAME with yours.

Press ctrl + S and ctrl + X to save and exit the text editor

Finally type the following command to enable the service

`sudo systemctl enable komga.service`

Either reboot or run `sudo systemctl start komga.service` immediately.

If you reboot or whenever you turn on the Linux device it will automatically start.

IMPORTANT NOTE: Not sure of other device, my raspberry pi takes around 2.5 minutes from switching on to getting 'localhost:8080' to work. Maybe it will be faster with other device but hope you all wait for a few minutes before declaring its not working.

# Stopping the madness of autostart

Open terminal and run `sudo systemctl disable komga.service`. Alternatively, you can use `sudo systemctl stop komga.service` but this will stop while the system is running, that is, reboot will auto start as usual.
