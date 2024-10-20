import pytest
from conftest import collector

class TestBooksCollector:

    @pytest.mark.parametrize(
        'name, expected_books_genre_count',
        [
            ['', 0],
            ['Гарри Поттер', 1],
            ['Название книги, в которой точно больше сорока символов', 0]
        ]
    )
    def test_add_new_book_name_length_result_matches_with_expected_books_count(self, collector, name, expected_books_genre_count):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_books_genre_count

    def test_add_new_book_adding_1book_books_genre_contains_1book(self, collector):
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'genry, expected_genre',
        [
            ['Фантастика', 'Фантастика'],
            ['Детективы', 'Детективы'],
            ['Биография', '']
        ]
    )
    def test_set_book_genre_updates_genre_correctly(self, collector, genry, expected_genre):
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.set_book_genre(name, genry)
        assert collector.get_books_genre()[name] == expected_genre

    @pytest.mark.parametrize(
        'name, expected_genre',
        [
            ['Гарри Поттер', 'Фантастика'],
            ['Книга, которой точно нет', None]
        ]
    )
    def test_get_book_genre_with_existing_and_non_existing_books(self, collector_with_harry_potter_fantastic_book, name, expected_genre):
        assert collector_with_harry_potter_fantastic_book.get_book_genre(name) == expected_genre

    def test_get_books_with_specific_genre_returns_correct_books(self, collector_with_harry_potter_fantastic_book):
        assert collector_with_harry_potter_fantastic_book.get_books_with_specific_genre('Фантастика')[0] == 'Гарри Поттер'

    @pytest.mark.parametrize(
        'book_names, expected_books_genre_count',
        [
            ['Гарри Поттер,Война и мир,Властелин колец', 3],
            ['Живи и помни,Тихий дон', 2]
        ]
    )
    def test_get_books_genre_counts_correctly(self, collector, book_names, expected_books_genre_count):
        for name in book_names.split(','):
            collector.add_new_book(name)

        assert len(collector.get_books_genre()) == expected_books_genre_count

    @pytest.mark.parametrize(
        'book_name, book_genre, expected_books_count',
        [
            ['Сияние', 'Ужасы', 0],
            ['Лунтик', 'Мультфильмы', 1]
        ]
    )
    def test_children_books_retrieval_based_on_genre(self, collector, book_name, book_genre, expected_books_count):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert len(collector.get_books_for_children()) == expected_books_count

    @pytest.mark.parametrize(
        'books_for_adding,favourite_books,expected_favourite_count',
        [
            [['Гарри Поттер', 'Судьба человека', 'Byte of python'], ['Byte of python'], 1],
            [['Гарри Поттер', 'Судьба человека', 'Byte of python'], ['Byte of python', 'Byte of python'], 1],
            [['Гарри Поттер', 'Судьба человека', 'Byte of python'], ['Гарри Поттер', 'Судьба человека'], 2]
        ]
    )
    def test_addition_to_favorites_handling_duplicates(self, collector, books_for_adding, favourite_books, expected_favourite_count):
        for book in books_for_adding:
            collector.add_new_book(book)

        for favourite in favourite_books:
            collector.add_book_in_favorites(favourite)

        assert len(collector.get_list_of_favorites_books()) == expected_favourite_count

    def test_delete_book_from_favorites_removes_it(self, collector_with_harry_potter_fantastic_book):
        collector_with_harry_potter_fantastic_book.add_book_in_favorites('Гарри Поттер')
        collector_with_harry_potter_fantastic_book.delete_book_from_favorites('Гарри Поттер')
        assert len(collector_with_harry_potter_fantastic_book.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_initially_empty(self, collector):
        assert len(collector.get_list_of_favorites_books()) == 0