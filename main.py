import tkinter as tk
import numpy as np
import matplotlib as plt

#from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.button import Button
#from kivy.uix.boxlayout import BoxLayout

class MyGUI: 
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="Hello World!")
        self.button = tk.Button(text="Click me!")
        self.button.pack()
        # Start the mainloop
        self.root.mainloop()
    
if __name__ == "__main__":
    MyGUI().run()

def calc_voltage(current,sys_res):
    return current*sys_res

def change_voltage(suggested):
   voltage = suggested
