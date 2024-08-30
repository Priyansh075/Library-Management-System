class Library :
    def __init__(self,list) :
        self.books = list

    def showavailablebooks(self) :
        print("Available books are : \n")
        for book in self.books :   
            print("*" + book)

    def borrowbook(self,bookname) :
        if bookname in self.books :
           print(f"You have issued {bookname} , Plzz keep it safe ")
           self.books.remove(bookname)
           return True
        
        else :
            print("Sorry, This book is unavailable")
    def returnbook(self,bookname) :
        print("Thanks for returning this book")
        self.books.append(bookname)
        return False

class Student :
    def __init__(self):
        self.mybooklist = []

    def requestbook(self) :
        self.reqbook = input("Enter the book you want to borrow : ")
        return self.reqbook
        self.mybooklist.append(self.reqbook)

    
    def returnbook(self) :
        self.rbook = input("Enter the book name you want to return : ")
        return self.rbook
        self.mybooklist.remove(self.rbook)

   


if __name__ == "__main__":
    centrallibrary = Library(["python","algorithms","django","java scripts"])

    

    while(True) :
        starkk = Student()

        welcomeMsg = "===== WELCOME TO CENTRAL LIBRARY ====="

        print(welcomeMsg)


        print('''\nChoose a option to proceed :
        1. Show Available Books 
        2. Borrow a Book
        3. Return a Book
        4. Exit Library \n''')

        choice = int(input("Enter your choice : "))
        if choice==1 :
            centrallibrary.showavailablebooks()

        elif choice==2 :
            centrallibrary.borrowbook(starkk.requestbook())

        elif choice==3 :
            centrallibrary.returnbook(starkk.returnbook())

       

        elif choice==4 :
            exit()

        else :
            print("invalid choice!")


            