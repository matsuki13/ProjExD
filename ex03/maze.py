import tkinter
import tkinter as Tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc(): #こうかとんの移動関連
    global cx, cy, mx, my, lst
    delta = { # キー：押されているキーkey/値：移動幅リスト[x,y]
        ""     :[0, 0],
        "Up"   :[0, -1],
        "Down" :[0, +1],
        "Left" :[-1, 0],
        "Right":[+1, 0],
    }
    if lst[my+delta[key][1]][mx+delta[key][0]] == 0:
        mx =  mx+delta[key][0]
        my =  my+delta[key][1]
        cx, cy = (mx*100)+50, (my*100)+50
        canvas.coords("tori", cx, cy)
    elif lst[my][mx] == 1:
        pass

         
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("迷えるこうかとん")

    key = ""

    canvas = Tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    lst = maze_maker.make_maze(15, 9)
    
    maze_maker.show_maze(canvas, lst)


    tori = Tk.PhotoImage(file="fig/5.png")
    cx, cy = 150, 150
    canvas.create_image(cx, cy, image=tori, tag="tori")

    mx, my = 1, 1
    cx, cy = (mx*100)+50, (my*100)+50


    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    root.mainloop()