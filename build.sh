#!/bin/sh
cd src
find . -iname "*.py" | xargs pylint 
pytest