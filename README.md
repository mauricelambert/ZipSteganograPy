![ZipSteganograPy logo](https://mauricelambert.github.io/info/python/code/ZipSteganograPy_small.png "ZipSteganograPy logo")
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

## Links

 - [Github Page](https://github.com/mauricelambert/ZipSteganograPy/)
 - [Pypi package](https://pypi.org/project/ZipSteganograPy/)
 - [Documentation](https://mauricelambert.github.io/info/python/code/ZipSteganograPy.html)
 - [Python Executable](https://mauricelambert.github.io/info/python/code/ZipSteganograPy.pyz)

## Licence

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
