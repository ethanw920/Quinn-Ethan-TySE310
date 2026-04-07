import math

#### TASK 1 - ENTER YOUR TEAM NAME AND NUMBER


team_name = "Quinn-Ethan-TyS310"

#### TASK 2 - Clone the empty gitHub repo in your local computer (Member #1)

#### TASK 3 - Add this code to your gitHub repo - follow the best practices of add --> commit --> pull --> push


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


#### TASK 4 (Member #2)- pull the gitHub repo in your local computer  and implement the SUBTRACTION function()

#### TASK 5 (Member #2)- Add the implemented the SUBTRACTION function() to your gitHub repo in a new branch called feature/subtract

#### TASK 6 (Member #3) - pull the gitHub repo in your local computer and implement the Multiplication function()

#### TASK 7 (Member #3) - Add the implemented the Multiplication function() to your gitHub repo in a new branch called feature/mult


#### TASK 8 (Member #4)- pull the gitHub repo in your local computer  and implement the Division function()

#### TASK 9 (Member #4)- Add the implemented the Division function() to your gitHub repo in a new branch called feature/div


#### TASK 8 (Member #1)- pull the gitHub repo in your local computer  and implement the IntegerDivision function()

#### TASK 9 (Member #1)- Add the implemented the IntegerDivision function() to your gitHub repo in the existing branch feature/div


#### TASK 10 (Member #2)- pull the gitHub repo in your local computer  and implement the SQRT function()

#### TASK 11 (Member #2)- Add the implemented the SQRT function() to your gitHub repo in the main branch
