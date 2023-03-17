# interface of the application

from tkinter import *
from hand import Hand

class Interface:
    def __init__(self):
        self.root = Tk()
        self.hand = Hand()

        self.LabelEnteredCards = Label(self.root, text="Your cards: ")
        self.LabelEnteredCards.grid(row=2, column=0)

        self.LabelChooseYourCards = Label(self.root, text="Choose your cards here: ")
        self.LabelChooseYourCards.grid(row=1, column=0)

        self.LabelChoice = Label(self.root, text = "Best choice is...")
        self.LabelChoice.grid(row = 6, column = 0)

        self.LabelChoiceCommentary = Label(self.root, text = "")
        self.LabelChoiceCommentary.grid(row = 7, column = 0)



        LabelGap1 = Label(self.root, text = " ")
        LabelGap1.grid(row = 3, column = 0)

        LabelGap2 = Label(self.root, text = " ")
        LabelGap2.grid(row = 5, column = 0)

        self.Button2 = Button(self.root, text = "2", padx = 30, pady = 30, command = self.click_card("2"))
        self.Button2.grid(row = 1, column = 1)

        Button3 = Button(self.root, text = "3", padx = 30, pady = 30, command = self.click_card("3"))
        Button3.grid(row = 1, column = 2)

        Button4 = Button(self.root, text = "4", padx = 30, pady = 30, comman = self.click_card("4"))
        Button4.grid(row = 1, column = 3)

        Button5 = Button(self.root, text = "5", padx = 30, pady = 30, command = self.click_card("5"))
        Button5.grid(row = 1, column = 4)

        Button6 = Button(self.root, text = "6", padx = 30, pady = 30, command = self.click_card("6"))
        Button6.grid(row = 1, column = 5)

        Button7 = Button(self.root, text = "7", padx = 30, pady = 30, command = self.click_card("7"))
        Button7.grid(row = 1, column = 6)

        Button8 = Button(self.root, text = "8", padx = 30, pady = 30, command = self.click_card("8"))
        Button8.grid(row = 1, column = 7)

        Button9 = Button(self.root, text = "9", padx = 30, pady = 30, command = self.click_card("9"))
        Button9.grid(row = 1, column = 8)

        Button10 = Button(self.root, text = "10", padx = 30, pady = 30, comman = self.click_card("10"))
        Button10.grid(row = 1, column = 9)

        ButtonJ = Button(self.root, text = "J", padx = 30, pady = 30, comman = self.click_card("J"))
        ButtonJ.grid(row = 1, column = 10)

        ButtonQ = Button(self.root, text = "Q", padx = 30, pady = 30, command = self.click_card("Q"))
        ButtonQ.grid(row = 1, column = 11)

        ButtonK = Button(self.root, text = "K", padx = 30, pady = 30, command = self.click_card("K"))
        ButtonK.grid(row = 1, column = 12)

        ButtonA = Button(self.root, text = "A", padx = 30, pady = 30, command = self.click_card("A"))
        ButtonA.grid(row = 1, column = 13)

        ButtonReset = Button(self.root, text = "RESET", padx = 15, pady = 10, command = self.clickReset())
        ButtonReset.grid(row = 2, column = 1)

        ButtonCalculate = Button(self.root, text = "Calculate!", padx = 15, pady = 10, command = self.clickCalculate())
        ButtonCalculate.grid(row = 4, column = 0)

        ButtonQuit = Button(self.root, text = "QUIT", padx = 40, pady = 30, command = self.root.quit)
        ButtonQuit.grid(row = 57, column = 57)
    
    def click_card(self, card: str) -> None:
        # method that updates the interface and hand when card button is clicked
        self.hand.add_card(card)
        self.LabelEnteredCards.config(text= "Your cards: " + " ".join(self.hand.get_cards()))
        return
    
    def clickReset(self):
        # method that resets the interface and hand
        self.hand.reset_hand()
        self.LabelEnteredCards.config(text = "Your cards: ")
        self.LabelChoice.config(text = "Best choice is...")
        self.LabelChoiceCommentary.config(text = "")
        return
    
    def clickCalculate(self) -> None:
        # method that calculates probability of success
        # and updates interface accordingly
        
        cards = self.hand.get_cards()   # list of cards
        cards_sum = self.hand.calc_sum()   # sum of the card values
        success_probability = self.hand.calc_prob()   # probasbility of success when drawing
        tens = ["10", "J", "Q", "K"]   # list of cards of values 10 for detecting blackjack

        if cards_sum > 21:
            self.LabelChoice.config(text = "It's a bust")
            self.LabelChoiceCommentary.config(text = "better luck next time")
        elif cards_sum == 21:
            self.LabelChoice.config(text = "You have exactly 21")
            self.LabelChoiceCommentary.config(text = "Congratulations!")
        elif len(cards) == 2 and \
            ((cards[0] == "A" and cards[1] in tens) or (cards[0] in tens and cards[1] == "A")):
            self.LabelChoice.config(text = "It's a BlackJack!")
            self.LabelChoiceCommentary.config(text = "Congratulations!")
        elif success_probability < 50:
            self.LabelChoice.config(text = "Best choice is STAND")
            self.LabelChoiceCommentary.config(text = str(round(100 - success_probability, 1)) + "% bust probability")
        else:
            self.LabelChoice.config(text = "Best choice is DRAW")
            self.LabelChoiceCommentary.config(text = str(round(100 - success_probability, 1)) + "% bust probability")
        return

    def start(self):
        # method that launches the interface
        self.root.mainloop()
        return