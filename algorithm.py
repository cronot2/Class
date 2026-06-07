
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
    print('the book was added succesfully.\n')

def edit_book(new_book, old_book):
    with open('books.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

        if old_book in data:
            i_book = data.index(old_book)
            data[i_book] = new_book
            with open('books.json', 'w', encoding='UTF-8') as file:
                file.write(json.dumps(data))
                file.closed
            print('The book was edited succesfully.\n')
        else:
            print('Are you sure that is the book?, check the name.\n')

def delete_book(user_book):
    with open('books.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)
        data_n = [dat.lower() for dat in data]

    if user_book in data_n:
        data_n.remove(user_book)
        with open('books.json', 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data_n))
            file.closed
        print('The book was deleted succesfully.')
    else:
        print('Check the book again.')

def show_library():
    with open('books.json', 'r', encoding='UTF-8') as file:
        books = json.load(file)

        for book in books:
            print(book.title())

def menu():
    while True:
        user_option = None
        print('''\n***Welcom to Library***
1.Search a book.
2.Show books.
3.Add a New book.
4.Edit a book.
5.Delete a book.
6.Salir''')
        try:
            user_option = int(input('What do you want to do?:'))
        except ValueError:
            print('\nInsert a integer number.')

        if user_option == 1:
            
            search_book(input('\nWhat book do you want to search?: ').strip().lower())

        elif user_option == 2:
            show_library()
            
        elif user_option == 3:
            
            add_book(input('\nWhat book do you want to add?: ').strip())
            
        elif user_option == 4:
            
            old_book=input('\nWhat book do you want to edit?: ').strip()
            new_book=input('What is the new name for the book?: ').strip().lower()
            edit_book(new_book=new_book, old_book=old_book)

        elif user_option == 5:

            delete_book(input('\nWhich book do you want delete?: ').strip().lower())
            
        elif user_option == 6:
            break    
        else:
            print('Insert a number in (1 to 5)\n')


if __name__ == '__main__':
    menu()