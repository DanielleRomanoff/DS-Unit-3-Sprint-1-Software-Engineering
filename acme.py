import numpy as np
import pandas as pd
from random import randint

class Product():
  """Class Product for Acme products assigns name, price, weight and
     flammability. Creates random identifier. Calculates the 'stealability'
     and 'explodability of the product
  """

# init function with variables initiated
def __init__(self, price = 10, weight = 20, flammability = 0.5):
    self.self = self
    self.name = str(name)
    self.price = int(price)
    self.weight = int(weight)
    self.flammability = float(flammability)
    # Identifier is a random integer between 1000000 and 9999999
    self.identifier = randint(1000000, 9999999)
    
    """stealability function calculates the price divided by the weight
       returns the message 'Not so stealable... if the ratio is less than 0.5
       returns the message 'Kinda stealable' if equal to or greater than 0.5 and less than 1.0
       returns the message 'Very stealable' if equal to or greater than 1.0
    """
    def stealability(self):
        stealable = self.price / self.weight
        if stealable < 0.5: 
            return 'Not so stealable...''
        elif stealable >= 0.5 and stealable < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable'
    
    """explode function calculates the flammability times the weight
       returns the message '...fizzle' if the product is less than 10 return
       returns the message '...boom!' if the product is greater than or equal to 10 
       and less than 50
       returns the message '...BABOOM!!' otherwise
    """
    def explode(self):
        explodable = self.flammability * self.weight
        if explodable < 10:
            return '...fizzle'
        elif explodable >= 10 and explodable < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'

# Subclass Boxing Glove
class BoxingGlove(Product):
    
    # defaults values for this class
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)
    
    # Punch function returns one of three strings specified.
    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!''
        else:
            return 'OUCH!'
    
    # Explode class always returns "... it's a glove."
    def explode(self):
        return "...it's a glove."



prod = Product('A Cool Toy')
print(prod.stealability())
print(prod.explode())
