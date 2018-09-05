#  Much of this code was borrowed from https://stevendkay.wordpress.com/2009/09/08/generating-ascii-art-from-photographs-in-python/

import random
from bisect import bisect
from Tkinter import *

def start():
    from PIL import Image
    img = Image.open(<path to image>)
    greyscale = [
                " ",
                " ",
                ".,-",
                "_ivc=!/|\\~",
                "gjez2]/(YL)t[+T7Vf",
                "mdK4ZGbNDXY5P*Q",
                "W8KMA",
                "#%$"
                ]

    zonebounds=[36,72,108,144,180,216,252]

    img=img.resize((160, 75),Image.BILINEAR)
    img=img.convert("L") # convert to mono

    str=""
    for y in range(0,img.size[1]):
        for x in range(0,img.size[0]):
            lum=255-img.getpixel((x,y))
            row=bisect(zonebounds,lum)
            possibles=greyscale[row]
            str=str+possibles[random.randint(0,len(possibles)-1)]
        str=str+"\n"

    #print str

    text.delete("1.0", END)
    text.insert(END, str)

master = Tk()
master.geometry("1500x1000")
master.grid_columnconfigure(0, weight=1)

text = Text(master, width=160, height=75)
text.config(font=("Consolas", 7))
text.pack(padx=0, pady=0)

b = Button(master, text="Start", command=start)
b.pack(padx=0, pady=0)

mainloop()
