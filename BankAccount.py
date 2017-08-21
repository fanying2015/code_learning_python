# BankAccount

"""In this project, a Python class that can be used to create and manipulate a personal bank account will be created

the functions of BankAccount include:

Accepting deposits
Allowing withdrawals
Showing the balance
Showing the details of the account"""

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print " Balance: $%.2f" % (self.balance)
    
  def deposit(self, amount):
    self.amount = amount
    if amount <= 0:
      print "Invalid input"
      return
    else:
      print "The deposit amount is $%.2f" % (self.amount) 
      self.balance += self.amount
      self.show_balance()
      
  def withdraw(self, amount):
    self.amount = amount
    if amount <= 0 or amount > self.balance:
      print "Error!"
      return
    else:
      print "The withdrawl amount is $%.2f" % (self.amount) 
      self.balance -= self.amount
      self.show_balance()
 
my_account = BankAccount(name = "Fanying")
print my_account

my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account
