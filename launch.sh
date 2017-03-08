#!/bin/bash



python3 main.py

if [ -f outputs/source_code.tar.gz ]; then
    rm *.tar.gz
fi
tar zcf outputs/source_code.tar.gz *.py
