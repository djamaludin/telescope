#!/usr/bin/python3
#
# telescope_client.py - Telescope Client.
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
dir_dec = "/path/to/directory/of/decrypted/photos/" # Directory of decrypted photos
dir_enc = "/path/to/Dropbox/directory/" # Dropbox directory of encrypted photos
encryption_key = "[Key Fingerprint]" # GPG Public Key Fingerpring

# Get file lists for photos and photos_encrypted directories
file_list = os.listdir(dir_dec)
file_list_enc = os.listdir(dir_enc)

# Extract Un-encrypted filename
counter = 0
while counter < len(file_list_enc):
    file_list_enc[counter] = os.path.splitext(file_list_enc[counter])[0]
    counter += 1

# Difference in files between photos and photos_encrypted directories
file_list_diff = list(set(file_list_enc) - set(file_list))


if len(file_list_diff) > 0: # If there's a new file to be decrypted
    counter = 0
    while counter < len(file_list_diff): # For each new file to be decrypted
        # Construct Decryption Command
        full_filename = dir_dec + file_list_diff[counter] # Full Filename (Unencrypted)
        full_filename_enc = dir_enc + file_list_diff[counter] + ".gpg" # Full Filename (Encrypted)
        decrypt_command = "gpg -d -o" + full_filename + " " + full_filename_enc
        # Do Decryption
        os.system(decrypt_command)
        counter += 1


