import pytest

from main import BooksCollector

@pytest.fixture(autouse=True)
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(autouse=True)
def collector_with_harry_potter_fantastic_book():
    collector_with_harry_potter_fantastic_book = BooksCollector()
    existing_name = 'Гарри Поттер'
    existing_genry = 'Фантастика'
    collector_with_harry_potter_fantastic_book.add_new_book(existing_name)
    collector_with_harry_potter_fantastic_book.set_book_genre(existing_name, existing_genry)
    return collector_with_harry_potter_fantastic_book