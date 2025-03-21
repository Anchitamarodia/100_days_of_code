# calculator
from art import logo
def add(num_1,num_2):
  return num_1 + num_2

def substract(num_1,num_2):
  return num_1 - num_2

def multiply(num_1,num_2):
  return num_1 * num_2

def divide(num_1,num_2):
  return num_1 / num_2

def exponent(num_1,num_2):
  return num_1 ** num_2
def calculator():
  print(logo)
  operation={
    '+':add
    ,'-':substract
    ,'*':multiply
    ,'/':divide
    ,'**':exponent
  }
  con_tinue=''
  num1=float(input('what is the first number?'))
  while con_tinue=='' or con_tinue=='y':
    for i in operation:
      print(i)
    operation_symbol=input('pick an operation from the above line ')
    
    num2=float(input('what is your number?'))
    
    answer=operation[operation_symbol](num1,num2)
    print(f"\n{num1}{operation_symbol}{num2}={answer}")
    
    con_tinue=input('do you want to continue? press y to continue and n to exit ')
    
    if con_tinue=='n':
      print('thank you for using the calculator')
      calculator()
calculator()




