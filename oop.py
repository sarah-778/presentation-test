# Object-Oriented Programming (OOP)

# Basic: 
# Create a class called Car with attributes brand and color. 
# Instantiate an object of the Car class and print its attributes.

# Intermediate: 
# Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. 
# Create an instance of Car and call the method.

class Car: 
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print(f"The car brand is {self.brand} and it has a {self.color} color.")  
        
    def start_engine(self):
        print(f"The engine of the car has started.")
         
car_1 = Car("Toyota", "Silver")
car_1.start_engine()



# Advanced: 
# Create a class called BankAccount with attributes account_number and balance. Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.




# Challenge: 
# Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. 
# The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).




