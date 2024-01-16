import curses
import os
import sys
from PIL import Image

# Try to get image path as given as command argument
try:
    img_path = str(sys.argv[1])
    im = Image.open(img_path) # Original image, remains unchanged
    imc = Image.open(img_path) # Copy of image, where changes are applied
except Exception as ex:
    print(ex)
    pass

'''
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
'''

placeholder_no_image_selected = "No image selected"

topbar_fkeys = "f1\tf2\tf3\tf4\tf5\tf6\tf7\tf8\tf9\tf10\tf11\tf12\n"
topbar_uses  = "f1\tf2\tf3\tf4\tf5\tf6\tf7\tf8\tf9\tf10\tf11\texit\n"

def main(win):
    win.nodelay(False)
    key=""
    win.clear()
    win.addstr(topbar_fkeys)
    win.addstr(topbar_uses)
    try:
        win.addstr(img_path)
    except:
        win.addstr(placeholder_no_image_selected)
    while 1:
        try:
            key = win.getkey()
            win.clear()
            win.addstr(topbar_fkeys)
            win.addstr(topbar_uses)
            try:
                win.addstr(img_path)
            except:
                win.addstr(placeholder_no_image_selected)
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
                case "KEY_F(9)": # Open new image
                    win.clear()
                    win.addstr("Input Filename: ")
                    img_path = strip(win.getstr())
                    im = Image.open(img_path)
                    imc = Image.open(img_path)
                    if img_path == "":
                        pass
                    else:
                        pass # Will be replaced with asking the user if they wish to discard the old image
                case "KEY_F(10)": # 
                    pass
                case "KEY_F(11)": # 
                    pass
                case "KEY_F(12)": # Exit on f12
                    break
        except Exception as e:
            # No input
            pass
            
print(img_path)
curses.wrapper(main)