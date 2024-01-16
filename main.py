import curses
import os
import sys

# Try to get image path as given as command argument
try:
    img_path = str(sys.argv[1])
except:
    pass

'''
- f1: invert
- f2: grayscale
- f3: rotate anticlockwise
- f4: rotate clockwise

- f5: crop
- f6: hue adjust
- f10: save (overwrite)
- f8: save (copy)

- f9: open new image (save/discard)
- f10: fullscreen the original image
- f11: fullscreen the edit preview
- f12: quit (save/discard)
'''

topbar_fkeys = "f1\tf2\tf3\tf4\tf5\tf6\tf7\tf8\tf9\tf10\tf11\tf12\n"
topbar_uses  = "f1\tf2\tf3\tf4\tf5\tf6\tf7\tf8\tf9\tf10\tf11\texit\n"

def main(win):
    win.nodelay(False)
    key=""
    win.clear()
    win.addstr(topbar_fkeys)
    win.addstr(topbar_uses)
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr(topbar_fkeys)
            win.addstr(topbar_uses)
            match key:
                case "KEY_F(1)": # 
                    pass
                case "KEY_F(2)": # 
                    pass
                case "KEY_F(3)": # 
                    pass
                case "KEY_F(4)": # 
                    pass
                case "KEY_F(5)": # 
                    pass
                case "KEY_F(6)": # 
                    pass
                case "KEY_F(7)": # 
                    pass
                case "KEY_F(8)": # 
                    pass
                case "KEY_F(9)": # 
                    pass
                case "KEY_F(10)": # 
                    pass
                case "KEY_F(11)": # 
                    pass
                case "KEY_F(12)": # Exit on f12
                    break
        except Exception as e:
            # No input
            pass

curses.wrapper(main)