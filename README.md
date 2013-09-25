# telescope #

telescope is a proof-of-concept secure end-to-end encryption surveillance
camera utility. It runs on a Raspberry Pi, but can be used on any device 
that runs Linux. It relies on Motion to capture movement events and 
surveillance. The resulting photos are encrypted using a user generated 
public key (GnuPG backend) and uploaded to a cloud service provider such 
as Dropbox. Encryption of data at rest and data in motion is implemented.

## Requirements and Dependancies ##

telescope was designed for use on a Raspberry Pi, however it can run on any
embedded computer or computer capable or running Linux. The proof-of-concept
system utilised the following hardware and software:

Hardware
   * [Raspberry Pi Model B (512MB)](http://www.raspberrypi.org/)
   * [Power Adapter](http://elinux.org/RPi_VerifiedPeripherals#Power_adapters)
   * [SD Card](http://elinux.org/RPi_SD_cards)
   * [Compatible Webcam](http://elinux.org/RPi_USB_Webcams)
   * [Powered USB Hub (optional)](http://elinux.org/RPi_Powered_USB_Hubs)
   * [USB WIFI Adaptor (optional)](http://elinux.org/RPi_USB_Wi-Fi_Adapters)

Software
   * [Rasbian](http://www.raspberrypi.org/downloads/)
   * [Python](http://python.org) 3.2
   * [GnuPG](http://www.gnupg.org/)
   * [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome)
   * [inotify-tools](https://github.com/rvoicilas/inotify-tools)
   * [cURL](http://curl.haxx.se/)
   * [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader)

You can either use your OS package manager such as apt-get or aptitude to
install these packages.

    $ sudo apt-get install python3 gnupg motion inotify-tools curl

To get Dropbox-Uploader you can visit the repository or use wget.

    $ wget https://raw.github.com/andreafabrizi/Dropbox-Uploader/master/dropbox_uploader.sh


## Server Installation and Setup ##
1. Download telescope_server.py, start_motion.bash, start_telescope_server.bash
into chosen telescope directory.
