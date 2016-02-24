from mypytest.employee.emp_pack import Employee
from mypytest.customer.customer_pack import Customer
import os


def print_menu():
    print('1. View Employee Detail')
    print('2. View Customer Deatail')
    print('3. Quit')
def main():
 e = Employee()
 c = Customer()
 os.system('cls')
 choice = 0
 
 while (choice != 3):
   os.system('cls')
   print_menu()
   choice = int(input("Enter Your Choice"))
   if choice == 1:
     e.read_Emp()
   elif choice == 2:
    c.read_Customer()
   elif choice == 3:
      break
   else:
      #os.system('cls')
      print_menu()

 print("Goodbye")

if __name__ == '__main__':
  main()
