import datetime

# Book Class.

class Book:
    def __init__(self, title, author, isbn, tot_books):
        self.title = title
        self.author = author
        self.__isbn = isbn
        self.tot_books = tot_books
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Total Books: {self.tot_books}"
        
    def get_isbn(self):
        return self.__isbn
    
    def get_tot_books(self):
        return self.tot_books
    

# User Class.
    
class User:
    
    def __init__(self,name, user_id,book_borr = 0):
        self.name = name
        self.__user_id = user_id
        self.book_borr = book_borr
        
    def __str__(self):
        return f"Name: {self.name}, ID: {self.__user_id}, Books Borrowed: {self.book_borr}"
    
    def get_user_id(self):
        return self.__user_id
    
    def get_book_borr(self):
        return self.book_borr
    
# Transaction Class.
    
class Transaction:
    def __init__(self):
        self.trans_list = []
        
    def allot_book(self,library,user_id, isbn, no_of_books):
        for book in library.book_list:
            if book.get_isbn() == isbn:
                if book.get_tot_books() >= no_of_books:
                    book.tot_books -= no_of_books
                    for user in library.user_list:
                        user.get_user_id == user_id
                        user.book_borr += no_of_books
                        trans = f"User with ID: {user_id} >> ISBN: {isbn} >> on : {datetime.date.today()} >> Alloted books: {no_of_books}"
                        self.trans_list.append(trans)
                        return trans
                else:
                    return f"Only {book.get_tot_books()} books are avaliable."
            else:
                return f"Book with ISBN {isbn} was not there."

class Library():
    
    def __init__ (self):
        self.book_list = []
        self.user_list = []
        

# Book Section::

    def add_book(self, title, author, isbn, tot_books):
        for book in self.book_list:
            if book.get_isbn() == isbn:
                print(f"Book with ISBN {isbn} already exists.")
                return
        new_book = Book(title, author, isbn,tot_books)
        self.book_list.append(new_book)
        return f"{new_book} was successfully added."
    
    def search_book(self,isbn):
        for book in self.book_list:
            if book.get_isbn() == isbn: 
                return (f"\n{book}")
        return f"Book with ISBN {isbn} was not found!"
    
    def update_book(self, isbn, tot_books):
        for book in self.book_list:
            if book.get_isbn() == isbn:
                pre_total = book.tot_books
                book.tot_books = tot_books
                return f"Total Books updated from {pre_total} to {tot_books}"
            
    def remove_book(self, isbn):
        for book in self.book_list:
            if book.get_isbn() == isbn:
                self.book_list.remove(book)
                return f"Book with ISBN: {isbn} was successfully removed."
            return f"Book with ISBN {isbn} was not found!"
        
    def avaliable_books(self):
        for book in self.book_list: 
            print("\n",book,"\n")
            
            
 # User section::

    def register_user(self, name, user_id):
        for user in self.user_list:
            if user.get_user_id() == user_id:
                print(f"User with ID {user_id} already exists.")
                return user
        new_user=User(name, user_id)
        self.user_list.append(new_user)
        return new_user
        
    def remove_user(self, user_id):
        for user in self.user_list:
            if user.get_user_id() == user_id:
                self.user_list.remove(user)
                return f"User with ID {user_id} was successfully deleted."
            
            else:
                return f"User with ID: {user_id} was not exit!"

    def user_details(self,user_id):
        for user in self.user_list:
            if user.get_user_id() == user_id:
                return f"Name: {user.name}, ID: {user_id}, Borrowed books:{user.get_book_borr()}"
        return f"User with ID: {user_id} was not exit!"
            

    def display_all_users(self):
        for user in self.user_list:
            print(user,"\n")
            
 # Return book section.

    def return_book(self,user_id, isbn):
        for book in self.book_list:
            if book.get_isbn() == isbn:
                no_of_books = int_valid("No.of books returning: ")
                book.tot_books += no_of_books
                print("Returnging Book.")
                return f"User {user_id} >> {isbn} >> {datetime.date.today()}"
        return f"Book with ISBN: {isbn} is not there!"
            
        
    
def int_valid(message = "Enter user Id: "):
    while True:
        try:
            user_id = int(input(message))
            if user_id > 0:
                return user_id
            else:
                print("User ID should be greater than 0.")
        except ValueError:
            print("\nPlease! enter valid input.\n")

def get_book_info(message = "Enter book details"):
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    tot_books = int_valid("Total no.of books: ")    
    return title, author, isbn, tot_books