#!/bin/bash
#
# start_telescope_client.bash - Bootstrap loader for telescope_client.py.
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


# Wait for changes to Dropbox directory
while inotifywait "/path/to/Dropbox/directory/"
do
    python3 "/path/to/telescope_client.py"
done


