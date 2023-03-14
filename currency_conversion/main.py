import tkinter

# screen
window = tkinter.Tk()
window.title("Moje první okno")
window.minsize(width=500, height=400)
window.resizable(True, True)
window.iconbitmap("icon.png")
window.config(bg="#1b073c")





# main cycle
window.mainloop()
