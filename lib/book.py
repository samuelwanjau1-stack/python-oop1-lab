class Book:
    def __init__(self, title, page_count):
        # Set the basic info for the book
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Validation: check if the input is a whole number
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Just a fun message for the user
        print("Flipping the page...wow, you read fast!")