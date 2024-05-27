import os
import datetime


class Library:
    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name
        self.books_dict={}
        id=101


        with open('list_of_books.txt','r') as f:
            a=f.readlines()
            for i in a:
                self.books_dict.update({id:{'book_title':i.removesuffix("\n"),'status':'Available'}})
                id=id+1

    def display_book(self):
        print("BOOK ID \t\t BOOK TITLE \t\t STATUS")
        print("---------------------------------------------------------")
        for key,value in self.books_dict.items():
            print(key,"\t\t",value.get('book_title'),"\t\t",value.get('status'))
    
    def Issue_books(self):
        book_id=int(input("Enter BOOK ID:"))
        current_date=datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['status']=='Available':
                user_name=input("Enter The User Name:")
                self.books_dict[book_id]['user_name']=user_name
                self.books_dict[book_id]['current_date']=current_date
                self.books_dict[book_id]['status']='Already Issued'
                print("BOOK ISSUED SUCCESSFULL")
            elif self.books_dict[book_id]['status']!='Available':
                print(f"This BOOK is alredy Issued by {self.books_dict[book_id]['user_name']} on {self.books_dict[book_id]['current_date']}")
        else:
            print("BOOK ID IS NOT FOUND")
    
    def return_books(self):
        book_id=int(input("Enter BOOK ID:"))
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]['status']=='Available':
                print("This Book is already Available in the Library")
            elif self.books_dict[book_id]['status']!='Available':
                self.books_dict[book_id]['user_name']=''
                self.books_dict[book_id]['current_date']=''
                self.books_dict[book_id]['status']='Available'
                print("Book Returned Sucessfully")
        else:
            print("BOOK ID IS NOT FOUND")


try:
    l1=Library('list_of_books.txt','abc library')
    key_press_list={'D':'DISPLAY BOOKS','R':'RETURN BOOKS','I':'ISSUE BOOKS','Q':'QUIT'}

    key_press=''

    while not (key_press == 'q'):
        print()
        print(".........WELCOME.........")
        print()
        for key,value in key_press_list.items():
            print("Press",key,'To',value)
        key_press=input("enter the key: ").lower()
        if key_press=='d':
            print("\n CURRENT SELECTION IS DISPLAY BOOKS \n")
            l1.display_book()
        elif key_press=='i':
            print("\n CURRENT SELECTION IS ISSUE BOOKS \n")
            l1.Issue_books()

        elif key_press=='r':
            print("\n CURRENT SELECTION IS RETURN BOOKS \n")
            l1.return_books()

        elif key_press=='q':
            print("\n QUIT \n")
            print("THANK YOU")
            print()
            break
        else:
            continue

except Exception as e:
    print("Something Went Wrong. Please Check again!!!!!")

        

                