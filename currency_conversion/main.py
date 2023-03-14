import tkinter

# screen
window = tkinter.Tk()
window.title("Moje první okno")
window.minsize(width=500, height=400)
window.resizable(False, False)
window.iconbitmap("icon.png")
window.config(bg="#5b0080")

window2 = tkinter.Tk()
window2.title("Moje druhé okno")
# window2.minsize(width=300, height=350)
window2.geometry("300x400+800+100")
window2.resizable(False, False)
window2.config(bg="#58d330")



# main cycle
window.mainloop()
