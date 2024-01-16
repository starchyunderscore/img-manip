import curses
import os
import sys
from PIL import Image

# Try to get image path as given as command argument

try:
    global img_path
    global im
    global imc
    img_path = str(sys.argv[1])
    im = Image.open(img_path) # Original image, remains unchanged
    imc = Image.open(img_path) # Copy of image, where changes are applied
except:
    img_path = 0 # Defaults to ignore
    im = 0
    imc = 0

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

pil_image_extensions = Image.registered_extensions()
pil_supported_images = {ex for ex, f in pil_image_extensions.items() if f in Image.SAVE}

working_directory = os.getcwd()

placeholder_no_image_selected = "No image selected"

topbar_fkeys = "f1\tf2\tf3\tf4\tf5\tf6\tf7\tf8\tf9\tf10\tf11\tf12\n"
topbar_uses  = "f1\tf2\tf3\tf4\tf5\tf6\tf7\tf8\topen\tf10\tf11\texit\n"

def scupdate(win, im, imc): # Display the top bars and the images
    win.clear()
    win.addstr(topbar_fkeys)
    win.addstr(topbar_uses)
    try:
        win.addstr(img_path)
    except:
        win.addstr(placeholder_no_image_selected)

def main(win):
    global im
    global imc
    global img_path
    win.nodelay(False)
    key=""
    scupdate(win, im, imc)
    while 1:
        try:
            key = win.getkey()
            scupdate(win, im, imc)
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
                    try:
                        win.clear()
                        curses.echo()
                        
                        directory_contents_display = []
                        directory_contents = os.listdir(working_directory)
                        for item in directory_contents:
                            if any(x in item.lower() for x in pil_supported_images):
                                directory_contents_display += item
                        
                        win.addstr("Input Filename: ")
                        
                        win.addstr("\n" + "".join(directory_contents_display))
                            
                        tmp_img_path = str(win.getstr(0, 16, 100)).strip().replace("\n", "")[2:-1]
                        if tmp_img_path == "":
                            pass
                        else: # Will add asking the user if they wish to discard the old image
                            tmp_im = Image.open(tmp_img_path)
                            tmp_imc = Image.open(tmp_img_path) 
                            # Remove from temporary only after chance of error has passed, otherwise it may update incorrectly
                            img_path = tmp_img_path
                            im = tmp_im
                            imc = tmp_imc
                        scupdate(win, im, imc)
                    except Exception as e:
                        print(e)
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