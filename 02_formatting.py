"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""
password = input("Put in a password ")
check_password = input("Confirm your password ")
if check_password == password:
    print("Your password is good ")
else :
    print("Try again ") 


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
ustring=input("In put a string ")
ustring=ustring.strip()
if bool(ustring) == True:
    print("This is a valid string ")
else:
    print("This is a invalid string ")
"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
cat = "Cat".lower()
dog = cat.replace("cat","Dog").lower()
print(cat, dog)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
username = input("What is your name ")
userage = input("What is your age ")
print(username, userage)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
d1 = float(input("Put in decimal "))
d2 = float(input("Put in decimal "))
quotient = d1 / d2
pquotient = f"{d1} / {d2} = {quotient:.1f}"
print(quotient)