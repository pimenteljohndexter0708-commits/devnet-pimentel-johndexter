"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Pimentel John Dexter
Date: 25/09/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================

So this lesson is about Control Flow. I'm going to explain if/elif/else statement. This statements is used for conditions. This is a conditional statements.
Following the program, the first thing or condition that will be considered or checked is the if statement. If the condition inside "if" is True, then it will print
the code inside the if statement. So how about if it's false?
The next is elif statement. Elif statement is the one catching the condifiton if it's not fit or it's not met by the if statement. Just like the If statement, the elif also 
have a block of code inside. So if the condition is met, it will execute the code. You can also put as many elif as you want. But if the condition is not met or if it's false,
it will directly go to the else statement. The else statement is just like the last security, if all of the conditions are false, it will execute the code inside the else statement. 
And lastly, the else statement doesn't have any condition.

============================================
KEY VOCABULARY
============================================
- condition: This is where the program will going to base. This is going to be checked, if it's true or false. 
- if / elif / else: This are condtional statements. This is where you put your conditions.
- comparison operator: This is the operator usually used inside the conditional statement. It is used to compare two values. 
- boolean expression: This is a true or false output.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- 
# 

uname = input("Enter your username: ")
password = input("Enter your password: ")

if(uname == "akoto" and password == "diakoto"):
    print("Login successful!")
else:
    print("Invalid username or password.")
    

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

Sometime when I'm using if/else statement, I sometimes forgot to use the word "and' and "or" when using logical operators. I always make a mistake in this, because in other programming 
language like the java, they use "&&" and "||" to combine to conditions. 


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
