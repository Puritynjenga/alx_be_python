
#create a class called book that has the following attributes
class Book:
    def __init__(self, title:str ,author:str,year:int): #condtructor to initialize the attributes
        self.title = title
        self.author = author
        self.year = year


    def __str__(self):  #represent the book object in a readable string format
        return f"{self.title} by {self.author}, published in {self.year}"

    def  __del__(self):
        print(f"Deleting {self.title}")  #close the title of the book once the object is deleted

    def __repr__(self):  #book object representation for  debugging and logging 
        return f"Book('{self.title}', '{self.author}', {self.year})"
        
         



