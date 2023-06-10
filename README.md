# starting komga for noob so anyone can understand (hopefully)

I too struggled on how to start komga when I first found out about it. And prolly its still a struggle for many especially if they don't know what .jar file or any code related jargon is. I thought I'll make a guide of how I run komga right now so a noob can run it more easily than scream at the internet on how to start komga for days or maybe even years (I think couple of years for me).

## What to download

First you need the .jar file of the latest release from [Komga's github](https://github.com/gotson/komga). Then download the following to use the noob way.

### for Windows

Download the 'startkomga.exe' file from my [releases](https://github.com/BaccanoMob/starting-komga-for-noob/releases).

But if you want to show off you are a noob hacker to others and want the log console as well like below download 'startkomga_log.exe' version.

<img width="972" alt="image" src="https://github.com/BaccanoMob/komga-for-noob-setup/assets/82655889/5330bd12-436c-4a19-88bf-a08221b0160e">

I highly recommend using 'startkomga_log.exe' for the first time then switch over to the other version if needed so you'll be more aware if komga is running or not.

### for Linux

Download the 'startkomga.sh' file from my [releases](https://github.com/BaccanoMob/starting-komga-for-noob/releases).

This will prolly work for all versions including MacOS (but I don't have one to test it out so feel free to let me know by raising an issue). I'm a noob too so I'm not 100% sure but 99.9% yes it should work as long as shell scripts execute.

## Folder/file setup

Whether it is Windows or Linux, I first suggest you make a folder named 'Komga' or whatever name you like to have the .jar file and the .exe or .sh file in. This is done to make sure the .exe and .sh can locate the jar file more quicker without any errors. So folder structure should look somewhat like this.

<pre>
└── Komga
    ├── komga-x.y.z.jar
    ├── startkomga.exe/.sh
</pre>

### Some additional steps for linux

You might need to make the shell script executable by running the following command (but make sure you change the directory of the terminal usind `cd` command to the komga folder as mentioned above)

`chmod +x startkomga.sh`

or if you think using terminal is pro level then I got a noob version as well. 

Right-click the .sh file -> Properties -> Permissions -> Make sure execute is ticked or change it to anyone or something along those lines (These should be available for ubuntu or raspberry pi)

## Java installation

Java is needed to run jar files so you need to do this even though you are not going to code in java.

### for Windows

You download the installer from the [Oracle's official site](https://www.oracle.com/java/technologies/downloads/) and install Java.

### for Linux

run `sudo apt install default-jre` in terminal to install java using the terminal.

[OPTIONAL:] Run `java -version` in command prompt (for Windows) or terminal (for Linux) to verify if you ever feel in doubt. You need Java version 8+ (or 1.8+) to run Komga.

## How to run komga

### for Windows

Just double click the .exe and it should run as long the jar file is in the same folder. If you're going without log console you literally won't see what is happening so please be patient. If you ran with log console you'll see how it fast/slow it runs. I highly recommend using 'startkomga_log.exe' for the first time then switch over to the other version if you want to so you'll be more aware if komga is running or not.

### for Linux

Just double click the .sh and it should run as long the jar file is in the same folder. Executing in terminal should have log console and just execute will do it in background.

IMPORTANT NOTE: Depending on the system the start up time might vary. For example, it takes around 10 seconds to start the server in my windows PC but my Raspberry Pi takes around 1 minute to start manually or around 2 minutes if automatic. So make sure to wait for a few minutes before cursing me or komga isn't working and flipping over tables. Also lauching the first time might take slightly longer as komga needs to set things up for the first time not 100% sure.

## How to access komga

You can access the komga server via browser using the url `http://localhost:8080` or `http://IP_ADDRESS:8080` where IP_ADDRESS is the device's ip address in the network.

We can get the device's IP address using `ipconfig` in Windows' command prompt or `hostname -I` in Linux's terminal where the komga is run.

IMPORTANT NOTE: localhost is used if youre using komga from the device itself. ip address is needed when you try to access from a different PC/Laptop/Phone.

Possible stupid noob mistake: Make sure mobile phones are not running only in data and all devices are on the same wifi (I made this noob mistake multiple times). Also yes, no matter how fast 5G mobile data speed is, komga wont run unless connected to wifi.

ANOTHER NOTE: IP address might change from time to time, it can be avoided by setting a static ip address (yes, its dynamic by default.). If people need me to inlcude a guide it as well raise a issue. 

And with this you can follow [Komga's official docs](https://komga.org/guides/libraries.html) from here on out on how to use komga.

## How to update komga

Just replace the .jar file with the latest version. Make sure the old .jar file is deleted or removed from the folder and only one .jar file (the latest one) is present in folder. Also deleting .jar file does not delete komga content so do not worry about accidentally deleting something inside komga.

## How to run komga automatically on start up

Will add this soon after taking break

## Code related gibbirsh only for people who want to how this .exe or .sh works

The .exe the filename of the first .jar file in the same directory and runs the .jar file using java.

The .sh file first changes directory to Komga folder or whatever name you created and then finds & runs the .jar file using java

It is possible to run the .jar file with .bat files for windows (.bat files are Windows equivalent to .sh in Linux).

The content of .bat files for komga with log console

    start java -jar komga-X-Y-Z.jar

or without log console

    start javaw -jar komga-X-Y-Z.jar

Double clicking should work the same way as an .exe file would. But the annoying part is you can't pin .bat files to start menu and you have to specify the .jar file name so I made .exe files using python and pyinstaller to automate the process.
