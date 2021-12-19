#!/bin/bash
pyinstaller -F -n lotus --specpath ./build/tmp/ --distpath ./build/bin/  main.py
rm -rf __pycache__
rm -rf build/tmp
rm -rf build/lotus/
