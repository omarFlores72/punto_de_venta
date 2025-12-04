from tkinter import*
from tkinter import tkk, messagebox
import tkinter as tk
from aplicacion_modulos.dashboard import Dashboard
from aplicacion_modulos.ventas import Ventas

class Container(tk.frame):
    def __init__(self, padre, controlador, user=None):
        super().__init__(padre)
        self.controlador = controlador
        self.user = user
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.widget()
        self.frames = {}
        self.buttons = []

        for i in (Dashboard, Ventas,):
            frame = i(self)
            self.frames[i] = frame
            frame.pack()
            frame.config(bg="#dcdcdc", highlightbackground="gray", highlight=1)
            frame.place(x=200, y=50, width=900, height=600)
        self.sh


    def show_frames(self, container):
        frame = self.frames[container]
        frame.tk

    
    def widget(self):
        label = Label(self, text="frame principal")
        label.pack()
