class Library:
    def __init__(self,list_of_books,name):
        self.book_list=list_of_books
        self.name=name
        self.lendDict={}
    def displayBooks(self):
        print("We have the following books available in our library: ")
        for book in self.book_list:
            print(book)
    def LendBook(self,user,book):
        if book not in self.book_list:
            print(f"Sorry! the book {book} is not available with us")
        elif book in self.lendDict:
            print(f"The book {book} is already lent to {self.lendDict[book]}")
        else:
            self.lendDict[book]=user 
            print(f"Lender - Book Database has been updated. Yopu can take the book now.")

    def addBook(self, book):
        self.book_list.append(book)
        print(f"The book {book} has been added to the library.")

    def returnBook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            print(f"The book {book} has been returned.")
        else:
            print(f"The book {book} was not borrowed from us.")
books = Library(["The story of my experiments with truth","Sapiens","The theory of everything","The big bang theory"],"Readers Library")

user_name= input("Welcome top thr Readers Library.\n Please enter your name: ")

while True:
    print(f"Hello {user_name}! Welcome to the {books.name}\n Please choose an option: ")

    print("1.Display Books\n2. Lend a book\n3. Add a book\n4.Return a book\n5.Quit")

    choice=int(input("Enter your choice: "))

    if choice not in [1,2,3,4,5]:
        print("Enter a valid option")
        continue

    if choice==1:
        books.displayBooks()
    elif choice==2:
        book_name=input("Enter the book name")
        books.LendBook(user_name,book_name)
    elif choice==3:
        book_add=input("Enter the book to add: ")
        books.addBook(book_add)
    elif choice==4:
        book_return=input("Enter the book to return: ")
        books.returnBook(book_return)
    elif choice==5:
        print(f"Thank you for using our library,{user_name}! Good Bye")
        break
