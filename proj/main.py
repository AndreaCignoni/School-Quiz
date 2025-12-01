# main.py
# Main entry point for the proj-part_A project.
# This program runs a series of quizzes, requesting input from the user,
# comparing responses with correct answers, and providing feedback through conditional branches.
# Input validation is handled with while loops to prevent errors.
# All files read and generated are stored in the "data" folder under the current directory.
# Author: Andrea Cignoni

import random
from datetime import datetime
import os

# Ask for user details
name = input("What is your first name? ")
last_name = input("What is your last name? ")
greeting = f"Hello, {name}."
print(greeting)

# Loop until user decides to finish
repeat_test = "no"
while repeat_test != "yes":
    
    menu = "\n1: Maths" + \
           "\n2: Italian" \
            "\n>>> "
    # Validate menu choice input
    while True:
        try:
            choice = int(input(menu))
            if 1 <= choice <= 2:
                break
            else:
                print("Please enter a valid number between 1 and 2.")
        except ValueError:
            print("Invalid input. Please enter a valid digit between 1 and 2.")
    # Maths quiz            
    if choice == 1:
        now = datetime.today() # Current timestamp
        topic = "MATHS"
        while True:
            try:
                num_question = int(input(f"{name}, how many questions? "))
                if 5 <= num_question <= 25:
                    break
                else:
                    print("Please enter a valid number between 5 and 25.")
            except ValueError:
                print("Invalid input. Please enter a valid digit between 1 and 25.")
        ADDITION = '+'
        SUBTRACTION = '-'
        numerator = 1
        answers = "\n"
        while numerator <= num_question:
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            operator = random.randint(1, 2)
            if operator == 1:
                operator = ADDITION
                correct_answer = num1 + num2
                while True:
                    try: 
                        answer = int(input(f"{numerator:<4}:{num1:>2} {operator} {num2} = "))
                        break
                    except ValueError:
                        print("Invalid input. Please insert a digit.")
                solution = (f"{numerator:<4}:{num1:>2} {operator} {num2} = {answer}")
            elif operator == 2:
                operator = SUBTRACTION
                if num1 > num2:               
                    correct_answer = num1 - num2
                    while True:
                        try:
                            answer = int(input(f"{numerator:<4}:{num1:>2} {operator} {num2} = "))
                            break
                        except ValueError:
                            print("Invalid input. Please insert a digit.")
                    solution = (f"{numerator:<4}:{num1:>2} {operator} {num2} = {answer}")
                else:
                    correct_answer = num2 - num1
                    while True:
                        try:
                            answer = int(input(f"{numerator:<4}:{num2:>2} {operator} {num1} = "))
                            break
                        except ValueError:
                            print("Invalid input. Please insert a digit.")    
                    solution = (f"{numerator:<4}:{num2:>2} {operator} {num1} = {answer}")
             # Provide feedback        
            if answer == correct_answer:
                feedback = "\033[1;95m\u2714\033[0m"
            else:
                feedback = "\033[1;91m\u2718\033[0m should be " + str(correct_answer)
            answers += solution + feedback + "\n"
            numerator += 1
        print(answers)
        # Log attempt with timestamp
        log =(f"\n{name} {last_name} - {topic} - {now.strftime('%B %d, %Y %H:%M:')}")
        if os.path.exists('proj/data/logs.txt'):
            with open ('proj/data/logs.txt', 'a') as f:
                f.write(log)
        else:
            with open('proj/data/logs.txt', 'w') as f:
                f.write(log)
        repeat_test = input("Are you finished (yes/no)? ")      

    # Language quiz
    elif choice == 2:
        now = datetime.today()
        while True:
            try:
                lang_level = int(input(f"{name}, what is your current level? "))
                if 1 <= lang_level <= 5:
                    break
                else:
                    print("Please enter a valid level number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please insert a valid digit between 1 and 5.")
        answers = "\n"
        if lang_level == 1:
            topic = "ITALIAN1"
            positive_feedback = 0
            with open("proj/data/level-1.txt") as file:
                lines = file.readlines()
                total_lines = len(lines)
            for line in range(0, len(lines) - 1, 2):
                answer = input(lines[line].rstrip() + " = ")
                correct_answer = lines[line+1].rstrip()
                if answer.rstrip() == correct_answer.rstrip():
                    feedback = "\033[1;95m\u2714\033[0m"
                    positive_feedback += 1
                else:
                    feedback = (f"{answer}\033[1;91m\u2718\033[0m should be {correct_answer}")
                solution = (f"{lines[line].rstrip()} = {answer}")
                answers += solution + feedback + "\n"
        elif lang_level == 2:
            topic = "ITALIAN2"
            positive_feedback = 0
            with open("proj/data/level-2.txt") as file:
                lines = file.readlines()
                total_lines = len(lines)
            for line in range(0, total_lines - 1, 2):
                answer = input(lines[line].rstrip() + " = ")
                correct_answer = lines[line+1].rstrip()
                if answer.rstrip() == correct_answer.rstrip():
                    feedback = "\033[1;95m\u2714\033[0m"
                    positive_feedback += 1
                else:
                    feedback = (f"{answer}\033[1;91m\u2718\033[0m should be {correct_answer}")
                solution = (f"{lines[line].rstrip()} = {answer}")
                answers += solution + feedback + "\n"
        elif lang_level == 3:
            topic = "ITALIAN3"
            positive_feedback = 0
            with open("proj/data/level-3.txt") as file:
                lines = file.readlines()
                total_lines = len(lines)
            for line in range(0, total_lines - 1, 2):
                answer = input(lines[line].rstrip() + " = ")
                correct_answer = lines[line+1].rstrip()
                if answer.rstrip() == correct_answer.rstrip():
                    feedback = "\033[1;95m\u2714\033[0m"
                    positive_feedback += 1
                else:
                    feedback = (f"{answer}\033[1;91m\u2718\033[0m should be {correct_answer}")
                solution = (f"{lines[line].rstrip()} = {answer}")
                answers += solution + feedback + "\n"
        elif lang_level == 4:
            topic = "ITALIAN4"
            positive_feedback = 0
            with open("proj/data/level-4.txt") as file:
                lines = file.readlines()
                total_lines = len(lines)
            for line in range(0, total_lines - 1, 2):
                answer = input(lines[line].rstrip() + " = ")
                correct_answer = lines[line+1].rstrip()
                if answer.rstrip() == correct_answer.rstrip():
                    feedback = "\033[1;95m\u2714\033[0m"
                    positive_feedback += 1
                else:
                    feedback = (f"{answer}\033[1;91m\u2718\033[0m should be {correct_answer}")
                solution = (f"{lines[line].rstrip()} = {answer}")
                answers += solution + feedback + "\n"
        elif lang_level == 5:
            topic = "ITALIAN5"
            positive_feedback = 0
            with open("proj/data/level-5.txt") as file:
                lines = file.readlines()
                total_lines = len(lines)
            for line in range(0, total_lines - 1, 2):
                answer = input(lines[line].rstrip() + " = ")
                correct_answer = lines[line+1].rstrip()
                if answer.rstrip() == correct_answer.rstrip():
                    feedback = "\033[1;95m\u2714\033[0m"
                    positive_feedback += 1
                else:
                    feedback = (f"{answer}\033[1;91m\u2718\033[0m should be {correct_answer}")
                solution = (f"{lines[line].rstrip()} = {answer}")
                answers += solution + feedback + "\n"
        print(answers + "\n")

        # Promotion logic based on score
        try:
            if ((positive_feedback / (total_lines/2)) * 100) > 70 and lang_level < 5:
                print(f"\nThe next time you use this program you should start with level {int(lang_level+1)}.")
            elif ((positive_feedback / (total_lines/2)) * 100) > 70 and lang_level == 5:
                print("Congratulations! You completed this course!")
        except ZeroDivisionError:
            continue

        # Log attempt with timestamp
        log =(f"\n{name} {last_name} - {topic} - {now.strftime('%B %d, %Y %H:%M:')}")
        if os.path.exists('proj/data/logs.txt'):
            with open ('proj/data/logs.txt', 'a') as f:
                f.write(log)
        else:
            with open('proj/data/logs.txt', 'w') as f:
                f.write(log)
        repeat_test = input("Are you finished (yes/no)? ")
        

# Timestamp and logboook confirmation
print("\nYour teacher can view details in logs.txt.")