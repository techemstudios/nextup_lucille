import turtle

frank = turtle.Turtle()

number1 = int(raw_input("Give me a number: "))
number2 = int(raw_input("Give me another number: "))

operation = raw_input("What operation? ")

if operation == '+':
	answer = number1 + number2
	
if operation == '-':
	answer = number1 - number2

if operation == '*':
	answer = number1 * number2

if operation == '/':
	answer = number1 / number2
	
print("\nCheck out the turtle window to see the answer!")
	
frank.write(answer, font = (None, 40, "bold"))
turtle.done()

