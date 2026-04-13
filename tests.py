import pytest

from main import BooksCollector

class TestBooksCollector:

 
    def test_add_new_book_add_two_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_length_more_40_book_not_added(self,collector):
        book_name = 'Рассвет полночи, или Созерцание славы, торжества и мудрости порфироносных, браноносных и мирных гениев России с последованием дидактических, эротических и других разного рода в стихах и прозе опытов Семена Боброва'
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_new_book_same_name_two_times_one_book_added(self,collector):
        book_name = 'Хоббит или туда и обратно'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_book_and_genre_exist_genre_added(self,collector):
        book_name = 'Хоббит или туда и обратно'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,'Фантастика')

        assert collector.get_book_genre(book_name) == 'Фантастика'

    def test_set_book_genre_genre_not_exists_genre_not_added(self,collector):
        book_name = 'Черный обелиск'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,'Драма')

        assert collector.get_book_genre(book_name) == ''

    def test_get_books_genre_verify_genre_lists_success(self,collector):
        genre_list= ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']        
        for genre in genre_list:
            assert genre in collector.genre

    def test_get_books_genre_verify_genre_not_in_list_success(self,collector):
        genre_list= ['Комиксы', 'Триллер','Драма']        
        for genre in genre_list:
            assert genre not in collector.genre     

    @pytest.mark.parametrize("genre, expected_books", [
        ('Фантастика', ['Хоббит или туда и обратно', 'Территория чудовищ', 'Таинственный остров', 'Лисьи броды']),
        ('Детективы', ['Клуб убийств по четвергам', 'Ловушка для дьявола', 'Десять негритят']),
        ('Комедии', ['Унесенные ветром', 'Благие знамения']),
        ('Ужасы', ['Зов Ктулху', 'Граф Дракула', 'За спиной']),
        ('Мультфильмы', ['Чук и Гек', 'Маленький принц']),
        ('Драма', [])  # несуществующий жанр
    ])          

    def test_get_books_with_specific_genre_add_several_books_with_genres_return_books(self,collector_with_books,genre, expected_books):

        result = collector_with_books.get_books_with_specific_genre(genre)
        assert result == expected_books
        assert len(result) == len(expected_books)
   
    def test_get_books_with_specific_genre_books_with_genre_success(self,collector_with_books):

        assert len(collector_with_books.get_books_with_specific_genre('Фантастика')) == 4 
        assert len(collector_with_books.get_books_with_specific_genre('Детективы')) == 3 
        assert len(collector_with_books.get_books_with_specific_genre('Ужасы')) == 3
        assert len(collector_with_books.get_books_with_specific_genre('Комедии')) == 2
        assert len(collector_with_books.get_books_with_specific_genre('Мультфильмы')) == 2
        assert collector_with_books.get_books_with_specific_genre('') == []

    def test_get_books_for_children_books_with_genres_success(self,collector_with_books):
        
        assert len(collector_with_books.get_books_for_children()) == 8
          

    def test_add_book_in_favorites_add_two_books_books_added(self, collector_with_books):
        list = ['Чук и Гек','Зов Ктулху']
        for i in list:
            collector_with_books.add_book_in_favorites(i)        
            assert i in collector_with_books.get_list_of_favorites_books()
        assert len(collector_with_books.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_remove_existing_books_books_removed(self, collector_with_books):
        list = ['Чук и Гек','Зов Ктулху']
        for i in list:
            collector_with_books.add_book_in_favorites(i)        
            
        collector_with_books.delete_book_from_favorites('Зов Ктулху')
        assert len(collector_with_books.get_list_of_favorites_books()) == 1  
        assert collector_with_books.get_list_of_favorites_books() == ['Чук и Гек']    