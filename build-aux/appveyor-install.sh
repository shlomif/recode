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
        MINGW_BITS=msys
        PREFIX=/usr
        ;;
esac

# Build dependencies
pacman --noconfirm -S rsync mingw-w64-$MINGW_BITS-cython
pip install six
