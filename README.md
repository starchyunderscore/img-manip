# img-manip
Simple TUI image manipulator written in python

To use:

1. Download main.py & all dependencies, run with python3
2. Use package made with cx_freeze (not ready yet)


Current state:

I think I know how to do all the needed user input, however I still need to figure out image manipulation and display

The plan:

Display preview of original image next to edited on most of the top of the screen (using the screenbuffer?).

On the bottom of the screen, some options:

- f1: invert
- f2: grayscale
- f3: rotate (cursor keys)
- f4: flip (cursor keys)

- f5: crop
- f6: advanced (hue, saturation, brightness)
- f10: 
- f8: save (overwrite/copy)

- f9: open new image (save(overwrite/copy)/discard)
- f10: fullscreen the original image
- f11: fullscreen the edit preview
- f12: quit (save/discard)