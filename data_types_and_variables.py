Identify the data type of the following values:


99.9      ---FLOAT

"False"   ---STR

False     ---BOOL

'0'       ---STR

0        ---INT

True    ---BOOL 

'True'  ---STR

[{}]     ---LIST

{'a': []}  ---DICT

What data type would best represent:

A term or phrase typed into a search box?  ---STR
If a user is logged in?  ---BOOL
A discount amount to apply to a users shopping cart?   ---INT
Whether or not a coupon code is valid?   ---BOOL
An email address typed into a registration form?   ---STR
The price of a product?   ---FLOAT
A Matrix?  ---DICT
The email addresses collected from a registration form?  ---LIST
Information about applicants to Codeups data science program?  ---DICT

'1' + 2 ---TypeError

6 % 4 ---2

type(6 % 4) ---INT

type(type(6 % 4)) --=type

'3 + 4 is ' + 3 + 4  ---TypeError

0 < 0 ---False

'False' == False  ---False

True == 'True'  ---False

5 >= -5 ---True

True or "42"   ---True

6 % 5  ----1

5 < 4 and 1 == 1   ---False

'codeup' == 'codeup' and 'codeup' == 'Codeup'  ---False

4 >= 0 and 1 !== '1' ---SyntaxError: invalid syntax

6 % 3 == 0  ---True

5 % 2 != 0   ---True

[1] + 2 ---TypeError

[1] + [2] ---- [1, 2]

[1] * 2  ----[1, 1]

[1] * [2] -------TypeError

[] + [] == []  ---True

{} + {}  ----TypeError


You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, 
they love it), and Hercules (1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, how much will you have to pay?

price = 3
days = 3
total = days * price

print (total)


Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:


username = 'codeup'
password = 'notastrongpassword'
Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters
the username must be no more than 20 characters
the password must not be the same as the username
bonus neither the username or password can start or end with whitespace
BONUS

For practicing with list comprehensions, work through 17 List Comprehension Exercises. Add your solutions to a new file named list_comprehensions.py

For even more practice with all your Python tools together, work through 20 Python Data Structure Manipulation Exercises. Name this file python_data_structure_manipulation_exercises.py.