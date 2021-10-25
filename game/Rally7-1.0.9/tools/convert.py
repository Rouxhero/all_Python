#!/usr/bin/env python

"""
Conversion of SVG templates into PNG images.

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
from glob import glob

def convert():
    for directory, directories, sizes in [
        (".", ["big", "medium", "small"], ["60 60", "48 48", "30 30"]),
        ("characters", ["big", "medium", "small"], ["20 30", "16 24", "10 15"]),
        ("special", ["big", "medium", "small"], ["240 120", "192 96", "120 60"]),
        ("info", ["big", "medium", "small"], ["40 30", "32 24", "20 15"])
        ]:
        for dir, size in zip(directories, sizes):
            source = os.path.join("data", "templates", directory)
            target = os.path.join("data", directory, dir)
            if not os.path.exists(target):
                os.makedirs(target)
            patterns = [os.path.join(source, "*" + os.extsep + "svg"), os.path.join(source, ".*" + os.extsep + "svg")]
            for templates in map(glob, patterns):
                for template in templates:
                    path, ext = os.path.splitext(template)
                    path, name = os.path.split(path)
                    image = os.path.join(target, name + os.extsep + "png")
                    cmd = "ksvgtopng %s '%s' '%s'" % (size, template.replace("'", "'\"'\"'"), image.replace("'", "'\"'\"'"))
                    #print cmd
                    os.system(cmd)

    os.system("ksvgtopng 48 48 '%s' '%s'" % (os.path.join("data", "templates", "car.svg"), os.path.join("data", "rally7-icon.png")))
    os.system("cp '%s' '%s'" % (os.path.join("data", "templates", "car.svg"), os.path.join("data", "rally7-icon.svg")))

if __name__ == "__main__":
    convert()

# vim: tabstop=4 expandtab shiftwidth=4
