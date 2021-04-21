#for checking
#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
deposite= input("how much that you want deposite")
takingmoney=input("how much that you want to take money?")

class thebank :
  def __init__(self,name,surname,age):
    self.name = name
    self.surname= surname 
    self.age= age

  def sayhello(self):
    print("welcome our bank {name} ".format(name=self.name))

class customer (thebank):
  def __init__(self,name,age):
    self.name =name
    self.age=age 
    self.remainder=100
  def what_is_remainder(self):
    return self.remainder
  def todeposite(self):
    self.remainder += deposite
  def takemoney(self):
    self.remainder -=takingmoney

customer1 = customer("kemal",23)
print(customer1.sayhello())
print(customer1.what_is_remainder())

