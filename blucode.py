import tkinter as tk

#pretty esencial v
def makeWindow(name="untitled", overwrite="blucode app:"):
    root = tk.Tk()
    root.title(" ".join([overwrite, name]))
    root.geometry("400x300")
    return root
    
def bgColor(window, color):
    window.config(bg=color)

def base():
    print("clicked!")
#UI v
def makeButton(window, btnText, fontt="Arial", cmd=base, color="black", x="", y=""):
    current_bg = window.cget("bg")
    btn = tk.Button(window, text=btnText, font=(fontt, 16), command=cmd, bg=current_bg, fg=color )
    if x != "" and y != "":
        btn.place(x, y)
    else:
        btn.pack(pady=10)
    
def makeText(window, mesage, fontt="Arial", color="black", x="", y=""):
    current_bg = window.cget("bg")
    label = tk.Label(window, text=mesage, font=(fontt, 16), bg=current_bg, fg=color)
    if x != "" and y != "":
        label.place(x, y)
    else:
        label.pack(pady=10)
    
def  makeImage(window, file_Path, size=1, x="", y=""):
    img = tk.PhotoImage(file=file_Path)
    size = int(size)
    if size < 1:
        img = img.subsample(abs(size), abs(size))
    elif size > 1:
        img  = img.zoom(size, size)
    label = tk.Label(window, image=img, bg=window.cget("bg"))
    label.image = img
    if x != "" and y != "":
        label.place(x, y)
    else:
        label.pack(pady=10)
    return label

#inputs v
def makeInput(window, fontt="Arial", widthh=20, x="", y=""):
    entryBox = tk.Entry(window, font=(fontt, 16), width=widthh)
    if x != "" and y != "":
        entryBox.place(x, y)
    else:
        entryBox.pack(pady=10)
    return entryBox

def makeCheckbox(window, textt, fontt="Arial", x="", y=""):
    current_bg = window.cget("bg")
    var = tk.BooleanVar(value=False)
    checkbox = tk.Checkbutton(window, text=textt, font=(fontt, 14), variable=var, bg=current_bg, activebackground=current_bg)
    if x != "" and y != "":
        checkbox.place(x, y)
    else:
        checkbox.pack(pady=10)
    return var
def makeScale(window, start=1, end=100, x="", y=""):
    current_bg = window.cget("bg")
    scale = tk.Scale(
        window,
        from_=start,
        to=end,
        orient="horizontal",
        font=("Arial", 12),
        bg=current_bg,
        highlightthickness=0,
        length=250
    )
    if x != "" and y != "":
        scale.place(x, y)
    else:
        scale.pack(pady=10)
    return scale
#other v
def erase(itemm):
    itemm.destroy()

def clear(window):
    for item in window.winfo_children():
        item.destroy()
        window.update()
        
def end(window):
    try:
        window.destroy()
    except:
        pass
    
def appLink(window, filePath):
    import subprocess as subpro
    import sys
    try:
        window.destroy()
    except:
        pass
    subpro.Popen([sys.executable, filePath])
    sys.exit()
    
        
def run(window):
    window.mainloop()
    
#this ones just for fun :)
def fallingText(window, textt="🎉", count=30):
    import random
    current_bg = window.cget("bg")
    active_particles = []
    for _ in range(count):
        lbl = tk.Label(window, text=textt, font=("Arial", 20), bg=current_bg)
        start_x = random.randint(10, 350)
        start_y = random.randint(-150, -30)
        lbl.place(x=start_x, y=start_y)
        speed = random .randint(3, 7)
        active_particles.append({"widget": lbl, "x": start_x, "y": start_y, "speed": speed})
    def drop_loop():
        still_falling = False
        window_hight = window.winfo_height()
        for p in active_particles:
            if p["y"] < window_hight:
                p["y"] += p["speed"]
                p["x"] += random.choice([-2, 0, 2])
                p["widget"].place(x=p["x"], y=p["y"])
                still_falling = True
            else:
                p["widget"].destroy()
        if still_falling:
            window.after(25, drop_loop)
        
    drop_loop()