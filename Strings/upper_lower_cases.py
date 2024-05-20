
str = input("Enter your String:")
upper_string = str.upper()
lower_string = str.lower()

try:
    print("Upper Case :",upper_string)
    print("lower Case :",lower_string)
    print("Number of letters in String :",len(str)) 
except ValueError:
    print("Error...........Try later")
finally:
    print("Operation Completed!!!!!")
