#!/usr/bin/env bash

set -euo pipefail

# brew install zstd lz4 xz

# rm -f depictions/* sileodepictions/*
echo "Minifying assets..."
uv run python minify_assets.py
echo "Importing depictions..."
uv run python main.py
echo "Validating metadata and generating Packages..."
uv run python scan_packages.py
echo "Compressing Packages files..."
gzip -ncf Packages > Packages.gz
xz -9fkev Packages > Packages.xz
bzip2 -cf Packages > Packages.bz2
zstd -c19 Packages > Packages.zst
lzma -kf Packages
lz4 -qf Packages
