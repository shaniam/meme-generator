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

    badLuckBrian = Image.open("badluckbrian.jpg")
    badLuckBrianResize = badLuckBrian.resize((300, 300))

    badLuckBrianPhoto = ImageTk.PhotoImage(badLuckBrianResize)

    self.__buttonOne = Button(self.__win, image=badLuckBrianPhoto, command = self.openBrian)
    self.__buttonOne.image = badLuckBrianPhoto
    self.__buttonOne.grid(row=1, column=1)

    bearcat = Image.open("bearcat.png")
    bearcatPhoto = ImageTk.PhotoImage(bearcat)

    self.__buttonTwo = Button(self.__win, image = bearcatPhoto)
    self.__buttonTwo.image = bearcatPhoto
    self.__buttonTwo.grid(row=1, column=2)

    tarnation = Image.open("tarnation.jpg")
    tarnationPhoto = ImageTk.PhotoImage(tarnation)

    self.__buttonThree = Button(self.__win, image = tarnationPhoto)
    self.__buttonThree.image = tarnationPhoto
    self.__buttonThree.grid(row=1, column=3)

    son = Image.open("son.png")
    sonResize = son.resize((300,300))
    sonPhoto = ImageTk.PhotoImage(sonResize)

    self.__buttonFour = Button(self.__win, image = sonPhoto)
    self.__buttonFour.image = sonPhoto
    self.__buttonFour.grid(row=1, column=4)

    bingDoor = Image.open("bingdoor.jpg")
    bingDoorPhoto = ImageTk.PhotoImage(bingDoor)

    self.__buttonFive = Button(self.__win, image = bingDoorPhoto)
    self.__buttonFive.image = bingDoorPhoto
    self.__buttonFive.grid(row=1, column=5)

    self.__buttonSix = Button(self.__win,
                              text="Random", fg="purple")
    self.__buttonSix.grid(row=1, column=6)

  def openBrian(self):
    root.withdraw()
    brianMeme()


class brianMeme():

  def __init__(self):

    self.__brianWindow = Toplevel()
    self.__brianWindow.title("Bad Luck Brian")
    self.__brianWindowWidth = self.__brianWindow.winfo_screenwidth()
    self.__brianWindowHeight = self.__brianWindow.winfo_screenheight()
    myfile = open("meme1.txt", "r")
    a = []
    for line in myfile:
        a.append(myfile.readline(10))
    a.pop()
    x = random.randrange(len(a))
    pic = a[x]
    badLuckBrian = Image.open(pic)
    badLuckBrianResize = badLuckBrian.resize((300, 300))

    badLuckBrianPhoto = ImageTk.PhotoImage(badLuckBrianResize)
    self.__brianMeme = Button(self.__brianWindow, image = badLuckBrianPhoto, command = self.exit)
    self.__brianMeme.image = badLuckBrianPhoto
    self.__brianMeme.grid()

  def exit(self):
    self.__brianWindow.destroy()
    root.deiconify()

root = Tk()
MemeGenerator(root)
root.mainloop()
