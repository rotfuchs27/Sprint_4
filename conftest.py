import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books(collector):
    books_list = {
        'Хоббит или туда и обратно': 'Фантастика',
        'Территория чудовищ': 'Фантастика',
        'Таинственный остров': 'Фантастика',
        'Лисьи броды': 'Фантастика',
        'Унесенные ветром': 'Комедии',
        'Благие знамения': 'Комедии',
        'Война и мир': 'Драма',  # несуществующий жанр
        'Зов Ктулху': 'Ужасы',
        'Граф Дракула': 'Ужасы',
        'За спиной': 'Ужасы',
        'Чук и Гек': 'Мультфильмы',
        'Маленький принц': 'Мультфильмы',
        'Клуб убийств по четвергам': 'Детективы',
        'Ловушка для дьявола': 'Детективы',
        'Десять негритят': 'Детективы',
    }
    for book, genre in books_list.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
    return collector
