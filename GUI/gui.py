import customtkinter as ct
import easygui
from organizer import create_path, organize_files

def organize(check_var):
    option = check_var.get()
    if option == 'on':
        while True:
            create_path()
            organize_files(source_path)
    else:
        create_path()
        organize_files(source_path)


def select_folder(l3):
    global source_path
    source_path = easygui.diropenbox()
    l3.configure(text=source_path)


def initial(root):
    check_var = ct.StringVar(value='off')
    l1=ct.CTkLabel(root, text='Seiri - Desktop Organizer')
    l1.pack(pady=20)

    l2=ct.CTkLabel(root, text='Selected Folder:')
    l2.pack()
    l3=ct.CTkLabel(root, text='None')
    l3.pack()

    c1 = ct.CTkCheckBox(root, text='Run continuously', checkbox_width=15, checkbox_height=15, corner_radius=0, border_width=2, variable=check_var, onvalue='on', offvalue='off')
    c1.pack(pady=10)

    b1=ct.CTkButton(root, text='Select Folder', command=lambda:select_folder(l3))
    b1.pack(pady=20)

    b2=ct.CTkButton(root, text='Organize', command=lambda:organize(check_var))
    b2.pack()

def root():
    root = ct.CTk()
    root.geometry("400x350")
    root.title("Seiri - Desktop Organizer")
    root.iconbitmap(r'Visual\seiri.ico')

    
    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

root()