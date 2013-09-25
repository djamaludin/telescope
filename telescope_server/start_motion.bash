#!/bin/bash
#
# start_motion.bash - Start Motion Process.
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


# Pick one configuration file

# Motion at a resolution of 480p
motion -c /home/pi/telescope/configuration/motion_640x480.conf

# Motion at a resolution of 720p
# motion -c /home/pi/telescope/configuration/motion_1280x720.conf

# Motion at a resolution of 1080p
# motion -c /home/pi/telescope/configuration/motion_1920x1080.conf

