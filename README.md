# PCEP Practice Quiz 🐍

A beginner-friendly, terminal-based Python quiz app that helps learners
prepare for the **PCEP – Certified Entry-Level Python Programmer** exam.

Built as a small project to practise core Python fundamentals: functions,
dictionaries, lists, tuples, loops, conditions, scoring, and exception
handling.

## ✨ Features

- Welcome message and clear instructions
- 10 multiple-choice questions covering PCEP-style topics
- Questions shuffle on every run for variety
- Answers cleaned with `.strip().upper()` so input is forgiving
- Instant right/wrong feedback with an explanation for each question
- Automatic scoring and percentage calculation
- Final feedback based on performance:
  | Score | Feedback |
  |---|---|
  | 85% and above | Excellent, ready for the exam |
  | 70–84% | Good, revise weak areas |
  | Below 70% | Keep practising |
- Quit early at any time by typing `Q`
- Invalid menu/answer input is caught and re-prompted, not crashed
- Retake the quiz as many times as you like

## 🧠 Python Skills Demonstrated

| Topic | How it's used |
|---|---|
| `print()` | Display questions and feedback |
| `input()` | Collect answers |
| `int()`, `float()`, `str()` | Convert menu choices and scores |
| Operators | Calculate percentage score |
| Conditions | Check correct and wrong answers |
| Loops | Ask multiple questions |
| `range()` | Number the questions |
| `break` | Exit quiz early |
| `continue` | Skip invalid input |
| Lists | Store multiple questions |
| Tuples | Store answer options |
| Dictionaries | Store question, options, answer, explanation |
| Strings | Clean answers with `.strip().upper()` |
| Functions | Run quiz, check answer, calculate result |
| Exceptions | Handle invalid menu choice and missing keys |

## 📁 Project Structure

```
.
├── pcep_quiz.py        # Standalone script version — run from the terminal
├── pcep_quiz.ipynb     # Jupyter notebook version — run cell by cell
└── README.md
```

## 🚀 Getting Started

### Requirements

- Python 3.8+
- No external dependencies (standard library only)

### Option 1: Run the script

```bash
git clone https://github.com/<your-username>/pcep-practice-quiz.git
cd pcep-practice-quiz
python3 pcep_quiz.py
```

### Option 2: Run the notebook

```bash
pip install notebook
jupyter notebook pcep_quiz.ipynb
```

Run each cell from top to bottom, then run the final **"Launch the Quiz"**
cell and answer in the input prompt that appears.

## 🎮 How to Play

1. Choose **1** from the main menu to start the quiz.
2. For each question, type **A**, **B**, **C**, or **D** and press Enter.
3. Type **Q** at any time to end the quiz early and see your results so far.
4. After the quiz, view your score, percentage, and feedback.
5. Choose to retake the quiz or exit from the menu.

## 🛣️ Possible Extensions

- Load questions from an external JSON/CSV file
- Add a timer per question
- Track high scores across sessions in a file
- Build a simple GUI (Tkinter) or web version (Flask/Streamlit)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built as a hands-on project to practise and showcase core Python skills
relevant to the PCEP entry-level certification.*
