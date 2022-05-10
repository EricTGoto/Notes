class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
    
    # defines the iteration variable n
    def __iter__(self):
        self.n = 0
        # returns a reference to the object itself
        return self
    
    # returns the next item in the iterator
    def __next__(self):
        if self.n < len(self.products):
            book = self.products[self.n]
            self.n += 1
            return book
        else:
            raise StopIteration