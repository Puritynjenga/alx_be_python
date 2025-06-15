import sys
print(sys.path)

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.Add_Book(Book("Brave New World", "Aldous Huxley"))
    library.Add_Book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.Check_out_Book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.Return_Book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()


