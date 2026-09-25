"""
Module 2 — Lesson 4: Functions
Student: Pimentel, John Dexter
Date: 25/09/2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================


A function is a block of code that will run only if it is called. For example, in an rpg game in CLI, you always open in your inventory to see your items. In the coding side of that, 
the code for the inventory is inside a funcion, everytime you going to use the inventory that function is going to be called. So instead of having copy of a block of code, you can
just have one function for that, and you just going to call the funciont whenever you need it.

============================================
KEY VOCABULARY
============================================
- function: A function is a block of code that will run only if you called it.
- def: The syntax or the keyword to create a function in python. 
- call: To execute or run the function.
- parameter: It is like a placeholder. This is inside the function. 
- arguments: When using the function, this is what you put on the parameter. This is the actual value. If you num1 and num2 in the parameter, you should put integer in the arguments.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# --- 
# 

def bomb():
  print("KABOOOM!!!")

ans = input("Do you want to go kaboom? ")

if ans.lower() == "yes":
  bomb()
else:
  print("You can't go kaboom")

# 
# 
#  ---


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what's something confusing or easy to get wrong
about this topic?]

In this topic, I remember having a struggle on understanding the arguments and parameters, and even now. In the game we did on game development, 
I remember that giving me a hard time tracking where that function leads, where I should find the arguments for that. But if I have a time to review it, it suddenly coming back to me.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
