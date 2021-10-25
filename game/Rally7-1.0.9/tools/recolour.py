#!/usr/bin/env python

"""
Recolouring script previously used to change the colour of the designed
characters.

Copyright (C) 2006 Paul Boddie <paul@boddie.org.uk>

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys

colours = [("#0000b4", "#000000"), ("#00ffff", "#ffffff")]

for filename in sys.argv[1:]:
    f = open(filename, "rb")
    s = f.read()
    f.close()
    for old, new in colours:
        s = s.replace(old, new)
    f = open(filename, "wb")
    f.write(s)
    f.close()

# vim: tabstop=4 expandtab shiftwidth=4
