from tkinter import *
from PIL import ImageTk
from PIL import Image
import random

class MemeGenerator:
  WINDOW_WIDTH = 490
  WINDOW_HEIGHT = 430


  def __init__(self, master):

    self.__win = master

    self.__win.title("I can has memes?")

    expanding = Image.open("expanding.jpg")
    expandingResize = expanding.resize((300, 300))

    expandingPhoto = ImageTk.PhotoImage(expandingResize)

    self.__buttonOne = Button(self.__win, image=expandingPhoto, command = self.openExpanding)
    self.__buttonOne.image = expandingPhoto
    self.__buttonOne.grid(row=1, column=1)

    bearcat = Image.open("bearcat.png")
    bearcatPhoto = ImageTk.PhotoImage(bearcat)

    self.__buttonTwo = Button(self.__win, image = bearcatPhoto, command = self.openBing)
    self.__buttonTwo.image = bearcatPhoto
    self.__buttonTwo.grid(row=1, column=2)

    arthur = Image.open("arthur.jpg")
    arthurResize = arthur.resize((300,300))
    arthurPhoto = ImageTk.PhotoImage(arthurResize)

    self.__buttonThree = Button(self.__win, image = arthurPhoto, command = self.openArthur)
    self.__buttonThree.image = arthurPhoto
    self.__buttonThree.grid(row=1, column=3)

    salt = Image.open("saltbae.jpg")
    saltResize = salt.resize((300,300))
    saltPhoto = ImageTk.PhotoImage(saltResize)

    self.__buttonFour = Button(self.__win, image = saltPhoto, command = self.openSalt)
    self.__buttonFour.image = saltPhoto
    self.__buttonFour.grid(row=1, column=4)

    bingDoor = Image.open("bingdoor.jpg")
    bingDoorPhoto = ImageTk.PhotoImage(bingDoor)

    self.__buttonFive = Button(self.__win, image = bingDoorPhoto, command = self.openDoor)
    self.__buttonFive.image = bingDoorPhoto
    self.__buttonFive.grid(row=1, column=5)

    random = Image.open("random.jpeg")
    randomResize = random.resize((300, 300))
    randomPhoto = ImageTk.PhotoImage(randomResize)

    self.__buttonSix = Button(self.__win, image = randomPhoto, command = self.openRandom)
    self.__buttonSix.image = randomPhoto
    self.__buttonSix.grid(row=1, column=6)

    self.__mainScreenWidth = self.__win.winfo_screenwidth()
    self.__mainScreenHeight = self.__win.winfo_screenheight()
    self.__mainXCoord = (self.__mainScreenWidth / 2) - (
      1735 / 2)
    self.__mainYCoord = (self.__mainScreenHeight / 2) - (
      308 / 2)
    self.__win.geometry("%dx%d+%d+%d" % (1735, 308, self.__mainXCoord, self.__mainYCoord))

  def openExpanding(self):
    root.withdraw()
    expandingMeme()

  def openDoor(self):
    root.withdraw()
    doorMeme()

  def openBing(self):
    root.withdraw()
    bingMeme()

  def openArthur(self):
    root.withdraw()
    arthurMeme()

  def openSalt(self):
    root.withdraw()
    saltMeme()

  def openRandom(self):
    root.withdraw()
    randomMeme()

class expandingMeme:

  def __init__(self):

    self.__expandingWindow = Toplevel()
    self.__expandingWindow.title("Expanding Brain")
    myfile = open("expandingbrain.txt", "r")
    a = []
    for line in myfile:
      a.append(myfile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    expanding = Image.open(pic)
    x, y = expanding.size
    if y > 750:
      expanding = expanding.resize((700,884))
    center(self.__expandingWindow, expanding)

    expandingPhoto = ImageTk.PhotoImage(expanding)
    self.__expandingMeme = Button(self.__expandingWindow, image = expandingPhoto, command = self.exit)
    self.__expandingMeme.image = expandingPhoto
    self.__expandingMeme.grid()

    self.__expandingWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__expandingWindow.destroy()
    root.deiconify()

class saltMeme:

  def __init__(self):

    self.__saltWindow = Toplevel()
    self.__saltWindow.title("Salt Bae")
    myfile = open("meme1.txt", "r")
    a = []
    for line in myfile:
      a.append(myfile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    salt = Image.open(pic)
    if salt.size > (1024, 768):
      salt = salt.resize((1024, 768))
    center(self.__saltWindow, salt)
    saltResize = salt.resize((1000, 1000))

    saltPhoto = ImageTk.PhotoImage(salt)
    self.__saltMeme = Button(self.__saltWindow, image=saltPhoto,
                              command=self.exit)
    self.__saltMeme.image = saltPhoto
    self.__saltMeme.grid()

    self.__saltWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__sonWindow.destroy()
    root.deiconify()

class arthurMeme:

  def __init__(self):

    self.__arthurWindow = Toplevel()
    self.__arthurWindow.title("Don't ever talk to me or my son again!")
    myfile = open("arthurmemes.txt", "r")
    a = []
    for line in myfile:
      a.append(myfile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    arthur = Image.open(pic)
    if arthur.size > (1024, 768):
      arthur = arthur.resize((1024, 768))
    center(self.__arthurWindow, arthur)
    arthurPhoto = ImageTk.PhotoImage(arthur)
    self.__arthurMeme = Button(self.__arthurWindow, image=arthurPhoto,
                            command=self.exit)
    self.__arthurMeme.image = arthurPhoto
    self.__arthurMeme.grid()

    self.__arthurWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__arthurWindow.destroy()
    root.deiconify()

class bingMeme:

  def __init__(self):

    self.__bingWindow = Toplevel()
    self.__bingWindow.title("Binghamton Memes")
    bingFile = open("binghamton.txt", "r")
    a = []
    for line in bingFile:
      a.append(bingFile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    bing = Image.open(pic)
    if (bing.size > (1080, 780)):
      bing = bing.resize((1024, 768))

    center(self.__bingWindow, bing)
    bingPhoto = ImageTk.PhotoImage(bing)
    self.__bingMeme = Button(self.__bingWindow, image=bingPhoto,
                            command=self.exit)
    self.__bingMeme.image = bingPhoto
    self.__bingMeme.grid()

    self.__bingWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__bingWindow.destroy()
    root.deiconify()

class rollMeme:

  def __init__(self):

    self.__rollWindow = Toplevel()
    self.__rollWindow.title("Roll Safe")
    myfile = open("meme1.txt", "r")
    a = []
    for line in myfile:
      a.append(myfile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    roll = Image.open(pic)
    if roll.size > (1024, 768):
      roll = roll.resize((1024, 768))

    rollPhoto = ImageTk.PhotoImage(roll)
    self.__rollMeme = Button(self.__rollWindow, image=rollPhoto,
                            command=self.exit)
    self.__rollMeme.image = rollPhoto
    self.__rollMeme.grid()

    self.__rollWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__rollWindow.destroy()
    root.deiconify()

class doorMeme:

  def __init__(self):

    self.__doorWindow = Toplevel()
    self.__doorWindow.title("Binghamton Doors")
    doorFile = open("doorsmeme.txt", "r")
    a = []
    for line in doorFile:
      a.append(doorFile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    door = Image.open(pic)
    if door.size > (1024, 768):
      door = door.resize((1024, 768))

    doorPhoto = ImageTk.PhotoImage(door)
    self.__doorMeme = Button(self.__doorWindow, image=doorPhoto,
                            command=self.exit)
    self.__doorMeme.image = doorPhoto
    self.__doorMeme.grid()

    self.__doorWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__doorWindow.destroy()
    root.deiconify()

class randomMeme:

  def __init__(self):

    self.__randomWindow = Toplevel()
    self.__randomWindow.title("Random")
    myfile = open("random.txt", "r")
    a = []
    for line in myfile:
      a.append(myfile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    randomPic = Image.open(pic)
    if randomPic.size > (1024, 768):
      randomPic = randomPic.resize((1024, 768))

    center(self.__randomWindow, randomPic)
    randomPhoto = ImageTk.PhotoImage(randomPic)

    self.__randomMeme = Button(self.__randomWindow, image=randomPhoto,
                            command=self.exit)
    self.__randomMeme.image = randomPhoto
    self.__randomMeme.grid()

    self.__randomWindow.protocol('WM_DELETE_WINDOW', self.exit)

  def exit(self):
    self.__randomWindow.destroy()
    root.deiconify()

def center(window, im):
  mainScreenWidth = window.winfo_screenwidth()
  mainScreenHeight = window.winfo_screenheight()
  x, y = im.size
  mainXCoord = (mainScreenWidth / 2) - (x / 2)
  mainYCoord = (mainScreenHeight / 2) - (y / 2)
  window.geometry("%dx%d+%d+%d" % (x, y, mainXCoord, mainYCoord))

root = Tk()
MemeGenerator(root)
root.mainloop()



