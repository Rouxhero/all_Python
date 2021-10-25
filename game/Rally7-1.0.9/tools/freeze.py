#!/usr/bin/env python

"""
Freezing a Rally 7 distribution. This is based heavily on the convert script,
and all image and music resources should have been converted or prepared before
this script is run.

Copyright (C) 2007 Paul Boddie <paul@boddie.org.uk>

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

def freeze(freezepath, frozen, archive=None, libpython=None, libsdl=None, libsdlmixer=None, libsdlimage=None, libsdlttf=None):

    """
    Freeze the software using 'freezepath' as the path to the cx_Freeze
    installation and 'frozen' as the directory into which the frozen software
    will be written. If 'archive' is specified and has the value "zip", a .zip
    archive will be produced containing the frozen software; if 'archive' has
    the value "tgz", a .tar.gz archive will be produced containing the frozen
    software.

    The Python shared library to be included may be specified using the optional
    'libpython' parameter.
    """

    libpython = libpython or "/usr/lib/libpython2.4.so.1.0"
    libsdl = libsdl or "/usr/lib/libSDL-1.2.so.0"
    libsdlimage = libsdlimage or "/usr/lib/libSDL_image-1.2.so.0"
    libsdlmixer = libsdlmixer or "/usr/lib/libSDL_mixer-1.2.so.0"
    libsdlttf = libsdlttf or "/usr/lib/libSDL_ttf-2.0.so.0"

    freezepython = os.path.join(freezepath, "FreezePython")
    if not os.path.exists(freezepython):
        print "cx_Freeze not installed in", freezepath
        sys.exit(1)

    os.system(freezepython + " --shared-lib-name=%s --target-dir=%s rally7.py" % (libpython, frozen))

    for directory, directories in [
        (".", ["big", "medium", "small"]),
        ("characters", ["big", "medium", "small"]),
        ("special", ["big", "medium", "small"]),
        ("info", ["big", "medium", "small"]),
        ("music", ["."]),
        (".", ["."])
        ]:
        for dir in directories:
            source = os.path.join("data", directory, dir)
            target = os.path.join(frozen, "data", directory, dir)
            if not os.path.exists(target):
                os.makedirs(target)

            # Include source data as well as converted/prepared data.

            patterns = [
                os.path.join(source, "*" + os.extsep + "svg"), os.path.join(source, ".*" + os.extsep + "svg"),
                os.path.join(source, "*" + os.extsep + "png"), os.path.join(source, ".*" + os.extsep + "png"),
                os.path.join(source, "*" + os.extsep + "ogg"),
                os.path.join(source, "*" + os.extsep + "wav"),
                os.path.join(source, "*" + os.extsep + "mid"),
                os.path.join(source, "*" + os.extsep + "not")
                ]

            for resources in map(glob, patterns):
                for resource in resources:
                    filename = os.path.split(resource)[1]
                    cmd = "cp '%s' '%s'" % (resource.replace("'", "'\"'\"'"), os.path.join(target, filename).replace("'", "'\"'\"'"))
                    #print cmd
                    if os.system(cmd):
                        print cmd

    # The documentation and sources should also be copied.

    sources = os.path.join(frozen, "sources")
    docs = os.path.join(frozen, "docs")
    tools = os.path.join(frozen, "tools")

    if not os.path.exists(sources):
        os.makedirs(sources)

    if not os.path.exists(docs):
        os.makedirs(docs)

    if not os.path.exists(tools):
        os.makedirs(tools)

    os.system("cp %s %s" % ("*" + os.extsep + "txt", frozen))
    os.system("cp %s %s" % ("*" + os.extsep + "py", sources))
    os.system("cp %s %s" % (os.path.join("docs", "*" + os.extsep + "txt"), docs))
    os.system("cp %s %s" % (os.path.join("tools", "*" + os.extsep + "py"), tools))

    # Add SDL libraries.

    for lib in (libsdl, libsdlimage, libsdlmixer, libsdlttf):
        os.system("cp %s %s" % (lib, frozen))

    # Make a distribution.

    self_extracting_file = frozen + os.extsep + "run"
    extraction_command = "'./rally7; echo Run %s --noexec --keep to get at the code.'" % os.path.split(self_extracting_file)[-1]

    if archive == "zip":
        os.system("find %s -print | zip -@ %s" % (frozen, frozen + os.extsep + "zip"))
    elif archive == "tgz":
        os.system("tar zcf %s %s" % (frozen + os.extsep + "tar" + os.extsep + "gz", frozen))
    elif archive == "tbz2":
        os.system("tar jcf %s %s" % (frozen + os.extsep + "tar" + os.extsep + "bz2", frozen))
    elif archive == "sxgz":
        os.system("makeself --gzip %s %s '%s' %s" % (frozen, self_extracting_file, "Rally 7", extraction_command))
    elif archive == "sxbz2":
        os.system("makeself --bzip2 %s %s '%s' %s" % (frozen, self_extracting_file, "Rally 7", extraction_command))

if __name__ == "__main__":
    try:
        freeze(sys.argv[1], sys.argv[2], (sys.argv[3:] or [None])[0], (sys.argv[4:] or [None])[0])
    except IndexError:
        print "Please specify the path to cx_Freeze and a target directory."
        print "You can also specify 'zip', 'tgz' or 'tbz2' to make archives of the frozen software."
        print "Alternatively, you can specify 'sxgz' or 'sxbz2' to make self-extracting archives."
        print
        print "Example: python %s ../cx_Freeze-3.0.3/ /tmp/Rally7 sxbz2"
        sys.exit(1)

# vim: tabstop=4 expandtab shiftwidth=4
