# imports
import regex as re

cards_value={'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}

class Card:
    def __init__(self,name):
        self.name=name
        self.value=cards_value[self.name]
    
    def __repr__(self):
        return repr((self.name, self.value))
    

class Hand:

    def __init__(self, cards, bid):
        self.cards=cards
        self.bid=bid

    def __type__(self):
        ordered=sorted(self.cards, key=lambda card: card.value)
        count=0
        first=ordered[0]
        for c in ordered[1:]:
            pass
    



        
    def get_first(self):
        return self.cards[0]
    




