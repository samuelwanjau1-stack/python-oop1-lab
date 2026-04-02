class Coffee:
    def __init__(self, size, price):
        self._size = None # Initialize the internal variable
        self.size = size   # This triggers the validation in the setter
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Validation: Only allow specific sizes
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        # Increase the price attribute by 1
        self.price += 1