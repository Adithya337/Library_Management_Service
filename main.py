obj_list=[]
status={}
issue_id=1000
issue_record={}

class bookList:
    def __init__ (self,isbn,title,author,category,price):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.category=category
        self.price=price
        status[self.isbn]="Available"
def addBook():
    isbn=input("Enter the ISBN value of the book:")
    title=input("Enter the Title of the book:")
    author=input("Enter the author of the book:")
    category=input("Enter the category to which the book belongs:")
    price=int(input("Enter the price of the book:"))
    obj_list.append(bookList(isbn,title,author,category,price))
    print("You have successfully added the book in the list.Thank you.")
def findBookByCategory():
    cate=input("Enter the Category of the books which you want :")
    ans=[]
    for i in obj_list:
        if i.category.lower() == cate.lower() :
            ans.append(i)
    print("The books of the given category are:")
    for i in ans:
        print(f'ISBN Value:{i.isbn} Title : {i.title} Author : {i.author} Category : {i.category} Price : {i.price}')
        print("********************")
def findBookByIsbn():
    isbn_value=input("Enter th ISBN value of the book which you want to search:")
    flag=0
    for i in obj_list:
        if i.isbn == isbn_value:
            print("The details of book are:")
            print(f'ISBN Value:{i.isbn} Title : {i.title} Author : {i.author} Category : {i.category} Price : {i.price}')
            flag=1
    if flag == 0:
        print(f"The book having ISBN Value {isbn_value} is not found .Please enter correct ISBN Value.")
def issue_func():
    issue_title=input("Enter the title of the book you want to take:")
    author_issue=input("Enter the author of the book you want to take:")
    category_issue=input("Enter the category of the book you want to take:")
    flag=0
    for i in obj_list:
        if i.title.lower()==issue_title.lower() and author_issue.lower()==i.author.lower() and category_issue.lower()==i.category.lower() and status[i.isbn]=="Available":
            global issue_id
            issue_id += 1
            print("The book is issued.")
            print(f"Issue id is {issue_id}.")
            issue_record[issue_id]=[i.isbn,"24/05/2023"]
            status[i.isbn]="Unavailable"
            flag=1
    if flag==0:
        print("The requested book is unavailable.Sorry!!")
def book_return():
    iss_id=int(input("Enter the issue id:"))
    if iss_id in list(issue_record.keys()):
        status[issue_record[iss_id][0]]="Available"
        del issue_record[iss_id]
        print("The return of book is successful.Thank you.")
    else:
        print("We regret . We cant process your return request . Please try again by entering correct issue id.")
def book_remove():
    isbn_remove=input("Enetr the ISBN value of the book you want to remove from the list:")
    flag=0
    for i in obj_list:
        if i.isbn == isbn_remove and status[i.isbn]=="Available":
            obj_list.remove(i)
            print("Book is removed from the list.Thank you.")
            flag=1
    if flag==0:
        print("We cant process your request. Please try again.")



print("******************************Welcome to the libray management system******************************")
while(True):
    print('---------------------------------------')
    print('Please select the option which you want to perform:')
    print('1.To add a book to list.')
    print('2.To find a book by category.')
    print('3.To find a book by ISBN Value.')
    print('4.To issue a book.')
    print('5.To return a book.')
    print('6.To remove a book from the list.')
    print('7.To Exit.')
    val=int(input("Enter your option:"))
    if val == 1 :
        addBook()
    elif val == 2 :
        findBookByCategory()
    elif val == 3:
        findBookByIsbn()
    elif val == 4:
        issue_func()
    elif val == 5:
        book_return()
    elif val == 6:
        book_remove()
    else:
        print("Thank you for using Library Management System.")
        exit()



        


