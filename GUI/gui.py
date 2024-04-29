import customtkinter as ct
import easygui
from organizer import *


def organize():
    create_path()
    organize_files()


def select_folder(l3):
    global source_path
    source_path = easygui.diropenbox()
    l3.configure(text=source_path)


def initial(root):
    l1=ct.CTkLabel(root, text='Seiri - Desktop Organizer')
    l1.pack(pady=20)

    l2=ct.CTkLabel(root, text='Selected Folder:')
    l2.pack()
    l3=ct.CTkLabel(root, text='None')
    l3.pack()

    b1=ct.CTkButton(root, text='Select Folder', command=lambda:select_folder(l3))
    b1.pack(pady=20)

    b2=ct.CTkButton(root, text='Organize', command=organize)
    b2.pack()

    print(1)

def root():
    root = ct.CTk()
    root.geometry("400x350")
    root.title("Seiri - Desktop Organizer")

    
    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()