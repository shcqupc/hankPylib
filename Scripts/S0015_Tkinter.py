#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tkinter import *
import webbrowser as wbr

class App:

    def __init__(self, master):

        master.title("CAS Kits")
        master.geometry("400x400+200+50")
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=RIGHT)

        self.hi_there = Button(frame, text="Login", command=openie2)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")

def openie1():
    #create capabilities
    capabilities = DesiredCapabilities.INTERNETEXPLORER

    #delete platform and version keys
    capabilities.pop("platform", None)
    capabilities.pop("version", None)

    #start an instance of IE
    driver = webdriver.Ie(executable_path="C:\Program Files\Internet Explorer\iexplore.exe", capabilities=capabilities)
    driver.get("https://www.baidu.com/")

def openie2():
    wbr.open("https://10.218.113.21:6011/forms/frmservlet?config=cas_sit01")
    
root = Tk()

app = App(root)

root.mainloop()
root.destroy()
