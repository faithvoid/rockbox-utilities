# Rockbox Utilities
## Utilities for managing a Rockbox library on iPods (or similar devices running Rockbox)

### coverResize.py (Linux-only)
- Automatically resize all large cover art (cover.jpg/cover.png) in your iPod library to 500x500, more than enough for the iPod's screen, while ensuring small file sizes and quick loading times for album art.

### coverSaveSpace.py (Linux-only)
- Automatically extracts "cover.jpg" from MP3 files if available, then removes it from the individual track, saving a bit of space for every album. (on an iPod with over 17,000 music files with 1MB cover art files embedded, this saves approximately 17GB of space)

## albumYear.py
- Automatically add album's year to the end of the album folder name (ie; Dowsing -> It's Still Pretty Terrible (2012) )

### flac2mp3.py (Linux-only)
- Automatically covert all available FLAC files on your device to high-quality 320kbps MP3, using ffmpeg. May expand this into a larger utility that supports more formats.
