import ZipSteganograPy as package
from setuptools import setup

setup(
    name=package.__name__,
    version=package.__version__,
    py_modules=[package.__name__],
    install_requires=[],
    author=package.__author__,
    author_email=package.__author_email__,
    maintainer=package.__maintainer__,
    maintainer_email=package.__maintainer_email__,
    description=package.__description__,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=package.__url__,
    project_urls={
        "Documentation": "https://mauricelambert.github.io/info/python/code/ZipSteganograPy.html",
        "Executable": "https://mauricelambert.github.io/info/python/code/ZipSteganograPy.pyz",
    },
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Topic :: Security",
        "Environment :: Console",
    ],
    entry_points={
        "console_scripts": [
            "ZipSteganograPy = ZipSteganograPy:main",
        ],
    },
    python_requires=">=3.6",
    keywords=[
        "Steganography",
        "Hide",
        "Image",
        "archive",
        "ZIP",
        "PNG",
        "JPG",
        "JPEG",
    ],
    platforms=["Windows", "Linux", "MacOS"],
    license=package.__license__,
)