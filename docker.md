## Here lies on how to step up docker and komga 

### System update

Run `sudo apt update && sudo apt upgrade -y` to bring the system up to date. (Optional) reboot the system.

### Installing Docker
- Run `curl -sSL https://get.docker.com | sh` to install docker
- Run `sudo usermod -aG docker $USER` to add docker group to user so you do not have to use sudo to run docker commands.
- You need to logout/reboot for installation to take effect.

### Running Komga container
- Create a folder for komga (this is where komga will store the config, database, tmp, etc files/folders)
- In that folder create a file called `docker-compose.yml` and paste the below content in it.
  ```yml
  services:
  komga:
    image: gotson/komga:latest
    container_name: komga
    hostname: komga
    ports:
      - 25600:25600
    networks:
      - proxy
    restart: unless-stopped
    volumes:
      - /etc/timezone:/etc/timezone:ro
      - ./config:/config
      - ./tmp:/tmp
      - ${LIBRARY_HOST_DIR}:/library
  ```
- Replace `${LIBRARY_HOST_DIR}` to the full parent folder path of the comic/ebook library. For example, if the comic library is at `~/Downloads/my-library` then change that line as `/home/<YOUR_USERNAME>/Downloads/my-library:/library`.
- If you have multiple library, say, different folder for comic or ebook or for different genre, etc. Add new line with `/path/to/different-library:/diffrent-library` as full directory.
- Just make sure the left side is a full path to that directory and right side does not repeated (also its not config, tmp, app, bin, etc)
  - &#x2611;
    - `/home/<YOUR_USERNAME>/Downloads/library:/library`
    - `/home/<YOUR_USERNAME>/Downloads/new-library:/new-library`
  - &#x2612;
    - `/home/<YOUR_USERNAME>/Downloads/library:/library`
    - `/home/<YOUR_USERNAME>/Downloads/new-library:/library`
- Also if every library is under Downloads or any other folder, use that to folder to bind the volume. In the above example, it will `/home/<YOUR_USERNAME>/Downloads:/library`, You can access the folders inside Downloads inside library as well.
- The current folder structure of your komga will be
  ```
  komga/
  └── docker-compose.yml
  ```
- Open the terminal and change directory to the komga folder.
- Run `docker compose up -d`. This will pull/download the latest image of komga and starts the container.
- Once it starts you will see the folder structure is similar to as below
  ```
  komga/
  ├── docker-compose.yml
  ├── config/
  └── tmp/
  ```
- DO NOT DELETE THESE FOLDERS, if you do you will have to create a new account and set the library every single time.
- Check the logs by running `docker compose logs` (while in the komga directory). Usually it takes a couple of minutes to set up. Till then you'll get `404 not found` or `Bad Gateway` or something similar. 

### How to access komga

You can access the komga server via browser using the url `http://localhost:25600` or `http://IP_ADDRESS:25600` where IP_ADDRESS is the device's ip address in the network.

We can get the device's IP address using `ipconfig` in Windows' command prompt or `hostname -I` in Linux's terminal where the komga is run.

IMPORTANT NOTE: localhost is used if youre using komga from the device itself. ip address is needed when you try to access from a different PC/Laptop/Phone.

Possible stupid noob mistake: Make sure mobile phones are not running only in data and all devices are on the same wifi (I made this noob mistake multiple times). Also, no matter how fast 5G mobile data speed is, komga wont run unless connected to same wifi.

ANOTHER NOTE: IP address might change from time to time, it can be avoided by setting a static ip address.

And with this you can follow [Komga's official docs](https://komga.org/guides/libraries.html) from here on out on how to use komga.

Also wait for a few minutes on the first run for the server to initial set up, if komga is not running after a few minutes check the logs by running `docker compose logs` (while in the komga directory)

### Updating komga container
- Open terminal and change to the komga directory
- Run `docker compose down` to stop the running container
- Run `docker compose pull` to get the latest image of komga
- Once its completed, run `docker compose up -d`
- Then run `docker image prune -a` to delete the old image.

