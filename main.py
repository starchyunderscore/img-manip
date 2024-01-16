import curses
import os

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
                case "KEY_F(12)": # Exit on f12
                    break
        except Exception as e:
            # No input
            pass

curses.wrapper(main)