
def palindrome(str):
    str1 = str
    str2 = str [::-1]
    if str1 == str2 :
        return "Palindrome"
    else :
        return "Not Palindrome"
    

str = "madam"
print(palindrome(str))