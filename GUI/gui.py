import customtkinter as ct


def initial(root):
    l1=ct.CTkLabel(root, text='Seiri - Desktop Organizer')
    l1.pack(pady=20)

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