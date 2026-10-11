class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

def borrow(self):
    if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Confirmation: '{self.title}' has been successfully borrowed.")
    else:
            print(f"Notice: '{self.title}' is already borrowed.")   

def return_book(self):
    if self.is_borrowed:
            self.is_borrowed = False
            print(f"Confirmation: '{self.title}' has been successfully returned.")
    else:
            print(f"Notice: '{self.title}' was not borrowed.")

book1 = Book("The Hobbit", "tom and jerry")
book2 = Book("titanic", "wow book")      
book3 = Book("To Kill a Mockingbird", "Harper Lee")

print("--- Borrowing Demonstration ---")
book1.borrow()
book2.borrow()

print("\n--- Returning Demonstration ---")
book1.return_book()
book3.return_book()