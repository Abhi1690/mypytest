import os
ROOT = os.path.dirname(__file__)
class Customer:
  def __init__(self):
     self.name = 'Customer'

  def read_Customer(self):
    infile = open(os.path.join(ROOT, 'Customer.txt'))
    inline = infile.readline()
    os.system('cls')
    print(inline)
    raw_input("Press Enter to continue..")
    infile.close()
print(ROOT)
