#!/usr/bin/python3
#
# telescope_server.py - Telescope Server.
# Copyright (C) 2012, 2013,  C.I.Djamaludin.
#
# This file is part of Telescope.
#
# Telescope is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Telescope is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os


# Configuration Settings
dir_dec = "/home/pi/telescope/photos/" # Directory of decrypted photos
dir_enc = "/home/pi/telescope/photos_encrypted/" # Directory of encrypted photos
encryption_key = "[Key Fingerprint]" # GPG Public Key Fingerpring
dropbox_upload = "/home/pi/telescope/dropbox_uploader.sh" # Path to dropbox_uploader.sh

# Get file lists for photos and photos_encrypted directories
file_list = os.listdir(dir_dec)
file_list_enc = os.listdir(dir_enc)

# Extract Un-encrypted filename
counter = 0
while counter < len(file_list_enc):
    file_list_enc[counter] = os.path.splitext(file_list_enc[counter])[0]
    counter += 1

# Difference in files between telescope_photos and telescope_photos_enc directories
file_list_diff = list(set(file_list) - set(file_list_enc))


if len(file_list_diff) > 0: # If there's a new file to be encrypted and uploaded
    counter = 0
    while counter < len(file_list_diff): # For each new file to be encrypted and uploaded
        # Construct Encryption Command
        full_filename = dir_dec + file_list_diff[counter] # Full Filename (Unencrypted)
        full_filename_enc = dir_enc + file_list_diff[counter] + ".gpg" # Full Filename (Encrypted)
        encrypt_command = "gpg -e -r " + encryption_key + " --trust-model always -o " + full_filename_enc + " " + full_filename
        # Do Encryption
        os.system(encrypt_command)
        # Construct Upload to Dropbox Command
        upload_command = dropbox_upload + " upload " + full_filename_enc
        # Do Upload
        os.system(upload_command)
        counter += 1


