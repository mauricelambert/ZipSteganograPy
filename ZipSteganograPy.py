#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This tool hides a ZIP archive in an image.
#    Copyright (C) 2021, 2022  Maurice Lambert

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This tool hides a ZIP archive in an image.

This tool is useful for bypassing antivirus and firewall scanning.

Hide a ZIP archive in an image:
~# python3 ZipSteganograPy.py -z archive.zip -o stegano -i image.png
~# python3 ZipSteganograPy.py -z archive.zip -o stegano -i image.jpg

Create a ZIP archive (with 3 text files) and hide it in an image:
~# python3 ZipSteganograPy.py -f file1.txt file2.txt file3.txt -i image.jpg
~# python3 ZipSteganograPy.py -f file1.txt file2.txt file3.txt -i image.png

Easily extract the hidden archive using python3 and its standard library:
~# python3 -m zipfile -l stegano.png            # list files
~# python3 -m zipfile -e stegano.jpg output/    # extract

Easily extract the hidden archive using unzip package:
~# unzip stegano.jpg -l                         # list files
~# unzip stegano.jpg -d output/                 # extract
"""

__version__ = "0.0.2"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This tool hides a ZIP archive in an image.

This tool is useful for bypassing antivirus and firewall scanning.
"""
__license__ = "GPL-3.0 License"
__url__ = "https://github.com/mauricelambert/ZipSteganograPy"

copyright = """
ZipSteganograPy  Copyright (C) 2022  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
license = __license__
__copyright__ = copyright

print(copyright)

from argparse import ArgumentParser, Namespace
from os.path import splitext, exists
from tempfile import TemporaryFile
from shutil import copyfileobj
from typing import Tuple, List
from sys import stderr, exit
from zipfile import ZipFile


def parse_args() -> Namespace:

    """
    This function parses command lines arguments.
    """

    parser = ArgumentParser(
        description="Create a new image containing the image and the zip file."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-z", "--zipfile", help="The zip file to hide.")
    group.add_argument(
        "-f",
        "--files",
        help="The files to zip and hide.",
        action="extend",
        nargs="+",
    )
    parser.add_argument(
        "-i", "--image", help="The jpeg/png file to use.", required=True
    )
    parser.add_argument(
        "-o", "--outfile", help="The output filename.", default="stegano"
    )
    return parser.parse_args()


def create_archive(files: List[str]) -> Tuple[TemporaryFile, int]:

    """
    This function creates a temporary zip file
    and returns the file object.
    """

    error_code = 0
    zipfile = TemporaryFile()
    zipfile_obj = ZipFile(zipfile, "w")
    nfiles = len(files)

    while nfiles:
        file = files.pop()
        nfiles -= 1

        if not exists(file):
            print(f"Error: file {file!r} does not exists.", file=stderr)
            error_code = 5
            continue

        zipfile_obj.write(file)

    zipfile_obj.close()
    zipfile.seek(0)

    return zipfile, error_code


def main() -> int:

    """
    This function executes checks arguments
    and hides the zip archive in image.
    """

    arguments = parse_args()
    error_code = 0
    filename = arguments.image

    if not exists(filename):
        print(f"Error: image {filename!r} does not exist.", file=stderr)
        return 2

    zipfilename = arguments.zipfile

    if zipfilename and not exists(zipfilename):
        print(f"Error: zipfile {zipfilename!r} does not exist.", file=stderr)
        return 3

    image_ame, extension = splitext(filename)

    if (
        extension != ".jpg"
        and extension != ".jpeg"
        and extension != ".jpe"
        and extension != ".png"
    ):
        print(
            "Error: Image file extension should be 'jpg',"
            " 'jpeg', 'jpe' or 'png'.",
            file=stderr,
        )
        return 4

    new_image_name = splitext(arguments.outfile)[0] + extension
    new_image = open(new_image_name, "wb")

    if zipfilename:
        zipfile = open(zipfilename, "rb")
    else:
        zipfile, error_code = create_archive(arguments.files)

    with open(filename, "rb") as image:
        copyfileobj(image, new_image)

    copyfileobj(zipfile, new_image)

    zipfile.close()
    new_image.close()

    print(
        f"New image {new_image_name!r} created "
        f"from {filename!r} with hidden ZIP archive."
    )

    return error_code


if __name__ == "__main__":
    exit(main())
