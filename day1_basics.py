#day1_basic.py
print("===Day1: Basics===")
#task A - name and age and roll
name=input("write your name:")
age=int(input("write your age:"))
roll=int(input("write your roll"))
print(f"Hello {name},{age+5},{roll}")



# Task B - bigger of two numbers
a = float(input("প্রথম নম্বর: "))
b = float(input("দ্বিতীয় নম্বর: "))
if a > b:
    print("বড় নম্বর:", a)
elif b > a:
    print("বড় নম্বর:", b)
else:
    print("দুইটি সমান।")

# Task C - calculator with % and power
num1 = float(input("Calculator - প্রথম নম্বর: "))
op = input("অপারেটর (+, -, *, /, %, **): ")
num2 = float(input("Calculator - দ্বিতীয় নম্বর: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")
elif op == "%":
    print("Result:", num1 % num2)
elif op == "**":
    print("Result:", num1 ** num2)
else:
    print("Invalid operator!")
