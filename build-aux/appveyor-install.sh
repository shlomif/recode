#!/bin/sh
# Pre-install script for appveyor: install build deps

# Get mingw type, if any, from MSYSTEM
case $MSYSTEM in
    MINGW32)
        MINGW_BITS=i686
        PREFIX=/mingw32
        ;;
    MINGW64)
        MINGW_BITS=x86_64
        PREFIX=/mingw64
        ;;
    MSYS)
        PREFIX=/usr
        ;;
esac

# Build dependencies
pacman --noconfirm -S base-devel rsync python2 texinfo

# Cython
wget https://github.com/cython/cython/archive/0.27.3.tar.gz
tar zxvf 0.27.3.tar.gz
cd cython-0.27.3
python2 setup.py install
cd ..
