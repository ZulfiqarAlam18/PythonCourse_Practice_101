
my_list = [2,4,6,8,9,10]

# one way
#print(2 in my_list)

# another way
count = 0
for find in my_list:
    if find == 11:
        print(True)
        break
    count +=1
    if count == 6:
        print(False)