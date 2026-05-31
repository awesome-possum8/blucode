import blucode as blu

app = blu.makeWindow("demo!")
blu.bgColor(app, "#D3DEFF")

blu.makeImage(app, "/Users/admin/Downloads/164593051_32x32.png", 3)
blu.makeText(app, "Enter your name")
name = blu.makeInput(app, "Arial")
confirmed = blu.makeCheckbox(app, "confirm")

def submit():
    if confirmed.get():
        namee = name.get()
        blu.clear(app)
        blu.makeImage(app, "/Users/admin/Downloads/164593051_32x32.png", 3)
        blu.bgColor(app, "#D3DEFF")
        blu.makeText(app, f"Hi {namee}!")
        blu.makeButton(app, "press to close", "Arial", lambda: blu.end(app))
        blu.makeButton(app, "press to play a fun game", "Arial", lambda: blu.appLink(app, "/Users/admin/Desktop/python/guessing game.py"))

blu.makeButton(app, "submit.", "Arial", submit)

blu.run(app)