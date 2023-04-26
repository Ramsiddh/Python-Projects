print("Welcome to my Python quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Question 1
question = "What is the output of the following code?\nx = 2\ny = 5\nprint(x + y)\n"
answer = input(question)
if answer == "7":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 2
question = "What does the print() function do in Python?\n"
question += "A) Prints the value of a variable\n"
question += "B) Outputs text to the console\n"
question += "C) Waits for user input\n"
question += "D) None of the above\n"
answer = input(question)
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 3
question = "Which of the following is not a valid Python variable name?\n"
question += "A) my_var\n"
question += "B) 123var\n"
question += "C) var123\n"
question += "D) _myvar\n"
answer = input(question)
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 4
question = "What does the % operator do in Python?\n"
question += "A) Multiplies two numbers\n"
question += "B) Divides two numbers\n"
question += "C) Calculates the remainder of a division operation\n"
question += "D) None of the above\n"
answer = input(question)
if answer.lower() == "c":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Question 5
question = "How do you create a comment in Python?\n"
question += "A) Use double slashes (//)\n"
question += "B) Use a hashtag (#)\n"
question += "C) Use double dashes (--)\n"
answer = input(question)
if answer.lower() == "b":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
