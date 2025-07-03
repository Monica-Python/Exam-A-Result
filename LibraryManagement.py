# -*- coding: utf-8 -*-
"""
PGR107 Python Programming Exam 2025
Authors: Candidate 63 and 13
Sources: https://emojipedia.org/ 

Question 2 - Library Management System

Defines a Book Class with title, author, num_pages, availability, and a Library Class
that manages a list of books with add, remove, check out, check in, and print 
operations.
Includes a test script that exercises all methods and prints the outcomes.

Emojis and separators were included to make the output more visual and improve 
readability.

"""

# Book class
class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.available = True #Added to use available status on the books
        
    def __str__(self):
        return f"The book '{self.title}' by {self.author} with {self.num_pages} pages."

# Library class
class Library: 
    def __init__(self):
        self.books = []
        print("\n")
        
    def add_book(self, book): #Function to add book
        self.books.append(book)
        print(f"Added {book}")
        print("---------")
        
    def remove_book(self, title): #Function to remove book
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Removed book: {title}")
                return
        print(f"Book '{title}' not found in the library")

    def check_in(self, title): #Function for check in
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    print(f"This book was never checked out: {title}")
                else:
                    book.available = True
                    print(f"Returned: {title}")
                return
        print(f"Book '{title}' not found in the library")


    def check_out(self, title): #Function for check out
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You checked out '{title}', enjoy! 📚")
                else:
                    print(f"'{title}' is unfortunately not available. 😞")
                return
        print(f"Book '{title}' not found in the library.")

    def print_books(self): #Function to print all the books in the library
        if len(self.books) == 0:
            print("There seems to be no books in this library yet.")
        else:
            print("\nBooks available in our library✅:")
            print("-------------------------------\n")
            for book in self.books:
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Number of pages: {book.num_pages}")
                status = "Available ✅" if book.available else "Checked Out ❌" #Available status
                print(f"Status: {status}")
                print("----")

                
"""
    Script test to verify the methods 
    The book titles and information is found from Ark.no
"""
    
def library_system():
    myLibrary = Library() #Library instanse
        
    #Books
    book1 = Book("The housemaid", "Freida McFadden", 336)
    book2 = Book("Iron Flame", "Rebecca Yarros", 800)
    book3 = Book("Cozy corner", "Coco Wyo", 96)
    book4 = Book("Fearless", "Lauren Roberts", 528)
    book5 = Book("Verity", "Colleen Hoover", 336)
        
    #Add books to library
    myLibrary.add_book(book1)
    myLibrary.add_book(book2)
    myLibrary.add_book(book3)
    myLibrary.add_book(book4)
    myLibrary.add_book(book5)
    
    print("\n")
                
    #Check out a book
    print("Checkout: ")
    myLibrary.check_out("The housemaid")
    #Check out a book that doesn't exist:
    myLibrary.check_out("SomeCoolBook")
    #Trying to check out the same book:
    myLibrary.check_out("The housemaid") #Prints that the book is not available since its alredy checked out(To show we handled doublebookings)
    #Checked out another one to show available status in the prints
    myLibrary.check_out("Cozy corner")    
    
    #Checking the book back in again:
    print("\nCheck in: ")
    myLibrary.check_in("The housemaid")
    #Check in a book that doesn't exist:
    myLibrary.check_in("SomeCoolBook")
    #Trying to check in the same book:
    myLibrary.check_in("The housemaid") #Prints that the book was not checked out since it was returned(To show we handled doublebookings)
        
    #Remove a book:
    print("\nRemoved: ")
    myLibrary.remove_book("The housemaid")
    #remove a book that doesn't exist:
    myLibrary.remove_book("SomeCoolBook")
        
    #Print all the books in the library
    myLibrary.print_books()
        
library_system()