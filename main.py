import random


# Asking the User for minimum and maximum range for the questions given in this Programm
print("What is Your Minimum Number where the Question Starts?")
MIN_NUMBER = int(input("-:> "))
print("What is Your Maximum Number where the Question Ends?")
MAX_NUMBER = int(input("-:> "))

# Number of the question
NB_QUESTION = 10


def ask_questions(minimum, maximum):
    points = 0

    # print the question and take input
    for i in range(NB_QUESTION):
        # Generate random numbers from given range
        a = random.randint(minimum, maximum)
        b = random.randint(minimum, maximum)

        # Generate Operators
        operators = ["+", "-", "*", "/"]
        operator = random.choice(operators)

        print(f"Q.{i+1} of {NB_QUESTION} => {a} {operator} {b} = ?")
        answer = int(input("-:> "))

        # Configure Compute Variable
        if operator == "+":
            compute = a+b
        elif operator == "-":
            compute = a-b
        elif operator == "*":
            compute = a*b
        else:
            compute = a/b

        # Check Answer and Give Result
        if answer == compute:
            print("Right")
            points += 1
        else:
            print("Wrong")

    print(f"You Have {points} points out of {NB_QUESTION} .")

    if points == NB_QUESTION:
        print("Excellent!")
    elif points == 0:
        print("You Have To Improve Your Maths!")
    elif points == (NB_QUESTION/2):
        print("Good!")
    elif points > (NB_QUESTION/2):
        print("Very Good!")
    elif points < (NB_QUESTION/2):
        print("You Can Be More Accurate and Better!")


# Calling the ask_question function for asking the question
ask_questions(MIN_NUMBER, MAX_NUMBER)
