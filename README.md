This is my calculator app!

To use, please make a clone of this repo, then in the same directory as calculator.py, type 

$ python calculator.py

to run the server, then open http://localhost:8000/ in your browser

This calculator has 4 actions: add, subtract, multiply, & divide.
To use the calculator, add a / followed by one of those actions, followed by another slash, and then two numbers, separated by a slash.

Example:
http://localhost:8000/add/8/7 will add the numbers 8 and 7

For subtraction and division, where order of the numbers matters, the first number is the number being subtracted against, or divided by the other number, the order you would expect to find it written out.

It should be noted that this calculator uses decimals, not floats, and is therefore better than the latest OSX calculator.