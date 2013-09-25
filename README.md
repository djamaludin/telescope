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

2. Edit telescope_server.py file with configuration settings
    * Set dir_dec to the directory path of decrypted photos (motion output directory)
    * Set dir_enc to the directory path of encrypted photos
    * Set encryption_key to the GPG public key fingerprint
    * Set the dropbox_upload to the path to dropbox_uploader.sh script

    An example of the configuration header is below:
    $ # Configuration Settings
    $ dir_dec = "/home/pi/telescope/photos/" # Directory of decrypted photos
    $ dir_enc = "/home/pi/telescope/photos_enc/" # Directory of encrypted photos
    $ encryption_key = "012345678" # GPG Public Key Fingerpring
    $ dropbox_upload = "/home/pi/telescope/dropbox_uploader.sh" # Path to dropbox_uploader.sh

3. Run dropbox_uploader.sh and follow instructions to configure access to Dropbox.

4. Edit start_motion.bash to add the location of the motion configuration file

    An example of this is:
    $ motion -c /home/pi/telescope/configuration/motion_640x480.conf

5. Change permissions of telescope directory to local user (where [user] is your local user).

    $ sudo chown -R [user]:[user] /home/[user]/telescope/

6. Make telescope_server.py, start_motion.bash, start_telescope_server.bash executable

    $ chmod +x telescope_server.py
    $ chmod +x start_motion.bash
    $ chmod +x start_telescope_server.bash

7. As local user, add to crontab using:

    $ crontab -e

    the following:

    $ @reboot [path to start_telescope_server.bash]
    $ @reboot [path to start_motion.bash]

    This automatically starts the telescope server and motion when the Raspberry Pi is booted.

Notes:

    * The GPG public key should reside in .gpg in the home directory of the user. 
    * Future versions of telescope should allow you to configure a custom gpg directory.
    * Also note that the dropbox-uploader.sh script is only required for use on a Raspberry Pi as there is no native 
Dropbox client. On x86 or x86-64 computers, you can use the native client and set the dir_enc setting to a folder in the Dropbox.



## Client Installation and Setup ##
The client can be any device capable of pulling files from Dropbox.
The proof-of-concept system was a Linux laptop running a native Dropbox 
client.

1. Download telescope_client.py, start_telescope_client.bash 
into chosen telescope directory.

2. Edit telescope_client.py file with configuration settings
    * Set dir_dec to the path of decrypted photos
    * Set dir_enc to the path of encrypted photos
    * Set encryption_key to the GPG public key fingerprint

    An example of the configuration header is below:

    $ # Configuration Settings
    $ dir_dec = "/home/pi/telescope/photos/" # Directory of decrypted photos
    $ dir_enc = "/home/pi/telescope/photos_enc/" # Directory of encrypted photos
    $ encryption_key = "012345678" # GPG Public Key Fingerpring

3. Change permissions of telescope directory to the local user (where [user] is your local user).

    $ sudo chown -R [user]:[user] /home/[user]/telescope/

4. Make telescope_client.py, start_telescope_client.bash executable

    $ chmod +x telescope_client.py
    $ chmod +x start_telescope_client.bash

5. Run telescope_client.py to decrypt files from Dropbox. Or if you used a GPG Private Key without a password, you can do the next step to provide auto decryption of photos.

6. (Optional) As local user, add to crontab using:

    $ crontab -e

    the following:

    $ @reboot [path to start_telescope_client.bash]

    This automatically starts the telescope client when the client is booted and allows for auto decryption of photos.

## Future Work ##
1. Allow custom GPG directories to be configured.
2. Allow different cloud backup services or servers to be configured.
3. Provide an easier installation mechanism.


## License ##
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

