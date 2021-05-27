#!/bin/bash

rm -f depictions/* sileodepictions/*
python3 depiction_gen.py
dpkg-scanpackages -m ./debs /dev/null > Packages
gzip -cf Packages > Packages.gz
xz -9fkev Packages > Packages.xz
bzip2 -cf Packages > Packages.bz2
