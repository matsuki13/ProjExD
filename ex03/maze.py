import tkinter
import tkinter as Tk


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("迷えるこうかとん")

    canvas = Tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    tori = Tk.PhotoImage(file="fig/5.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=tori, tag="tori")
    root.mainloop()