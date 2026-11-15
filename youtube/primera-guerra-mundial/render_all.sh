#!/usr/bin/env bash
# Renderiza los 8 capítulos y los une en out/primera-guerra-mundial.mp4
set -e
cd "$(dirname "$0")"
for i in 0 1 2 3 4 5 6 7; do (cd cap$i && npx givemotion render video.html -o out/cap$i.mp4 2>&1 | tail -1); done
mkdir -p out && : > out/list.txt
for i in 0 1 2 3 4 5 6 7; do echo "file '$PWD/cap$i/out/cap$i.mp4'" >> out/list.txt; done
ffmpeg -v error -y -f concat -safe 0 -i out/list.txt -c copy out/primera-guerra-mundial.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 out/primera-guerra-mundial.mp4
