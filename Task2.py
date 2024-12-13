from abc import ABC, abstractmethod
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logger.info(f"Book removed: {title}")

    def get_books(self) -> List[Book]:
        return self.books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        if year.isdigit():
            book = Book(title, author, int(year))
            self.library.add_book(book)
        else:
            logger.error("Invalid year format. Book not added.")

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            for book in books:
                print(book)
        else:
            print("No books in the library.")


def main():
    library = Library()
    manager = LibraryManager(library)

    try:
        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            match command:
                case "add":
                    title = input("Enter book title: ").strip()
                    author = input("Enter book author: ").strip()
                    year = input("Enter book year: ").strip()
                    manager.add_book(title, author, year)
                case "remove":
                    title = input("Enter book title to remove: ").strip()
                    manager.remove_book(title)
                case "show":
                    manager.show_books()
                case "exit":
                    print("Exiting the program. Goodbye!")
                    break
                case _:
                    print("Invalid command. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")

if __name__ == "__main__":
    main()

