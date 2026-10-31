#!/usr/bin/env bash

set -euo pipefail

count="${1:-20}"
root="$(cd "$(dirname "$0")" && pwd)"

cd "$root"
find debs -name '*.deb' -exec du -h {} + | sort -hr | awk -v n="$count" 'NR <= n'
