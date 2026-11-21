#!/usr/bin/env bash
# Renderiza los capítulos y los une con la pantalla final en out/<nombre>.mp4
set -e
cd "$(dirname "$0")"; NAME=$(basename "$PWD"); CAPS=$(ls -d cap* | sort -V)
echo $CAPS | tr " " "\n" | xargs -P 3 -I{} sh -c "cd {} && npx givemotion render video.html -o out/{}.mp4 2>&1 | tail -1"
(cd extras && [ -f endscreen.html ] && npx givemotion render endscreen.html -o pantalla-final.mp4 2>&1 | tail -1)
mkdir -p out && : > out/list.txt
for c in $CAPS; do echo "file '$PWD/$c/out/$c.mp4'" >> out/list.txt; done
[ -f extras/pantalla-final.mp4 ] && echo "file '$PWD/extras/pantalla-final.mp4'" >> out/list.txt
ffmpeg -v error -y -f concat -safe 0 -i out/list.txt -c copy out/$NAME.mp4
ffmpeg -v error -y -i out/$NAME.mp4 -c:v libx264 -crf 28 -preset veryfast -c:a aac -b:a 128k $NAME-ligero.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 out/$NAME.mp4
