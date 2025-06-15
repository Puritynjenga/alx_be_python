class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def __str__(self):
        return f"{self.title} by {self.author}"
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
        
class Library(Book):
    def __init__(self):
        self.books = [] #store Book objects

    def Add_Book(self, book):
        """
        Adds a Book object to the library's collection.
        """
        if isinstance(book, Book): #adding a Book object
            self.books.append(book)
        else:
            print(f"Error: Can only add Book objects to the library. Received: {type(book)}")

    def Check_out_Book(self, title):
        """
        Checks out a book by its title if it's available.
        """
        for book in self.books:
            if book.title == title:
                if not book._is_checked_out: # Check if it's currently available
                    book.check_out()
                    # print(f"'{title}' has been checked out.")
                    return True
                else:
                    # print(f"'{title}' is already checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def Return_Book(self, title):
        """
        Returns a book by its title if it was checked out.
        """
        for book in self.books:
            if book.title == title:
                if book._is_checked_out: # Check if it's currently checked out
                    book.return_book()
                    # print(f"'{title}' has been returned.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        """
        available_found = False
        for book in self.books:
            if not book._is_checked_out:
                print(book) # Uses the __str__ method of the Book class
                available_found = True
        if not available_found:
            print("No books available at the moment.")
    
          
            
       
        
            


       
            