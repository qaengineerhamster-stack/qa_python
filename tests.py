import pytest
from main import BooksCollector


class TestBooksCollector:

    # ПРИМЕР ОСТАВЛЯЕМ КАК ЕСТЬ
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # 1. Книга добавляется без жанра
    def test_add_new_book_has_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Маленький принц')

        assert collector.get_book_genre('Маленький принц') == ''

    # 2. Нельзя добавить одну и ту же книгу дважды
    def test_add_same_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')

        assert len(collector.get_books_genre()) == 1

    # 3. Нельзя добавить книгу с названием длиннее 40 символов
    def test_add_book_with_long_name(self):
        collector = BooksCollector()

        long_name = 'А' * 41
        collector.add_new_book(long_name)

        assert len(collector.get_books_genre()) == 0

    # 4. Установка жанра существующей книге
    def test_set_book_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        assert collector.get_book_genre('1984') == 'Фантастика'

    # 5. Нельзя установить жанр, которого нет в списке
    def test_set_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Роман')

        assert collector.get_book_genre('1984') == ''

    # 6. Получение книг по конкретному жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')

        books = collector.get_books_with_specific_genre('Ужасы')

        assert books == ['Оно', 'Сияние']

    # 7. Книги с возрастным рейтингом не попадают в детские
    def test_books_for_children_without_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Чип и Дейл')
        collector.add_new_book('Оно')

        collector.set_book_genre('Чип и Дейл', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')

        children_books = collector.get_books_for_children()

        assert 'Чип и Дейл' in children_books
        assert 'Оно' not in children_books

    # 8. Добавление книги в избранное
    def test_add_book_to_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')

        assert 'Шерлок Холмс' in collector.get_list_of_favorites_books()

    # 9. Нельзя добавить книгу в избранное дважды
    def test_add_same_book_to_favorites_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')

        assert len(collector.get_list_of_favorites_books()) == 1

    # 10. Удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')

        assert collector.get_list_of_favorites_books() == []
