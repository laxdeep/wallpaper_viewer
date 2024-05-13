from tkinter import *
import os
from PIL import ImageTk,Image


def next_img():
    global count
    img_label.config(image = img_array[count%len(img_array)])
    count = count + 1
        
count = 1
root = Tk()
root.title('wallpaper viewer')
root.geometry('400x400')

root.configure(background='black')

files = os.listdir('wallpapers')
img_array = []
for file in files:
    img = Image.open(os.path.join('wallpapers',file))
    img_resize = img.resize((300,150))
    img_array.append(ImageTk.PhotoImage(img_resize))


img_label = Label(root,image = img_array[0])
img_label.pack(pady = (40,10))

next_bt = Button(root,bg ='white',fg='black',width=20,text = "next",command = next_img)
next_bt.pack(pady = (10,20))

root.mainloop()