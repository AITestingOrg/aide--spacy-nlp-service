#!/bin/sh
cd src
find . -iname "*.py" | xargs pylint 
python -m pytest tests