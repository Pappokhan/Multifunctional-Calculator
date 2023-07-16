#Project name is Multifunctional Calculator
#Normal Calculator 
#Bmi calculator 
#Birth calculator
#Discount calculator

import datetime

def normal_calculator():
    print()
    print("--CALCULATOR--")
    n1 = float(input("Enter your 1st number: "))
    n2 = float(input("Enter your 2nd number: "))
    oprator = input("Enter an operator (+, -, *, /): ")
    if oprator == "+":
        print("Addition is: ", n1 + n2)
    elif oprator == "-":
        print("Subtraction is: ", n1 - n2)
    elif oprator == "*":
        print("Multiplication is: ", n1 * n2)
    elif oprator == "/":
        print("Division is: ", n1 / n2)
    else:
        print("Invalid operator...")


def bmi_calculator():
    print()
    print("--BMI CALCULATOR--")
    weight = float(input("Enter your weight in kilograms : "))
    height = float(input("Enter your height in meters    : "))
    bmi = weight / (height ** 2)
    category = " "
    if bmi < 18.5:
        category = "You are: Underweight"
    elif bmi >= 18.5 and bmi < 25:
        category = "You are: Normal weight"
    elif bmi >= 25 and bmi < 30:
        category = "You are: Overweight"
    else:
        category = "Obese..."
    print("Your BMI is: ", round(bmi, 2))
    print("Category is: ", category)


def birth_calculator():
    print()
    print("--BIRTH CALCULATOR--")
    year = int(input("Enter your birth year           : "))
    month = int(input("Enter your birth month (1-12)   : "))
    day = int(input("Enter your birth day            : "))
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    print("Your age is: ", age)


def discount_calculator():
    print()
    print("--DISCOUNT CALCULATOR--")
    a = int(input("Enter List price     : "))
    b = int(input("Enter selling price  : "))
    dis = (a-b)/a*100
    print("Your Discount is: ", dis, " % ")

while True:
    print()
    print("Welcome to Multifunctional Calculator!")
    print()
    print(" 1. Normal Calculator    __")
    print(" 2. BMI Calculator       __")
    print(" 3. Birth Calculator     __")
    print(" 4. Discount Calculator  __")
    print()
    choice = input("Choice your Calculator (1 - 4): ")

    if choice == "1":
        normal_calculator()
    elif choice == "2":
        bmi_calculator()
    elif choice == "3":
        birth_calculator()
    elif choice == "4":
        discount_calculator()
    elif choice:
        print("Invalid choice...")
        print()
        
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        pass
