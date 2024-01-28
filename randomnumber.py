import random

def arithmetic_quiz():
    correct = 0
    num_questions = 5
    for i in range(num_questions):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(['+', '-', '*'])
        question = f"What is {a} {op} {b}? "
        answer = eval(str(a) + op + str(b))
        user_answer = input(question)
        if int(user_answer) == answer:
            print("Correct!")
            correct += 1
        else:
            print(f"Sorry, the correct answer is {answer}")
    print(f"You got {correct} out of {num_questions} correct.")

arithmetic_quiz()
