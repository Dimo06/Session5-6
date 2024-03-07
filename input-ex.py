name = input("what is your name? ")
age = input("How old are you? ")

try:
    age = int(age)
    birth_year = 2023 - age
    print(name, "you were born in", str(birth_year) + ".")
    number= input("Provide a number to divide the age ")
    number = int(number)
    print(age/number)
except ValueError:
    print("Invalid age")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Unknown Error")
else:
    print("No exceptions were raised.")
finally:
    print("Thank you for playing!")