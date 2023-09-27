#Author = Sachin Jain
#Date - 26th May 2023
#file - game.py
#description - fifteen puzzle as GUi

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
from random import choice
import numpy as np

def clickButton(button):

    if button.cget("text") != " ":
        if button.cget("text") == "shuffle":
            shuffle(100)
            return

        if tiles.is_valid_move(int(button.cget("text"))):

            tiles.update(int(button.cget("text")))
            buttonRow = button.grid_info()['row']
            buttonColumn = button.grid_info()['column']
            emptyRow = button16.grid_info()['row']
            emptyColumn = button16.grid_info()['column']
            button.grid_forget()
            button16.grid_forget()
            button.grid(row=emptyRow, column=emptyColumn)
            button16.grid(row = buttonRow, column= buttonColumn)

        if tiles.is_solved():
            exit()



def shuffle(count):
    tiles.shuffle(count)
    j = 0
    for i in tiles.tiles:
        if i == 0:
            button = gui.nametowidget("16")
            button.grid(row=j // 4, column=j % 4)
        else:
            button = gui.nametowidget(str(i))
            button.grid(row=j // 4, column=j % 4)
        j += 1



if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    text1 = StringVar()
    text1.set('1')
    name1 = 1
    button1 = Button(gui, textvariable=text1, name=str(name1),
                      bg='white', fg='black', font=font, height=2, width=5,
                      command = lambda : clickButton(button1))
    button1.configure(bg='coral')
    button1.grid(row=0, column=0)

    text2 = StringVar()
    text2.set('2')
    name2 = 2
    button2 = Button(gui, textvariable=text2 , name=str(name2),
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda : clickButton(button2))
    button2.configure(bg='coral')
    button2.grid(row=0, column=1)

    text3 = StringVar()
    text3.set('3')
    name3 = '3'
    button3 = Button(gui, textvariable=text3, name=name3,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda : clickButton(button3))
    button3.configure(bg='coral')
    button3.grid(row=0, column=2)

    text4 = StringVar()
    text4.set('4')
    name4 = '4'
    button4 = Button(gui, textvariable=text4, name=name4,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda :clickButton(button4))
    button4.configure(bg='coral')
    button4.grid(row=0, column=3)

    text5 = StringVar()
    text5.set('5')
    name5 = '5'
    button5 = Button(gui, textvariable=text5, name=name5,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda :clickButton(button5))
    button5.configure(bg='coral')
    button5.grid(row=1, column=0)

    text6 = StringVar()
    text6.set('6')
    name6 = '6'
    button6 = Button(gui, textvariable=text6, name=name6,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda :clickButton(button6))
    button6.configure(bg='coral')
    button6.grid(row=1, column=1)

    text7 = StringVar()
    text7.set('7')
    name7 = '7'
    button7 = Button(gui, textvariable=text7, name=name7,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda :clickButton(button7))
    button7.configure(bg='coral')
    button7.grid(row=1, column=2)

    text8 = StringVar()
    text8.set('8')
    name8 = '8'
    button8 = Button(gui, textvariable=text8, name=name8,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda :clickButton(button8))
    button8.configure(bg='coral')
    button8.grid(row=1, column=3)

    text9 = StringVar()
    text9.set('9')
    name9 = '9'
    button9 = Button(gui, textvariable=text9, name=name9,
                     bg='white', fg='black', font=font,
                     height=2, width=5, command=lambda :clickButton(button9))
    button9.configure(bg='coral')
    button9.grid(row=2, column=0)

    text10 = StringVar()
    text10.set('10')
    name10 = '10'
    button10 = Button(gui, textvariable=text10, name=name10,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda :clickButton(button10))
    button10.configure(bg='coral')
    button10.grid(row=2, column=1)

    text11 = StringVar()
    text11.set('11')
    name11 = '11'
    button11 = Button(gui, textvariable=text11, name=name11,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda :clickButton(button11))
    button11.configure(bg='coral')
    button11.grid(row=2, column=2)

    text12 = StringVar()
    text12.set('12')
    name12 = '12'
    button12 = Button(gui, textvariable=text12, name=name12,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda :clickButton(button12))
    button12.configure(bg='coral')
    button12.grid(row=2, column=3)

    text13 = StringVar()
    text13.set('13')
    name13 = '13'
    button13 = Button(gui, textvariable=text13, name=name13,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda :clickButton(button13))
    button13.configure(bg='coral')
    button13.grid(row=3, column=0)

    text14 = StringVar()
    text14.set('14')
    name14 = '14'
    button14 = Button(gui, textvariable=text14, name=name14,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda :clickButton(button14))
    button14.configure(bg='coral')
    button14.grid(row=3, column=1)

    text15 = StringVar()
    text15.set('15')
    name15 = '15'
    button15 = Button(gui, textvariable=text15, name=name15,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda :clickButton(button15))
    button15.configure(bg='coral')
    button15.grid(row=3, column=2)

    text16 = StringVar()
    text16.set(' ')
    name16 = '16'
    button16 = Button(gui, textvariable=text16, name=name16,
                      bg='white', fg='black', font=font,
                      height=2, width=5, command=lambda: clickButton(button16))
    button16.configure(bg='white')
    button16.grid(row=3, column=3)

    text17 = StringVar()
    text17.set('shuffle')
    name17 = 'shuffle'
    button17 = Button(gui, textvariable=text17, name=name17,
                      bg='white', fg='black', font=font,
                      height=2, width=20, command=lambda: clickButton(button17))
    button17.configure(bg='white')
    button17.grid(row=4, columnspan=5)

    gui.mainloop()
