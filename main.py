"""
Created on Thu Jan 23 22:24:07 2020
@author: imran
"""

from tkinter import * 
from tkinter.filedialog import *
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkfontchooser import askfont
#local class
from filtres import Filtre


# global variables:
x1 = 0
y1 = 0
x2 = 0
y2 = 0
command = "Draw"
color   = "black"
font    = {'family': '@Arial Unicode MS', 'size': 10, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}

def coords_reset():
    global x1
    global y1
    global x2
    global y2
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    
def canvas_set(image):
    global canvas
    photo = ImageTk.PhotoImage(image)
    canvas.config(width=image.width, height=image.height)
    canvas.image= photo
    canvas.create_image(0, 0, anchor=NW, image=photo)
    
def about():
    messagebox.showinfo("A propos de", "Image processor 1.0 - Created by Imran YAZIDI & Khadija OUCHATTI")
  
def newimg():
    global image
    global draw
    image = Image.new("RGB", (500, 400), "white")
    draw  = ImageDraw.Draw(image)
    photo = ImageTk.PhotoImage(image)
    canvas2.config(width=image.width, height=image.height)
    canvas2.image= photo
    canvas2.create_image(0, 0, anchor=NW, image=photo)
    canvas_set(image)
    
def openimg():
    global filepath
    filepath = askopenfilename(title="Ouvrir une image",filetypes=[('all files','.*')])
    global image
    global draw
    image = Image.open(filepath)
    draw  = ImageDraw.Draw(image)
    global canvas2
    photo = ImageTk.PhotoImage(image)
    canvas2.config(width=image.width, height=image.height)
    canvas2.image= photo
    canvas2.create_image(0, 0, anchor=NW, image=photo)
    canvas_set(image)

def hide_canvas2():
    canvas2.grid_remove()
    
def saveimgas():
    global image
    f = asksaveasfilename(filetypes=[('Png files', '.png'),('All files', '*')], defaultextension=".png")
    image.save(f,"PNG")
    
# Image  filters
    
def imgbin():
    global image
    image=Filtre(image).binary(x1,y1,x2,y2)
    canvas_set(image)
    
def imggraylevel():
    global image
    image=Filtre(image).graylevel()
    canvas_set(image)
    
def imgbrightnessplus():
    global image
    image=Filtre(image).brightness(50)
    canvas_set(image)
    
def imgbrightnessmoins():
    global image
    image=Filtre(image).brightness(-50)
    canvas_set(image)
    
def imgreverse():
    global image
    image=Filtre(image).reverse()
    canvas_set(image)



def mousemove(event):
    cursorposition.config(text="X: "+str(event.x)+" Y: "+str(event.y))

def mousemoveclick(event):
    global x1
    global y1
    global x2
    global y2
    
    if(command == "Draw"):
        xl,y1=(event.x -1), (event.y -1) 
        x2,y2=(event.x+1), (event.y+1) 
        draw.rectangle([(xl,y1),(x2,y2)], fill=color, outline=color)
        canvas_set(image)
   
    if(command =="Select"):
        if(x1==0):
            x1 = event.x
            y1 = event.y
        else:
            x2 = event.x
            y2 = event.y
            canvas.delete('no')
            dashes = [3, 2]
            canvas.create_rectangle(x1,y1,x2,y2,dash=dashes,outline="white",tags='no')
            canvas.create_rectangle(x1+1,y1+1,x2+1,y2+1,dash=dashes,outline="black",tags='no')
            
            
def mouseclick(event):
    global x1
    global y1
    global x2
    global y2
    global image
            
    if(command=="Text"):
        x1 = event.x
        y1 = event.y
        root = Tk()
        root.title("Insert Text")
        label = Label(root, fg="green",text="Insert Text")
        label.pack()
        text = Entry(root,text="Hello")
        text.pack()
        def set_text():
            global image
            draw  = ImageDraw.Draw(image)
            myfont = ImageFont.truetype('gulim', font['size'])
            draw.text((x1,y1), text.get(), font = myfont, fill=color)
            canvas_set(image)
            root.destroy()
        
        button = Button(root, text='OK', width=25, command=set_text)
        button.pack()
        root.mainloop()

def paint(): 
    global command
    command ="Draw"
    canvas.config(cursor="dot")
    commandlabel.config(text="Command: "+ command)
    
def select():
     global command
     command ="Select"
     commandlabel.config(text="Command: "+ command)
     canvas.config(cursor="tcross")
     coords_reset()
     
def errase():
    global color
    color = "white"
    
def askingcolor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    print((rgb, hx))
    
def askingfont():
    global font
    font = askfont(fenetre)
    print(font)
    
def imgcrop():
    global x1
    global y1
    global x2
    global y2
    global image
    command = "Crop"
    commandlabel.config(text="Command: "+ command)
    image = image.crop((x1, y1, x2, y2))
    canvas_set(image)
    coords_reset()


def imgtext():
    global command
    command ="Text"
    canvas.config(cursor="xterm")
    commandlabel.config(text="Command: "+ command)
    
    
    
def reset():
    global filepath
    global image
    global draw
    image = Image.open(filepath)
    draw  = ImageDraw.Draw(image)
    photo = ImageTk.PhotoImage(image)
    canvas_set(image)
    
def mirror():
    global image
    image=Filtre(image).mirror()
    canvas_set(image)
    
def rotation():
    global image
    image=Filtre(image).rotation()
    canvas_set(image)
    
def cut_red():
    global image
    image=Filtre(image).cut_color("red")
    canvas_set(image)

def cut_green():
    global image
    image=Filtre(image).cut_color("green")
    canvas_set(image)
    
def cut_blue():
    global image
    image=Filtre(image).cut_color("blue")
    canvas_set(image)

def redplus():
    global image
    image=Filtre(image).red_plus(+10)
    canvas_set(image)

def redmoins():
    global image
    image=Filtre(image).red_plus(-10)
    canvas_set(image)
    
def greenplus():
    global image
    image=Filtre(image).green_plus(+10)
    canvas_set(image)

def greenmoins():
    global image
    image=Filtre(image).green_plus(-10)
    canvas_set(image)
    
def blueplus():
    global image
    image=Filtre(image).blue_plus(+10)
    canvas_set(image)

def bluemoins():
    global image
    image=Filtre(image).blue_plus(-10)
    canvas_set(image)
    
def rgb_form():
    root = Tk()
    root.minsize(100,100)
    redButtonPlus = Button(root,text="Red +", width=15, command=redplus)
    redButtonPlus.grid(row = 0, column = 0 , sticky = W, pady = 2) 
    redButtonMoins = Button(root,text="Red -", width=15, command=redmoins)
    redButtonMoins.grid(row = 0, column = 1, sticky = E, pady = 2) 
    greenButtonPlus = Button(root,text="Green +", width=15, command=greenplus)
    greenButtonPlus.grid(row = 1 ,column = 0, sticky = W, pady = 2) 
    greenButtonMoins = Button(root,text="Green -", width=15, command=greenmoins)
    greenButtonMoins.grid(row = 1, column = 1, sticky = E, pady = 2) 
    blueButtonPlus = Button(root,text="Blue +", width=15, command=blueplus)
    blueButtonPlus.grid(row = 2, column = 0, sticky = W, pady = 2) 
    greenButtonMoins = Button(root,text="Blue -", width=15, command=bluemoins)
    greenButtonMoins.grid(row = 2, column = 1, sticky = E, pady = 2) 
    root.mainloop()
    
image = Image.new("RGB", (500, 400), "white")
draw  = ImageDraw.Draw(image)

fenetre = Tk()
fenetre.title("Image Processor 1.0")
fenetre.state("zoomed")
# tool bar
toolbar = Frame(fenetre, bd=1, relief=RAISED)
toolbar.grid(row = 0, column = 1, sticky = W, pady = 2) 

toolbar2 = Frame(fenetre, width=50, height=600)
toolbar2.grid(row = 2, column = 0)

rightframe = Frame(fenetre, width=300, height=600, background="black")
rightframe.grid(row = 2, column = 1)

# canvas
canvas = Canvas(rightframe, width=500, height= 400 , bg="white")
canvas.grid(row = 2, column = 0,  pady = 20, padx = 20)
canvas.config(cursor="dot")
canvas.bind('<B1-Motion>',mousemoveclick)
canvas.bind('<Motion>',mousemove)
canvas.bind('<Button-1>',mouseclick)

# canvas 2
canvas2 = Canvas(rightframe, width=500, height= 400 , bg="white")
canvas2.grid(row = 2, column = 1,  pady = 20, padx = 20)

statutbar = Frame(fenetre, width=300, height=600 )
statutbar.grid(row = 3, column = 1)

sizelabel = Label(statutbar, text= "Width: 500 Height: 400")
sizelabel.pack(side=RIGHT)

cursorposition = Label(statutbar, text= "X: 0  Y: 0")
cursorposition.pack(side=RIGHT)

commandlabel = Label(statutbar, text= "Command: Draw")
commandlabel.pack(side=RIGHT)

img1 = ImageTk.PhotoImage(Image.open("icons/exit.png"))
exitButton = Button(toolbar, image=img1, relief=FLAT,command=fenetre.destroy)
exitButton.pack(side=RIGHT, padx=2, pady=2)

lf_img0 = ImageTk.PhotoImage(Image.open("icons/reset.png"))
resetButton = Button(toolbar, image=lf_img0, relief=FLAT,command=reset)
resetButton.pack(side=RIGHT, padx=2, pady=2)

lf_img55 = ImageTk.PhotoImage(Image.open("icons/cut_blue.png"))
resetButton = Button(toolbar, image=lf_img55, relief=FLAT,command=cut_blue)
resetButton.pack(side=RIGHT, padx=2, pady=2)

lf_img56 = ImageTk.PhotoImage(Image.open("icons/cut_green.png"))
resetButton = Button(toolbar, image=lf_img56, relief=FLAT,command=cut_green)
resetButton.pack(side=RIGHT, padx=2, pady=2)

lf_img57 = ImageTk.PhotoImage(Image.open("icons/cut_red.png"))
resetButton = Button(toolbar, image=lf_img57, relief=FLAT,command=cut_red)
resetButton.pack(side=RIGHT, padx=2, pady=2)

rgbButton = Button(toolbar, text="RGB", relief=FLAT,command=rgb_form)
rgbButton.pack(side=RIGHT, padx=2, pady=2)


lf_img00 = ImageTk.PhotoImage(Image.open("icons/mirror.png"))
resetButton = Button(toolbar, image=lf_img00, relief=FLAT,command=mirror)
resetButton.pack(side=RIGHT, padx=2, pady=2)

lf_img01 = ImageTk.PhotoImage(Image.open("icons/rotation.png"))
resetButton = Button(toolbar, image=lf_img01, relief=FLAT,command=rotation)
resetButton.pack(side=RIGHT, padx=2, pady=2)

lf_img5a5 = ImageTk.PhotoImage(Image.open("icons/select.png"))
selectButton = Button(toolbar2, image=lf_img5a5, relief=FLAT, command=select)
selectButton.pack( padx=2, pady=2)

lf_img1 = ImageTk.PhotoImage(Image.open("icons/pencil.png"))
exitButton = Button(toolbar2, image=lf_img1, relief=FLAT, command=paint)
exitButton.pack( padx=2, pady=2)

lf_img2 = ImageTk.PhotoImage(Image.open("icons/rubber.png"))
exitButton = Button(toolbar2, image=lf_img2, relief=FLAT,command=errase)
exitButton.pack( padx=2, pady=2)

lf_img3 = ImageTk.PhotoImage(Image.open("icons/color.jpg"))
colorButton = Button(toolbar2, fg='red',image=lf_img3, relief=FLAT,command=askingcolor)
colorButton.pack( padx=2, pady=2)

lf_img4 = ImageTk.PhotoImage(Image.open("icons/crop.png"))
colorButton = Button(toolbar2, fg='red',image=lf_img4, relief=FLAT,command=imgcrop)
colorButton.pack(padx=2, pady=2)

lf_img5 = ImageTk.PhotoImage(Image.open("icons/text.png"))
colorButton = Button(toolbar2, fg='red',image=lf_img5, relief=FLAT,command=imgtext)
colorButton.pack(padx=2, pady=2)

lf_img25 = ImageTk.PhotoImage(Image.open("icons/font.png"))
colorButton = Button(toolbar2, fg='red',image=lf_img25, relief=FLAT,command=askingfont)
colorButton.pack(padx=2, pady=2)

img223 = ImageTk.PhotoImage(Image.open("icons/inverse.png"))
invButton = Button(toolbar, image=img223, relief=FLAT,command=imgreverse)
invButton.pack(side=RIGHT, padx=2, pady=2)

img222 = ImageTk.PhotoImage(Image.open("icons/graylevel.png"))
bgrButton = Button(toolbar, image=img222, relief=FLAT,command=imggraylevel)
bgrButton.pack(side=RIGHT, padx=2, pady=2)

img22 = ImageTk.PhotoImage(Image.open("icons/blackwhite.png"))
bwButton = Button(toolbar, image=img22, relief=FLAT,command=imgbin)
bwButton.pack(side=RIGHT, padx=2, pady=2)

img2 = ImageTk.PhotoImage(Image.open("icons/brightness_plus.png"))
bpButton = Button(toolbar, image=img2, relief=FLAT,command=imgbrightnessplus)
bpButton.pack(side=RIGHT, padx=2, pady=2)

img3 = ImageTk.PhotoImage(Image.open("icons/brightness_moins.png"))
bmButton = Button(toolbar, image=img3, relief=FLAT, command=imgbrightnessmoins)
bmButton.pack(side=RIGHT, padx=2, pady=2)

img4 = ImageTk.PhotoImage(Image.open("icons/save.png"))
sButton = Button(toolbar, image=img4, relief=FLAT, command=saveimgas)
sButton.pack(side=RIGHT, padx=2, pady=2)

img5 = ImageTk.PhotoImage(Image.open("icons/open.png"))
OButton = Button(toolbar, image=img5, relief=FLAT, command=openimg)
OButton.pack(side=RIGHT, padx=2, pady=2)

img77 = ImageTk.PhotoImage(Image.open("icons/new.png"))
OButton = Button(toolbar, image=img77, relief=FLAT, command=newimg)
OButton.pack(side=RIGHT, padx=2, pady=2)
    
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Ouvrir", command=openimg)
menu1.add_command(label="Save", command=about)
menu1.add_command(label="Save as", command=saveimgas)
menu1.add_separator()
menu1.add_command(label="Exit", command=fenetre.destroy)
menubar.add_cascade(label="File", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Cut", command=about)
menu2.add_command(label="Copy", command=about)
menu2.add_command(label="Paste", command=about)
menubar.add_cascade(label="Edit", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Hide original image", command=hide_canvas2)
menubar.add_cascade(label="Display", menu=menu3)

menu4 = Menu(menubar, tearoff=0)
menu4.add_command(label="Black and white", command=imgbin)
menu4.add_command(label="Gray level", command=imggraylevel)
menubar.add_cascade(label="Filtre", menu=menu4)

menu5 = Menu(menubar, tearoff=0)
menu5.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=menu5)

fenetre.config(menu=menubar)


fenetre.mainloop()