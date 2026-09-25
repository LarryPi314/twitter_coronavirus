#!/bin/bash

mkdir -p outputs
mkdir -p logs

for file in /data/Twitter\ dataset/geoTwitter20-*.zip
do
    name=$(basename "$file")
    nohup ./src/map.py \
        --input_path="$file" \
        --output_folder=outputs \
        > "logs/$name.log" 2>&1 &
done
