#!/bin/bash
pyinstaller -F -n $1 --specpath ./build/tmp/ --distpath ./build/bin/  ./Lotus/main.py
rm -rf __pycache__
rm -rf build/tmp
rm -rf build/$1/
