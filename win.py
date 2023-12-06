from tkinter import* #importa o arquivo 

window = Tk()
window.title("Welcome nerds")
window.geometry('350x200')
lbl = Label(window, text = "Ola")
lbl.pack()
btn = Button(window, text="Clique aqui")
btn.pack()
window.mainloop()