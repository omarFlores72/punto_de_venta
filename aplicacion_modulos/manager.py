from tkinter import*
from tkinter import tkk, messagebox

class Manager(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("sistema de punto de venta")
        self.resizable(False, False)
        self.geometry("100*650+120+50")

        #contenedor para los modulos adicionales(inventario,clientes, etc)  
        self.container = Frame(self, bg="#dcdcdc") #frame es un recuadro para ingresar dartos, informacion, etc
        self.container.pack(fill=BOTH, expand=True)
        #crear un diciconario
        self.frames = {}
        #3 tipos de ventanas; 1 clientes; login; registro
        for i in (Container):
            frame = i(self.container, self) #i porque se crea una instancia del controlador 
            self.frames[i] = frame #permite cambiar entre los 3 contenedores 
            
    def show_frame(self, frame_class, user=None):
        frame = self.frames[frame_class]

        if user is not None:
            frame.set_user(user)

        frame.tkraise() #perite ver la aprte visual

    def main():
        app = Manager()
        app.mainloop() #para mantener la interfaz abierta

    if __name__ == " __main__": #para verificar que el archivo se este ejecutando
        main()
