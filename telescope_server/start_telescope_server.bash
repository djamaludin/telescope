#!/bin/bash
#
# start_telescope_server.bash - Bootstrap loader for telescope_server.py.
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


# Watch and wait for changes to snapshots directory
# while inotifywait -e create "/home/pi/motion/snapshots"
# while inotifywait -e access "/home/pi/motion/snapshots"
# while inotifywait -e modify "/home/pi/motion/snapshots"

while inotifywait -e access "/home/pi/telescope/photos"
do
    python3 "/home/pi/telescope/telescope_server.py"
done


