section1 = "The UNBREAKABLE Calculator:"
section1 = section1.upper()

print(section1)

print("\nWelcome! Feast your eyes upon the great Calcu-maton! Enter two numbers below and prepare to be amazed!~ \n")

start = str(input("Do you want to use the calcu-maton? \n <YES>    <NO> \n")).upper()

if start == "YES":
  calc_run = True
if start != "YES":
  calc_run = False
  print("Alas, now is not the time for trickery. Goodbye and have a jolly good day!")

  
while calc_run == True:

  operations = ["+","-","*","/"]

  def add(num1,num2):
    total = num1 + num2
    return total
  def subtract(num1,num2):
    total = num1 - num2
    return total
  def multiply(num1,num2):
    total = num1 * num2
    return total
  def divide(num1,num2):
    total = num1 / num2
    return total
    
  
  try:
    num1 = float(input("Enter your first number: ")) 
    valid_num1 = True
  except ValueError:
    print("Nice try.")
    valid_num1 = False
    continue

  operation = str(input("Enter your operation: "))
  '''operations = ["+","-","*","/"]'''
  for o in operations:
    if operation in operations:
      valid_opp = True
    else:
      valid_opp = False

  while valid_opp == False:
    operation = str(input("Try again. Enter an appropriate symbol. "))
    
    if operation in operations:
      valid_opp = True
  
  try:
    num2 = float(input("Enter your second number: ")) 
    valid_num2 = True
  except ValueError:
    print("Nice try.")
    valid_num2 = False
  while valid_num2 == False:
    
    try:
      num2 = float(input("Enter your second number: ")) 
      valid_num2 = True
    except ValueError:
      print("Nice try.")
      valid_num2 = False
      continue
    

  for o in operations:
    if operation == "+":
      result = add(num1,num2)
    elif operation == "-":
      result = subtract(num1,num2)
    elif operation == "*":
      result = multiply(num1,num2)
    elif operation == "/":
      if num2 != 0:
        result = divide(num1,num2)
      else: 
        result = "Undefined. You cannot divide by zero"
     
  print(f"\nYour total is: {result}.\n")