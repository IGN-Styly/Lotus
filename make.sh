#!/bin/bash
pyinstaller -F -n app --specpath ./build/tmp/ --distpath ./build/bin/  ./Lotus/main.py
rm -rf __pycache__
rm -rf build/tmp
rm -rf build/lotus/
