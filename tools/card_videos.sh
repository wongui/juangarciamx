#!/bin/sh
# Project videos for the grey-box, from the Vimeo downloads in assets/source/ (never touched; that folder is git-ignored, so the site can't load from it):
#  - assets/data/video-<slug>.mp4: the project page's main video, a silent 720p web copy
#  - assets/data/card-video-<slug>.mp4: a short, silent, card-shaped (1.6:1, 640 x 400) loop for the card / bubble and the next-project preview
#  - assets/data/card-video-<slug>.js: that loop as a data URI (window.CARD_VID[slug]), so WebGL can draw it even when the page is opened from disk
#    (it refuses video files over file://, as it does images; see card_images.py)
# Coltrane is left out: its page on juangarcia.mx is behind an NDA.
# usage: sh tools/card_videos.sh
cd "$(dirname "$0")/.." || exit 1
SRC=assets/source/juangarcia-mx-framer
# slug:vimeo id:start (s into the video, past any fade-in; keep PREV_AT in index.html in step):loop length (s)[:page video length (s), when the whole video is too heavy]
for row in aido:1024246820:2:10 jiviniti:1024544300:2:10 around:920256960:2:10 chiefchallenges:919866881:2:10 \
           nocturna:917237556:2:10 surrealelfs:917251662:2:10 rmc:917283133:2:10 hule:1092826366:2:10 luum:1092830929:2:10 trascender:1125948427:2:8:60; do
  IFS=: read slug id ss len plen <<EOF
$row
EOF
  in="$SRC/$slug/media/vimeo-$id.mp4"
  ffmpeg -v error -y ${plen:+-t $plen} -i "$in" -an -vf "scale=-2:720" -c:v libx264 -profile:v main -pix_fmt yuv420p -crf 28 -maxrate 1500k -bufsize 3000k -preset slow -movflags +faststart "assets/data/video-$slug.mp4"
  ffmpeg -v error -y -ss "$ss" -t "$len" -i "$in" -an \
    -vf "scale=640:400:force_original_aspect_ratio=increase,crop=640:400,fps=30" \
    -c:v libx264 -profile:v main -pix_fmt yuv420p -crf 30 -preset slow -movflags +faststart "assets/data/card-video-$slug.mp4"
  printf 'window.CARD_VID=window.CARD_VID||{};CARD_VID["%s"]="data:video/mp4;base64,%s";\n' "$slug" "$(base64 -i "assets/data/card-video-$slug.mp4" | tr -d '\n')" > "assets/data/card-video-$slug.js"
  echo "$slug  page $(du -h "assets/data/video-$slug.mp4" | cut -f1)  card $(du -h "assets/data/card-video-$slug.mp4" | cut -f1)"
done
