BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages


class Library:
    def __init__(self, books=None):
        # если аргумент не передан — инициализируем пустым списком
        self.books = books if books is not None else []

    def get_next_book_id(self):
        # если книг нет — возвращаем 1
        if not self.books:
            return 1
        # если книги есть — id последней + 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        # если книга не найдена
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # ожидаем 1

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # библиотека с книгами
    print(library_with_books.get_next_book_id())  # ожидаем 3

    print(library_with_books.get_index_by_book_id(1))  # ожидаем 0