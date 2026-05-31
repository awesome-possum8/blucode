import blucode as blu
import random

guesses = 0
app = blu.makeWindow("number guess!", "fun game:")
blu.bgColor(app, "#D3DEFF")

number = random.randint(1, 100)
blu.makeText(app, "Can you guess my number?", "Arial Rounded MT Bold")
blu.makeText(app, "first guess", "Arial Rounded MT Bold")
blu.makeText(app, f"{guesses} guesses", "Arial Rounded MT Bold")
guess = blu.makeScale(app, 1, 100,)

def giveup():
    blu.clear(app)
    blu.bgColor(app, "#D3DEFF")
    blu.makeText(app, f"The number was {number}", "Arial Rounded MT Bold")
    blu.makeText(app, f"😞you quit after {guesses} guesses😞", "Arial Rounded MT Bold")
    blu.makeText(app, "<:(", "Arial Rounded MT Bold")
    blu.fallingText(app, "😞")
def check(num):
    global guess
    global guesses
    global number
    guesses += 1
    if num == number:
        blu.clear(app)
        blu.bgColor(app, "#D3DEFF")
        blu.makeText(app, "The number was {number}!", "Arial Rounded MT Bold")
        blu.makeText(app, f"🎉you won after {guesses} guesses!🎉", "Arial Rounded MT Bold")
        blu.makeText(app, ":D", "Arial Rounded MT Bold")
        blu.fallingText(app)
    else:
        blu.clear(app)
        blu.bgColor(app, "#D3DEFF")
        blu.makeText(app, "Oops! thats not it :(", "Arial Rounded MT Bold")
        if abs(number-num) <= 10:
            blu.makeText(app, "realy hot!", "Arial Rounded MT Bold")
        elif abs(number-num) <= 30:
            blu.makeText(app, "hot!", "Arial Rounded MT Bold")
        elif abs(number-num) <= 70:
            blu.makeText(app, "warm.", "Arial Rounded MT Bold")
        else:
            blu.makeText(app, "cold", "Arial Rounded MT Bold")
        blu.makeText(app, f"{guesses} guesses", "Arial Rounded MT Bold")
        guess = blu.makeScale(app, 1, 100,)
        blu.makeButton(app, "submit guess", "Arial Rounded MT Bold", lambda: check(guess.get()))
        blu.makeButton(app, "give up", "Arial Rounded MT Bold", lambda: giveup())


blu.makeButton(app, "submit guess", "Arial Rounded MT Bold", lambda: check(guess.get()))
blu.run(app)