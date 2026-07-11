#!/usr/bin/env bash

set -euo pipefail

# brew install dpkg zstd lz4

# rm -f depictions/* sileodepictions/*
echo "Importing depictions..."
uv run python main.py
echo "Validating deb coverage..."
uv run python validate_data.py
echo "Generating Packages files..."
dpkg-scanpackages -m ./debs /dev/null > Packages
echo "Compressing Packages files..."
gzip -ncf Packages > Packages.gz
xz -9fkev Packages > Packages.xz
bzip2 -cf Packages > Packages.bz2
zstd -c19 Packages > Packages.zst
lzma -kf Packages
lz4 -qf Packages
