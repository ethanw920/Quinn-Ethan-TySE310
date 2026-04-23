import math



team_name = "Quinn-Ethan-TyS310"



def calculator():
  print("Calculator by team =  " + team_name)
  print("Choose the operation you want to perform: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Integer Division")
  print("6. Square Root")
  print("7. Exponent")

  choice = int(input("Enter your choice: "))
  
  number1 = float(input("Enter the first number: "))
  
  if not choice == 6:
    number2 = float(input("Enter the second number: "))
  
  match choice:
    case 1:
      addition(number1, number2)
    case 2:
      subtraction(number1, number2)
    case 3:
      multiplication(number1, number2)
    case 4:
      division(number1, number2)
    case 5:
      intDivision(number1, number2)
    case 6:
      sqrt(number1)
    case 7:
      exponent(number1, number2)

def addition(number1, number2):
  print("We are adding " + str(number1) + " and " + str(number2))
  return number1 + number2

def subtraction(number1, number2): #Ty
  print("We are subtracting " + str(number2) + " from " + str(number1))
  return number1 - number2


def multiplication(number1, number2): #Ty
  print("We are multiplying " + str(number1) + " and " + str(number2))
  return number1 * number2

def division(number1, number2): #Ethan
  print("We are dividing " + str(number1) + " by " + str(number2))
  return number1 / number2
  
def intDivision(number1, number2): #Ethan
  print("We are performing integer division of " + str(number1) + " by " + str(number2))
  return number1 // number2

def sqrt(number1): #Quin
  print("We are taking the square root of " + str(number1))
  return math.sqrt(number1)

def exponent(number1, number2): #Quin
  print("We are taking " + str(number1) + " to the power of " + str(number2))
  return math.pow(number1, number2)

calculator()