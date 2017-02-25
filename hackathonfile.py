import turtle
import random
import PIL

def main():
    wn = turtle.Screen()
    i = random.randrange(4)
    if(i == 0):
        myfile = open("meme1.txt", "r")
        a = []
        for line in myfile:
            a.append(myfile.readline(10))
        a.pop()
        print(a)
        x = random.randrange(len(a))
        pic = a[x]
        print("test1")
        wn.bgpic(pic)

    elif(i == 1):
        myfile = open("meme1.txt", "r")
        a = []
        for line in myfile:
            a.append(myfile.readline(10))
        a.pop()
        print(a)
        x = random.randrange(len(a))
        pic = a[x]
        print("test1")
        wn.bgpic(pic)
    elif(i == 2):
        myfile = open("meme1.txt", "r")
        a = []
        for line in myfile:
            a.append(myfile.readline(10))
        a.pop()
        print(a)
        x = random.randrange(len(a))
        pic = a[x]
        print("test1")
        wn.bgpic(pic)
    elif(i == 3):
        myfile = open("meme1.txt", "r")
        a = []
        for line in myfile:
            a.append(myfile.readline(10))
        a.pop()
        print(a)
        x = random.randrange(len(a))
        pic = a[x]
        print("test1")
        wn.bgpic(pic)

    wn.exitonclick()
main()
