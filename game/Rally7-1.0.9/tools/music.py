#!/usr/bin/env python

"""
Conversion of MIDI scores into audio tracks.

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

import os, sys
from glob import glob

format_codes = {
    "ogg" : "v",
    "wav" : "w"
    }

def convert(format):
    format_code = format_codes[format]
    directory = os.path.join("data", "music")
    pattern = os.path.join(directory, "*" + os.extsep + "mid")
    for score in glob(pattern):
        path, ext = os.path.splitext(score)
        path, name = os.path.split(path)
        audio = os.path.join(directory, name + os.extsep + format)
        tmp_audio = os.path.join(directory, "_" + name + os.extsep + format)
        cmd = "timidity -O%s -o %s %s" % (format_code, tmp_audio, score)
        #print cmd
        os.system(cmd)
        cmd = "sox %s %s silence 0 1 00:00:01 1.5%%" % (tmp_audio, audio)
        #print cmd
        os.system(cmd)
        os.remove(tmp_audio)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        convert("ogg")
    else:
        format = sys.argv[1]
        convert(format)

# vim: tabstop=4 expandtab shiftwidth=4
