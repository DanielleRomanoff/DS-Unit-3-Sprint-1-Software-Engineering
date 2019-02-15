import acme
import numpy as np
import pandas as pd
from random import randint

def products(number_of_products=30):
    """products function provides a total of 30 products with random values for the name, price, weight, and        flammability fields. For the name attribute, I needed a list of possible name to choose from:
       Will print a list of the product names, the total price of the products, the 
       total weight of the products, and the average flammability of the products.
    """

    # List of names needed for random choice
    adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
    return [acme.Product("{} {}".format(random.choice(adj_list),
                                        random.choice(noun_list)),
                         random.randint(5, 100), random.randint(5, 100),
                         random.uniform(0.0, 2.5)) for i in range(amount)]

# Report function
def report(list_of_products):
    product_name = []
    product_price = []
    product_weight = []
    product_flammability = []
    for i in list_of_products:
        product_name.append(i.product_names)
        product_price.append(i.product_prices)
        product_weight.append(i.product_weights)
        product_flammability.append(i.product_flammabilities)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names:', len(list(set(product_name))))
    print('Average price:', sum(product_price) / len(product_price))
    print('Average weight:', sum(product_weight) / len(product_weight))
    print('Average flammability:', sum(product_flammability) / len(product_flammability))

if __name__ == '__main__':
    report(list_of_products())
