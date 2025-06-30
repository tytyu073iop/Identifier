# Identifier - app that says if video of the series is the right length (Still in develop)
uses tvdb api to determine the right length and ffmpeg to check the video length

## Example how it should work

video file - KiffS01E13.mkv, length - 20 min
what length should be - 10 min
```
python Identifier.py KiffS01E13.mkv
wrong length - KiffS01E13.mkv
```
## Plans
- [ ] Make it work
- [ ] Integrate it with Sonarr
