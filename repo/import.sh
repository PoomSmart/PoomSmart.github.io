#!/usr/bin/env bash

set -euo pipefail

# brew install dpkg zstd lz4

# rm -f depictions/* sileodepictions/*
uv run python main.py
dpkg-scanpackages -m ./debs /dev/null > Packages
gzip -ncf Packages > Packages.gz
xz -9fkev Packages > Packages.xz
bzip2 -cf Packages > Packages.bz2
zstd -c19 Packages > Packages.zst
lzma -kf Packages
lz4 -qf Packages
