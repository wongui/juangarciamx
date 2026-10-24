#!/bin/sh
# Project videos for the grey-box, from the Vimeo downloads in assets/source/ (never touched; that folder is git-ignored, so the site can't load from it):
#  - assets/data/video-<slug>.mp4: the project page's main video: the download's own video stream, untouched, with the sound taken out
#    (it's what juangarcia.mx plays; re-encoding to 720p made them blockier and halved the vertical ones to 406 px wide)
#  - assets/data/card-video-<slug>.mp4: a short, silent, card-shaped (1.6:1, 640 x 400) loop for the card / bubble and the next-project preview
#  - assets/data/card-video-<slug>.js: that loop as a data URI (window.CARD_VID[slug]), so WebGL can draw it even when the page is opened from disk
#    (it refuses video files over file://, as it does images; see card_images.py)
# usage: sh tools/card_videos.sh             (every project)
#        sh tools/card_videos.sh config2026  (only the projects named)
cd "$(dirname "$0")/.." || exit 1
SRC=assets/source/juangarcia-mx-framer
ONLY=" $* "
want() { [ "$ONLY" = "  " ] || case "$ONLY" in *" $1 "*) return 0;; *) return 1;; esac; }
# the card loop and its data-URI script: card <slug> <source> <start> <length> [left: crop from the left edge instead of the centre]
card() {
  ffmpeg -v error -y -ss "$3" -t "$4" -i "$2" -an \
    -vf "scale=640:400:force_original_aspect_ratio=increase,crop=640:400${5:+:0:(ih-oh)/2},fps=30" \
    -c:v libx264 -profile:v main -pix_fmt yuv420p -crf 24 -preset slow -movflags +faststart "assets/data/card-video-$1.mp4"
  printf 'window.CARD_VID=window.CARD_VID||{};CARD_VID["%s"]="data:video/mp4;base64,%s";\n' "$1" "$(base64 -i "assets/data/card-video-$1.mp4" | tr -d '\n')" > "assets/data/card-video-$1.js"
  echo "$1  page $(du -h "assets/data/video-$1.mp4" | cut -f1)  card $(du -h "assets/data/card-video-$1.mp4" | cut -f1)"
}
# slug:vimeo id:start (s; 0 for all, Juan wants the videos from their first frame; the page video carries on from the card's frame, so a later start
# needs an offset in playMain in index.html):loop length (s)[:page video length (s), when the whole video is too heavy]
for row in aido:1024246820:0:10 jiviniti:1024544300:0:10 around:920256960:0:10 chiefchallenges:919866881:0:10 \
           nocturna:917237556:0:10 surrealelfs:917251662:0:10 rmc:917283133:0:10 luum:1092830929:0:10 trascender:1125948427:0:8:60 \
           coltrane:920144108:0:10; do
  IFS=: read slug id ss len plen <<EOF
$row
EOF
  want "$slug" || continue
  in="$SRC/$slug/media/vimeo-$id.mp4"
  ffmpeg -v error -y ${plen:+-t $plen} -i "$in" -an -c:v copy -movflags +faststart "assets/data/video-$slug.mp4"
  card "$slug" "$in" "$ss" "$len"
done
# screen recordings Juan supplies, kept in assets/source/lab or work (git-ignored: too big for GitHub). They're huge (3456 px, 120 fps),
# so the page video is re-encoded: 1920 px wide, silent (and down to 60 fps when it's higher). Also Juan's own exports, like Hule's logo motion
# slug:path:start:loop length[:left, to keep the left edge in the card (Config's slide titles sit on the left)][:fps, to lower it]
for row in config2026:assets/source/lab/config2026/screen-recording.mov:0:10:left:60 hule:assets/source/work/hule/logo-motion.mp4:0:8; do
  IFS=: read slug in ss len anchor fps <<EOF
$row
EOF
  want "$slug" || continue
  ffmpeg -v error -y -i "$in" -an -vf "scale=1920:-2${fps:+,fps=$fps}" -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 23 -preset slow -movflags +faststart "assets/data/video-$slug.mp4"
  card "$slug" "$in" "$ss" "$len" "$anchor"
done
# videos inside a project's gallery (gal entries named video-<name> in index.html): the download's own stream, silent, in assets/data/gallery/<slug>/
# slug:vimeo id:name
for row in hule:1092826366:launch hule:1092827311:branding; do
  IFS=: read slug id name <<EOF
$row
EOF
  want "$slug" || continue
  mkdir -p "assets/data/gallery/$slug"
  ffmpeg -v error -y -i "$SRC/$slug/media/vimeo-$id.mp4" -an -c:v copy -movflags +faststart "assets/data/gallery/$slug/video-$name.mp4"
  echo "$slug gallery video-$name $(du -h "assets/data/gallery/$slug/video-$name.mp4" | cut -f1)"
done
