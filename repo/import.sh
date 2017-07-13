#!/bin/bash
dpkg-scanpackages -m ./ /dev/null | gzip > Packages.gz;

dpkg-scanpackages -m ./ /dev/null | bzip2 > Packages.bz2;

dpkg-scanpackages -m ./ /dev/null > Packages;
