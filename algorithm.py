import random
import json
from turtle import title

def read_json():
    try:
        with open('books.json', 'r', encoding='UTF-8') as file:
            data = json.load(file)
            books = data.get("books", [])
            return books
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def write_json(books_list):
    data_to_save = {
        "books": books_list
    }
    with open('books.json', 'w', encoding='UTF-8') as file:
        json.dump(data_to_save, file, indent= 4, ensure_ascii=False)

def search_book(user_book):
    books = read_json()
    found_books = None

    if user_book.isdigit():
        id_books = int(user_book)
        for book in books:
            if book['id'] == id_books:
                found_books = book
                break
    else:
        for book in books:
            if book['title'].lower() == user_book:
                found_books = book
                break

    if found_books:
        print(f'Title:{found_books["title"].title()}, is in the library.')
    else:
        print('The book is not in the library')
            

def add_book(user_book):
    books = read_json()

    new_id = random.randint(10000, 99999)

    new_book = {
        "id":new_id,
        "title":user_book
    }

    books.append(new_book)

    write_json(books)
    print(f'The book was added successfully, ID:{new_id}  Title:{user_book.title()}')

def edit_book(user_book, old_book):
    books = read_json()
    found = False
    
    if old_book.isdigit():
        id_book = int(old_book)
        for book in books:
            if book["id"] == id_book:
                book["title"] = user_book
                found = True
                break
    else:
        for book in books:
            if (old_book).lower().strip() in book["title"].lower():
                book["title"] = user_book
                found = True
                break
    
    if found:
        write_json(books)
        print(f'\n{user_book.title()} was added successfully')
    else:
        print('\nCheck the id or the title')
            

def delete_book(user_book):
    books = read_json()
    initial_length = len(books)
    
    if user_book.isdigit():
        id_book = int(user_book)
        books = [book for book in books if book["id"] != id_book]
    else:
        books = [book for book in books if book['title'] != user_book]
        
    if len(books) < initial_length:
        write_json(books)
        print(f'\n{user_book} was deleted successfully')
    else:
        print('\nCheck the id or title, please')

def show_library():
    books = read_json()
    
    for book in books:
        print(f'\nID:{book["id"]} Title:{book['title'].title()}')

def menu():
    while True:
        user_option = None
        print('''\n***Welcome to Library***
1.Search a book.
2.Show books.
3.Add a new book.
4.Edit a book.
5.Delete a book.
6.Exit''')
        try:
            user_option = int(input('What do you want to do?:'))
        except ValueError:
            print('\nPlease enter an integer number.')

        if user_option == 1:
            
            search_book(input('\nWhat book do you want to search?: ').strip().lower())

        elif user_option == 2:
            show_library()
            
        elif user_option == 3:
            
            add_book(input('\nWhat book do you want to add?: ').strip())
            
        elif user_option == 4:
            
            old_book=input('\nWhat book do you want to edit?: ')
            new_book=input('What is the new name for the book?: ').lower().strip()
            edit_book(user_book=new_book, old_book=old_book)

        elif user_option == 5:

            delete_book(input('\nWhich book do you want delete?: ').strip().lower())
            
        elif user_option == 6:
            break    
        else:
            print('Insert a number in (1 to 5)\n')


if __name__ == '__main__':
    menu()