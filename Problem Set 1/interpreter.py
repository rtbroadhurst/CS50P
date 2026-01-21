# takes an input in the format x y z where x and z are numbers and y is a math operator (+, -, *, /)
# then performs the operation and prints the result as a float

num1, operator, num2 = input("Enter your maths expression: ").split()
num1 = float(num1)
num2 = float(num2)  

if operator == "+":
    print(float(num1 + num2))
elif operator == "-": 
    print(float(num1 - num2))
elif operator == "*":
    print(float(num1 * num2))    
elif operator == "/":
    print(float(num1 / num2))
