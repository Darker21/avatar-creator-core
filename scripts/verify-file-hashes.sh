#!/bin/bash

for file in dist/*; do
    checksum_file="dist/$(basename "$file").sha256"
    if [ -f "$checksum_file" ]; then
        sha256sum -c "$checksum_file"
    fi
done