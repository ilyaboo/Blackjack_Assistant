import tkinter
from tkinter import *

def calc_prob(cards_array):
    cards_sum = sum(cards_array)
    success = 0
    for i in range(1, 11):
        if cards_sum + i < 22 and i < 10:
            success += 7.692
        elif cards_sum + i < 22:
            success = 100
        else:
            break
    return round(success, 2)

root = Tk()

entered_cards = []

def click2():
    entered_cards.append('2')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click3():
    entered_cards.append('3')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click4():
    entered_cards.append('4')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click5():
    entered_cards.append('5')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click6():
    entered_cards.append('6')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click7():
    entered_cards.append('7')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click8():
    entered_cards.append('8')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click9():
    entered_cards.append('9')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def click10():
    entered_cards.append('10')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def clickJ():
    entered_cards.append('J')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def clickQ():
    entered_cards.append('Q')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def clickK():
    entered_cards.append('K')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def clickA():
    entered_cards.append('A')
    LabelEnteredCards.config(text= "Your cards: " + " ".join(entered_cards))

def clickReset():
    global entered_cards
    entered_cards = []
    LabelEnteredCards.config(text = "Your cards: ")
    LabelChoice.config(text = "Best choice is...")
    LabelChoiceCommentary.config(text = "")

def clickCalculate():
    global entered_cards
    entered_cardsNumbers = []
    for i in range (0, len(entered_cards)):
        if entered_cards[i].isdigit():
            entered_cardsNumbers.append(int(entered_cards[i]))
        elif entered_cards[i] == 'A':
            entered_cardsNumbers.append(1)
        else:
            entered_cardsNumbers.append(10)
    if sum(entered_cardsNumbers) > 21:
        LabelChoice.config(text="It's a bust")
        LabelChoiceCommentary.config(text= "better luck next time")
    elif sum(entered_cardsNumbers) == 21:
        LabelChoice.config(text="You have exactly 21")
        LabelChoiceCommentary.config(text="Congratulations!")
    elif len(entered_cardsNumbers) == 2 and ((entered_cardsNumbers[0] == 1 and entered_cardsNumbers[1] == 10) or (entered_cardsNumbers[0] == 10 and entered_cardsNumbers[1] == 1)):
        LabelChoice.config(text="It's a BlackJack!")
        LabelChoiceCommentary.config(text="Congratulations!")
    elif calc_prob(entered_cardsNumbers) < 50:
        LabelChoice.config(text = "Best choice is STAND")
        LabelChoiceCommentary.config(text = str(round(100 - calc_prob(entered_cardsNumbers), 1)) + "% bust probability")
    else:
        LabelChoice.config(text="Best choice is DRAW")
        LabelChoiceCommentary.config(text= str(round(100 - calc_prob(entered_cardsNumbers), 1)) + "% bust probability")

#myLabel1 = Label(root, text = "This is label 1")
#myLabel1.grid(row = 0, column = 0)

#myButton = Button(root, text = "This is the button", state = DISABLED, padx = 50, pady = 50, command = click)
#myButton.grid(row = 1, column = 1)

LabelEnteredCards = Label(root, text="Your cards: ")
LabelEnteredCards.grid(row=2, column=0)

LabelChooseYourCards = Label(root, text="Choose your cards here: ")
LabelChooseYourCards.grid(row=1, column=0)

LabelGap1 = Label(root, text=" ")
LabelGap1.grid(row=3, column=0)

LabelGap2 = Label(root, text=" ")
LabelGap2.grid(row=5, column=0)

LabelChoice = Label(root, text = "Best choice is...")
LabelChoice.grid(row = 6, column = 0)

LabelChoiceCommentary = Label(root, text = "")
LabelChoiceCommentary.grid(row = 7, column = 0)

Button2 = Button(root, text = "2", padx = 30, pady = 30, command = click2)
Button2.grid(row = 1, column = 1)

Button3 = Button(root, text = "3", padx = 30, pady = 30, command = click3)
Button3.grid(row = 1, column = 2)

Button4 = Button(root, text = "4", padx = 30, pady = 30, comman = click4)
Button4.grid(row = 1, column = 3)

Button5 = Button(root, text = "5", padx = 30, pady = 30, command = click5)
Button5.grid(row = 1, column = 4)

Button6 = Button(root, text = "6", padx = 30, pady = 30, command = click6)
Button6.grid(row = 1, column = 5)

Button7 = Button(root, text = "7", padx = 30, pady = 30, command = click7)
Button7.grid(row = 1, column = 6)

Button8 = Button(root, text = "8", padx = 30, pady = 30, command = click8)
Button8.grid(row = 1, column = 7)

Button9 = Button(root, text = "9", padx = 30, pady = 30, command = click9)
Button9.grid(row = 1, column = 8)

Button10 = Button(root, text = "10", padx = 30, pady = 30, comman = click10)
Button10.grid(row = 1, column = 9)

ButtonJ = Button(root, text = "J", padx = 30, pady = 30, comman = clickJ)
ButtonJ.grid(row = 1, column = 10)

ButtonQ = Button(root, text = "Q", padx = 30, pady = 30, command = clickQ)
ButtonQ.grid(row = 1, column = 11)

ButtonK = Button(root, text = "K", padx = 30, pady = 30, command = clickK)
ButtonK.grid(row = 1, column = 12)

ButtonA = Button(root, text = "A", padx = 30, pady = 30, command = clickA)
ButtonA.grid(row = 1, column = 13)

ButtonReset = Button(root, text = "RESET", padx = 15, pady = 10, command = clickReset)
ButtonReset.grid(row = 2, column = 1)

ButtonCalculate = Button(root, text = "Calculate!", padx = 15, pady = 10, command = clickCalculate)
ButtonCalculate.grid(row = 4, column = 0)



ButtonQuit = Button(root, text = "QUIT", padx = 40, pady = 30, command = root.quit)
ButtonQuit.grid(row = 57, column = 57)



root.mainloop()





#   cards_array = map(int, input().split())
#   print(calc_prob(cards_array))
