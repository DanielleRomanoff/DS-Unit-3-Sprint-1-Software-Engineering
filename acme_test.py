```python
#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
import unittest
from acme import Product, BoxingGlove



class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_stealability(self):

        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), "Kinda stealable.")

    def test_default_explode(self):

        prod = Product('Test Product')
        self.assertEqual(prod.explode(), "...boom!")


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        self.assertEqual(len(products()), 30)

    def test_legal_names(self):
        adj_list = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun_list = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']
        prods = products()
        for i in prods:
            self.assertEqual(i.name.count(" "), 1)
            self.assertIn(i.name.split(" ")[0], adj_list)
            self.assertIn(i.name.split(" ")[-1], noun_list)


if __name__ == '__main__':
    # Run unittests
    unittest.main()