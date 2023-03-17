# class Hand that corresponds to the player's hand

class Hand:
    def __init__(self) -> None:
        self.__cards = []   # array containing values of the cards
        return
    
    def add_card(self, card: int) -> None:
        # method that adds a card to the hand
        self.__cards.append(card) 
        return

    def get_cards(self) -> list[int]:
        # method that returns a string with the cards in the hand
        return self.__cards
    
    def reset_hand(self) -> None:
        # method that resets the hand
        self.__cards = []
        return
    
    def calc_sum(self) -> int:
        # method that calculates the sum of the cards in the hand
        cards_sum = 0
        for card in self.__cards:
            if card.isdigit():
                cards_sum += int(card)
            elif card == "A":
                cards_sum += 1
            else:
                cards_sum += 10
        return cards_sum

    def calc_prob(self) -> float:
        # method that returns the probability of successfully
        # drawing the next card with a current hand

        cards_sum = self.calc_sum()
        success = 0   # probability to return 
        for i in range(1, 11):

            # if the drawn card is of value 10 and won't cause bust
            # (sum < 22), there are not cards that can cause bust
            # (ace can be treated as 1 in case 11 causes bust) 
            if cards_sum + i < 22 and i == 10:   
                success = 100

            # if the card won't cause bust (sum < 22) and is not of value of 10
            # it is drawn with probability 1 / 13 (in decimals, then converted to percent)
            # so success probability increases by probability of drawing this card
            elif cards_sum + i < 22:
                success += 100 * (1 / 13) 
            else:
                # card causes bust, so all cards of greater value will also do that
                break
        return round(success, 2)
    
    

