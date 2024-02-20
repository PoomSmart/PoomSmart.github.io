#!/usr/bin/env bash

# brew install dpkg

# rm -f depictions/* sileodepictions/*
python3 gen/depiction.py
dpkg-scanpackages -m ./debs /dev/null > Packages
gzip -cf Packages > Packages.gz
xz -9fkev Packages > Packages.xz
bzip2 -cf Packages > Packages.bz2
zstd -c19 Packages > Packages.zst
