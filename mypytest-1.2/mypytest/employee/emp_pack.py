import os
ROOT = os.path.dirname(__file__)
class Employee:

 def __init__(self):
   self.name = 'Employee'


 def read_Emp(self):
   in_file = open(os.path.join(ROOT, 'Employeetf.txt'))
   in_line = in_file.readline()
   os.system('cls')
   print(in_line)
   raw_input("Press any key to continue")
   in_file.close()

print(ROOT)

