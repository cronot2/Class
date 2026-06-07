import json

def search_book(user_book):
    with open('books.json', 'r', encoding='UTF-8') as file:
        
        books = json.load(file)
        normal_book = [book.strip().lower() for book in books]
        
        if user_book in normal_book:
            print(f'The book, \"{user_book.capitalize()}\" is in the library\n')
        else:
            print(f'The book, \"{user_book.capitalize()}\" is not in the library\n')
            file.closed

def add_book(user_book):
    with open('books.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data.append(user_book)

    with open('books.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(data))
        file.closed

def edit_book(user_book):
    with open('books.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

        if user_book in data:
            data.

def menu():
    while True:
        user_option = None
        print('''\nWelcom to Library
1.Search a book.
2.Add a New book.
3.Edit a book.
3.Salir''')
        try:
            user_option = int(input('What do you want to do?:'))
        except ValueError:
            print('\nInsert a integer number.')

        if user_option == 1:
            search_book(input('\nWhat book do you want to search?: ').strip().lower())
        elif user_option == 2:
            add_book(input('\nWhat book do you want to add?: ').strip().lower())
        elif user_option == 3:
            break
        else:
            print('Insert a number in (1 to 3)\n')


if __name__ == '__main__':
    menu()