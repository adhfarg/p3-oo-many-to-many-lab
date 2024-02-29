from datetime import datetime

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise ValueError("Invalid book type")
        if not isinstance(date, str) or not date:
            raise ValueError("Invalid date")
        if not isinstance(royalties, int) or royalties <= 0:
            raise ValueError("Invalid royalties type or value")
        
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Invalid author type")
        if not isinstance(book, Book):
            raise ValueError("Invalid book type")
        if not isinstance(date, str) or not date:
            raise ValueError("Invalid date")
        if not isinstance(royalties, int) or royalties <= 0:
            raise ValueError("Invalid royalties type or value")

        self.author = author
        self.book = book
        self.date = datetime.strptime(date, "%m/%d/%Y")
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        contracts = [contract for contract in cls.all if contract.date.strftime("%m/%d/%Y") == date]
        return sorted(contracts, key=lambda x: x.date)
