"""
PCEP Practice Quiz
-------------------
A beginner-friendly Python quiz app to help prepare for the
PCEP (Certified Entry-Level Python Programmer) exam.

Covers: print(), input(), type conversion, operators, conditions,
loops, range(), break, continue, lists, tuples, dictionaries,
string methods, functions, and exception handling.
"""

import random

# ---------------------------------------------------------------------------
# 1. QUESTION BANK
# ---------------------------------------------------------------------------
# Stored as a list of dictionaries. Each dictionary holds:
#   "question"    -> the question text (string)
#   "options"     -> a tuple of A/B/C/D answer choices
#   "answer"      -> the correct option letter (string)
#   "explanation" -> why that answer is correct (string)

QUESTIONS = [
    {
        "question": "Which function is used to display output on the screen?",
        "options": ("A. input()", "B. print()", "C. display()", "D. output()"),
        "answer": "B",
        "explanation": "print() sends text to standard output (the screen)."
    },
    {
        "question": "Which function reads text typed by the user?",
        "options": ("A. read()", "B. get()", "C. input()", "D. scan()"),
        "answer": "C",
        "explanation": "input() pauses the program and reads a line of user text."
    },
    {
        "question": "What data type does input() always return?",
        "options": ("A. int", "B. float", "C. bool", "D. str"),
        "answer": "D",
        "explanation": "input() always returns a string, even if the user types numbers."
    },
    {
        "question": "Which of these is an immutable ordered collection?",
        "options": ("A. list", "B. tuple", "C. dict", "D. set"),
        "answer": "B",
        "explanation": "Tuples are ordered but, unlike lists, cannot be changed after creation."
    },
    {
        "question": "Which keyword immediately exits the nearest enclosing loop?",
        "options": ("A. continue", "B. pass", "C. break", "D. exit"),
        "answer": "C",
        "explanation": "break stops the loop entirely and jumps to the code after it."
    },
    {
        "question": "Which keyword skips the rest of the current loop iteration only?",
        "options": ("A. continue", "B. break", "C. return", "D. skip"),
        "answer": "A",
        "explanation": "continue jumps back to the top of the loop for the next iteration."
    },
    {
        "question": "What does range(1, 5) produce?",
        "options": ("A. 1,2,3,4,5", "B. 1,2,3,4", "C. 0,1,2,3,4", "D. 2,3,4,5"),
        "answer": "B",
        "explanation": "range(1, 5) starts at 1 and stops before 5, giving 1, 2, 3, 4."
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ("A. list", "B. tuple", "C. dictionary", "D. string"),
        "answer": "C",
        "explanation": "Dictionaries map unique keys to values, e.g. {'name': 'Ada'}."
    },
    {
        "question": "What does 'hello'.upper() return?",
        "options": ("A. hello", "B. HELLO", "C. Hello", "D. Error"),
        "answer": "B",
        "explanation": ".upper() returns a new string with all letters capitalised."
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ("A. func", "B. define", "C. def", "D. function"),
        "answer": "C",
        "explanation": "Functions are defined with the def keyword, e.g. def greet():."
    },
]


# ---------------------------------------------------------------------------
# 2. HELPER FUNCTIONS
# ---------------------------------------------------------------------------

def welcome() -> None:
    """Print a welcome banner and instructions."""
    print("=" * 60)
    print("        WELCOME TO THE PCEP PRACTICE QUIZ")
    print("=" * 60)
    print("Instructions:")
    print(" - You will be asked a series of multiple-choice questions.")
    print(" - Answer with A, B, C, or D (upper or lower case is fine).")
    print(" - Type 'Q' at any time to quit the quiz early.")
    print(" - Your final score and feedback will be shown at the end.")
    print("-" * 60)


def ask_question(index: int, question_dict: dict) -> str:
    """
    Display a single question and its options.
    Returns the user's cleaned answer as a string ('A'-'D' or 'Q').
    """
    print(f"\nQuestion {index}: {question_dict['question']}")
    for option in question_dict["options"]:
        print(f"   {option}")

    # Loop until valid input is received, using continue to skip bad input.
    while True:
        raw_answer = input("Your answer (A/B/C/D, or Q to quit): ")
        cleaned = raw_answer.strip().upper()  # clean the input

        if cleaned == "Q":
            return cleaned
        if cleaned in ("A", "B", "C", "D"):
            return cleaned

        print("Invalid entry. Please type A, B, C, D, or Q.")
        continue  # go back and ask again


def check_answer(user_answer: str, question_dict: dict) -> bool:
    """Return True if the user's answer matches the correct answer."""
    return user_answer == question_dict["answer"]


def calculate_percentage(score: int, total: int) -> float:
    """Calculate the percentage score, guarding against division by zero."""
    try:
        percentage = (score / total) * 100
    except ZeroDivisionError:
        percentage = 0.0
    return percentage


def give_feedback(percentage: float) -> str:
    """Return a feedback message based on the final percentage."""
    if percentage >= 85:
        return "Excellent! You're ready for the PCEP exam."
    elif percentage >= 70:
        return "Good effort. Revise your weak areas and try again."
    else:
        return "Keep practising. Review the explanations and retake the quiz."


def run_quiz() -> None:
    """Run one full attempt of the quiz and print the final results."""
    questions = list(QUESTIONS)      # copy so shuffling doesn't affect original
    random.shuffle(questions)

    score = 0
    questions_answered = 0

    for i in range(len(questions)):
        question_number = i + 1
        current_question = questions[i]

        user_answer = ask_question(question_number, current_question)

        if user_answer == "Q":
            print("\nYou chose to end the quiz early.")
            break  # exit the loop early

        questions_answered += 1

        if check_answer(user_answer, current_question):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was "
                  f"{current_question['answer']}.")
            print(f"Explanation: {current_question['explanation']}")

    # ---- Results ----
    print("\n" + "=" * 60)
    print("QUIZ RESULTS")
    print("=" * 60)

    if questions_answered == 0:
        print("No questions were answered.")
        return

    percentage = calculate_percentage(score, questions_answered)
    print(f"Questions answered: {questions_answered}")
    print(f"Correct answers:    {score}")
    print(f"Score:              {percentage:.1f}%")
    print(f"Feedback:           {give_feedback(percentage)}")


def main_menu() -> None:
    """Display the main menu and handle the user's menu choice safely."""
    while True:
        print("\n" + "-" * 60)
        print("MAIN MENU")
        print("1. Start Quiz")
        print("2. Exit")
        choice_input = input("Enter your choice (1 or 2): ")

        try:
            choice = int(choice_input.strip())
        except ValueError:
            print("Invalid entry. Please enter a number (1 or 2).")
            continue

        if choice == 1:
            run_quiz()
            retake()
        elif choice == 2:
            print("Thanks for practising. Goodbye!")
            break
        else:
            print("Please choose a valid option: 1 or 2.")
            continue


def retake() -> None:
    """Ask the user if they want to retake the quiz."""
    while True:
        answer = input("\nWould you like to retake the quiz? (Y/N): ")
        cleaned = answer.strip().upper()
        if cleaned == "Y":
            run_quiz()
        elif cleaned == "N":
            break
        else:
            print("Please enter Y or N.")
            continue


# ---------------------------------------------------------------------------
# 3. PROGRAM ENTRY POINT
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    welcome()
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted by user. Goodbye!")
    except Exception as error:
        # Catch-all so an unexpected error doesn't crash ungracefully.
        print(f"\nAn unexpected error occurred: {error}")
