class Publisher:
    def __init__(self,name):
        self.name = name
    def display(self):
        pass
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title = title
        self.author = author
    def display(self):
        pass
class Python(Book):
    def __init__(self,name,title,author,price,page):
        Book.__init__(self,name,title,author)
        self.price = price
        self.page = page
    def display(self):
        print("Name=",self.name)
        print("Title=",self.title)
        print("Author=",self.author)
        print("Price = ",self.price)
        print("No of Pages=",self.page)
details = Python("Goodwill Books","Digital Fundamentals","Karl Pearson",3499,1200)
details.display()









