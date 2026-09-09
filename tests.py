import pytest

from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()


        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', 
                             ['', 
                              'Жизнь и приключения солдата Ивана Чонкина'])
    def test_add_new_book_does_not_add_book_with_invalid_name_length(self, name):

        collector = BooksCollector()
    
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_set_book_genre_sets_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Фантастика')

        assert collector.get_book_genre('Колобок') == 'Фантастика'

    def test_get_book_genre_returns_correct_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_book_genre('Сияние') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_list_with_chosen_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Безмолвный пациент')
        collector.set_book_genre('Безмолвный пациент', 'Детективы')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')

        assert collector.get_books_with_specific_genre('Детективы') == ['Безмолвный пациент']

    def test_get_books_genre_returns_books_genre_dictionary(self):

        collector = BooksCollector()
        
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.set_book_genre('Трое в лодке, не считая собаки', 'Комедии')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')

        assert collector.get_books_genre() == {
            'Трое в лодке, не считая собаки': 'Комедии',
            'Десять негритят': 'Детективы'
        }

    def test_get_books_for_children_returns_list_with_books_for_children(self):

        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Дядя Фёдор, пёс и кот')
        collector.set_book_genre('Дядя Фёдор, пёс и кот', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Дядя Фёдор, пёс и кот']

    def test_add_book_in_favorites_book_added_to_favorites_list(self):

        collector = BooksCollector()

        collector.add_new_book('Безмолвный пациент')
        collector.add_book_in_favorites('Безмолвный пациент')

        assert collector.get_list_of_favorites_books() == ['Безмолвный пациент']

    def test_delete_book_from_favorites_removes_book_from_the_list(self):

        collector = BooksCollector()
        
        collector.add_new_book('Безмолвный пациент')
        collector.add_book_in_favorites('Безмолвный пациент')

        collector.delete_book_from_favorites('Безмолвный пациент')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_favorites_list(self):

        collector = BooksCollector()
        
        collector.add_new_book('Безмолвный пациент')
        collector.add_book_in_favorites('Безмолвный пациент')
        
        assert collector.get_list_of_favorites_books() == ['Безмолвный пациент']
