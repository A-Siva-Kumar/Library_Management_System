from LMS import *

trans = Transaction()
lib_sys = Library()


while True:
    
    print('''
    Welcome to LMS!

    Choose the option:
    ------------------

    a. Register User.     1. Add Book.
    b. Remove User.       2. Search Book.
    c. User Details.      3. Update Book.       
    e. Exit.              4. remove Book.
                          5. Allot Book.
                          6. Returned Book.
                          
    ''')

    option = input("Option: ").lower()
    
    try:

        if option == "a":
            name = input("Enter Name: ")
            Id = int_valid()
            reg_user = lib_sys.register_user(name, Id)
            print(f"\n{reg_user} was Registered successfully.")

        elif option == 'b' :
            Id = int_valid()
            print(lib_sys.remove_user(Id))

        elif option == 'c':
            Id = int_valid()
            print(lib_sys.user_details(Id))

        elif option == "e":
            print("Successfully Exited.")
            break
        
        elif int(option) == 1 :
            title, author, isbn, tot_books = get_book_info()
            print(lib_sys.add_book(title, author, isbn, tot_books))

        elif int(option) == 2:
            isbn = input("ISBN: ")
            print(lib_sys.search_book(isbn))

        elif int(option) == 3:
            isbn = input("ISBN: ")
            tot_books = int_valid("No.of books: ")
            print(lib_sys.update_book(isbn, tot_books))

        elif int(option) == 4:
            isbn = input("ISBN: ")
            print(lib_sys.remove_book(isbn))

        elif int(option) == 5:
            user_id = int_valid()
            isbn = isbn = input("ISBN: ")
            no_of_books = int_valid("No.of books: ")
            print(trans.allot_book(lib_sys, user_id, isbn, no_of_books))

        elif int(option) == 6:
            user_id = int_valid()
            isbn = input("ISBN: ")
            no_of_books = int_valid("No.of books: ")
            print(lib_sys.return_book(user_id, isbn))

    except ValueError:
        print("\nPlease enter valid Option!\n")