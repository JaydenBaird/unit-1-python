"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
float_number = float(13.37)
int_number = int(float_number)


print (float_number)
print (int_number)

    
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

num = float(input("Put in a number: "))
if num > 0:
   print("Positive")
elif num == 0:
   print("Zero")
else:
   print("Negative ")

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
f_num = int(input("Put in a number: "))
s_num = float(input("Put in a number: "))
f_s_sum = f_num + s_num
f_s_sub = f_num - s_num
f_s_mul = f_num * s_num
f_s_div = f_num // s_num

print(f_s_sum)
print(f_s_sub)
print(f_s_mul)
print(f_s_div)

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
Fruits = {
   'Lemon':1,
   'Apple': 2,
   'Raspberries':3,
   'Orange':4,
   'Strawberry':5
}
print(Fruits["Orange"])
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
Bstr = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0"
Tuple = Bstr.split(",")
print(Bstr)
print(Tuple)