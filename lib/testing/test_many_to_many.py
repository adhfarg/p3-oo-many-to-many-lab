import pytest
from many_to_many import Author, Book, Contract

def test_contract_validates_author():
    """Test Contract class validates author of type Author"""
    book = Book("Title")
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(ValueError, match="Invalid author type"):
        Contract(Author("ValidAuthor"), book, date, royalties)

    assert contract.author == author
    assert contract.book == book
    assert contract.date.strftime("%m/%d/%Y") == date  
    assert contract.royalties == royalties

def test_contract_validates_author():
    """Test Contract class validates author of type Author"""
    book = Book("Title")
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(ValueError, match="Invalid author type"):
        Contract("InvalidAuthor", book, date, royalties)

def test_contract_validates_book():
    """Test Contract class validates book of type Book"""
    author = Author("Name")
    date = '01/01/2001'
    royalties = 40000

    with pytest.raises(ValueError, match="Invalid book type"):
        Contract(author, "InvalidBook", date, royalties)

def test_contract_validates_royalties():
    """Test Contract class validates royalties of type int"""
    author = Author("Name")
    book = Book("Title")
    date = '01/01/2001'

    with pytest.raises(ValueError, match="Invalid royalties type"):
        Contract(author, book, date, "InvalidRoyalties")

def test_author_sign_contract():
    """Test Author class has method sign_contract() that creates a contract for an author and book"""
    author = Author("Name")
    book = Book("Title")
    date_str = '01/01/2001'
    royalties = 50000

    author.sign_contract(book, date_str, royalties)
    contract = author.contracts()[0]

    assert contract.author == author
    assert contract.book == book
    assert contract.date.strftime("%m/%d/%Y") == date_str  
    assert contract.royalties == royalties

def test_author_has_total_royalties():
    """Test Author class has method total_royalties that gets the sum of all its related contracts' royalties"""
    author = Author("Name")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")

    author.sign_contract(book1, "01/01/2001", 10)
    author.sign_contract(book2, "01/01/2001", 20)
    author.sign_contract(book3, "01/01/2001", 30)

    assert author.total_royalties() == 60

def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that sorts all contracts by date"""
    Contract.all = []
    author1 = Author("Name 1")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")
    author2 = Author("Name 2")
    book4 = Book("Title 4")
    contract1 = Contract(author1, book1, "02/01/2001", 10)
    contract2 = Contract(author1, book2, "01/01/2001", 20)
    contract3 = Contract(author1, book3, "03/01/2001", 30)
    contract4 = Contract(author2, book4, "01/01/2001", 40)

    assert Contract.contracts_by_date('01/01/2001') == [contract2, contract4]
