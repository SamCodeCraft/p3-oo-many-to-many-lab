from datetime import datetime

class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]

class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return sorted([contract for contract in cls.all_contracts if contract.date == date], key=lambda x: x.date)

# Example Usage:

# Create authors and books
author1 = Author("Jane Austen")
author2 = Author("Charles Dickens")

book1 = Book("Pride and Prejudice")
book2 = Book("Great Expectations")

# Author signs contracts
contract1 = author1.sign_contract(book1, "2024-01-01", 10)
contract2 = author2.sign_contract(book2, "2024-01-02", 12)

# Get author's contracts and books
print([contract.book.title for contract in author1.contracts()])  # Output: ['Pride and Prejudice']
print([book.title for book in author1.books()])  # Output: ['Pride and Prejudice']

# Get total royalties for an author
print(author1.total_royalties())  # Output: 10

# Get contracts by date
contracts_on_date = Contract.contracts_by_date("2024-01-01")
print([(contract.author.name, contract.book.title) for contract in contracts_on_date])  # Output: [('Jane Austen', 'Pride and Prejudice')]

# Get book's contracts and authors
print([contract.author.name for contract in book1.contracts()])  # Output: ['Jane Austen']
print([author.name for author in book1.authors()])  # Output: ['Jane Austen']
