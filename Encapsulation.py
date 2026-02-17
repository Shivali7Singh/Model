# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def add_amount(self,amount):
#         self.__balance +=amount
#     def withdraw(self,amount):
#       if amount <= self.__balance:
#          self.__balance -= amount
#     def show_balance(self):
#        return self.__balance
# x = BankAccount("Shivali",1000)
# x.add_amount(500)
# x.withdraw(300)
# print(x.show_balance())


# class ATM:
#    def __init__(self,pin,balance):
#       self.__pin = pin
#       self.__balance = balance
#    def check_balance(self,pin):
#       if pin == self.__pin:
#          return self.__balance
#       else:
#          return "Incorrect Pin"
# x=ATM(1234,6000000000)
# print(x.check_balance(1234))

#ENCAPSULATION
class Employee:
   def __init__(self,name,salary):
      self.name =name
      self.__salary = salary
   def display_name(self):
      return self.name
    #   print("Employee name")
   def update_salary(self,amount):
      if amount <= 100000:
         self.__salary += amount
         print("salary updated successfuly:",self.__salary)
      else:
         print("Please enter a positive amount.")
   def show_salary(self):
       return self.__salary
a = Employee("riya",16000)
print("Employee name:",a.display_name())
a.update_salary(6000)
print("updated salary:",a.show_salary())
         
        
    