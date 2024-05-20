
num1 = int(input("Enter first Number:"))
num2 = int(input("Enter Second Number:"))
op = input("Enter Operator (*,**,/,+,-,%)")

def cal(num1,num2):
    if op == "*":
        print(num1*num2)
    elif op == "/":
        print(num1/num2)
    elif op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num1)
    elif op == "**":
        print(num1**num2)
    elif op == "%":
        print(num1%num2)
    else:
        print("Invlaid Operatorl")
        return 0

print(cal(num1,num2))