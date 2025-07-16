import tkinter as tk

# Quiz Data
quiz_data = {
    "easy": [
        {"q": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": 1},
        {"q": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": 2},
        {"q": "Color of the sky?", "options": ["Green", "Blue", "Red", "Yellow"], "answer": 1},
        {"q": "Which is an even number?", "options": ["1", "3", "4", "5"], "answer": 2},
        {"q": "Which animal barks?", "options": ["Cat", "Dog", "Cow", "Horse"], "answer": 1},
    ],
    "medium": [
        {"q": "5 * 3 = ?", "options": ["15", "25", "20", "10"], "answer": 0},
        {"q": "Planet closest to sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": 2},
        {"q": "Opposite of cold?", "options": ["Hot", "Cool", "Warm", "Chill"], "answer": 0},
        {"q": "What is H2O?", "options": ["Oxygen", "Water", "Hydrogen", "Air"], "answer": 1},
        {"q": "Square root of 36?", "options": ["5", "6", "7", "4"], "answer": 1},
    ],
    "hard": [
        {"q": "Prime number among these?", "options": ["4", "6", "9", "7"], "answer": 3},
        {"q": "Which is a mammal?", "options": ["Shark", "Whale", "Frog", "Crocodile"], "answer": 1},
        {"q": "What is 12 / 4?", "options": ["3", "2", "4", "6"], "answer": 0},
        {"q": "Which continent is Pakistan in?", "options": ["Asia", "Africa", "Europe", "America"], "answer": 0},
        {"q": "Binary of 2?", "options": ["10", "01", "11", "00"], "answer": 0},
    ]
}

# Initial states
current_question = 0
selected_level = ""
score = 0

# Functions
def go_to_menu():
    welcome_frame.pack_forget()
    menu_frame.pack()

def back_to_welcome():
    menu_frame.pack_forget()
    welcome_frame.pack()

def back_to_menu():
    quiz_frame.pack_forget()
    menu_frame.pack()

def start_quiz(level):
    global selected_level, current_question, score
    selected_level = level
    current_question = 0
    score = 0
    menu_frame.pack_forget()
    quiz_frame.pack()
    load_question()

def load_question():
    global current_question
    question_data = quiz_data[selected_level][current_question]
    question_label.config(text=f"Q{current_question + 1}: {question_data['q']}")
    for i in range(4):
        options[i].config(text=question_data["options"][i])
    selected_option.set(-1)

def next_question():
    global current_question, score
    selected = selected_option.get()
    if selected == quiz_data[selected_level][current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question < 5:
        load_question()
    else:
        quiz_frame.pack_forget()
        result_label.config(text=f"You scored {score} out of 5")
        result_frame.pack()

def play_again():
    result_frame.pack_forget()
    menu_frame.pack()

# GUI window setup
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x450")
root.config(bg="#e6f2ff")

# Styles
btn_style = {"font": ("Arial", 12), "bg": "#007acc", "fg": "white", "width": 20, "bd": 0, "activebackground": "#005f99"}
label_style = {"bg": "#e6f2ff", "font": ("Arial", 14)}
header_style = {"bg": "#e6f2ff", "font": ("Arial", 16, "bold")}

# Welcome Page
welcome_frame = tk.Frame(root, bg="#e6f2ff")
tk.Label(welcome_frame, text="Welcome to the Quiz App", **header_style).pack(pady=20)
tk.Button(welcome_frame, text="Login", state="disabled", **btn_style).pack(pady=5)
tk.Button(welcome_frame, text="Signup", state="disabled", **btn_style).pack(pady=5)
tk.Button(welcome_frame, text="Play as Guest", command=go_to_menu, **btn_style).pack(pady=10)
welcome_frame.pack()

# Menu Page
menu_frame = tk.Frame(root, bg="#e6f2ff")
tk.Label(menu_frame, text="Select Difficulty Level", **label_style).pack(pady=15)
tk.Button(menu_frame, text="Easy", command=lambda: start_quiz("easy"), **btn_style).pack(pady=5)
tk.Button(menu_frame, text="Medium", command=lambda: start_quiz("medium"), **btn_style).pack(pady=5)
tk.Button(menu_frame, text="Hard", command=lambda: start_quiz("hard"), **btn_style).pack(pady=5)
tk.Button(menu_frame, text="Back", command=back_to_welcome, **btn_style).pack(pady=15)

# Quiz Page
quiz_frame = tk.Frame(root, bg="#e6f2ff")
question_label = tk.Label(quiz_frame, text="Question", **label_style, wraplength=450, justify="left")
question_label.pack(pady=20)

selected_option = tk.IntVar()
options = []
for i in range(4):
    rb = tk.Radiobutton(quiz_frame, text="", variable=selected_option, value=i, font=("Arial", 12),
                        bg="#e6f2ff", anchor="w", padx=20)
    rb.pack(fill='x', padx=40, pady=2)
    options.append(rb)

tk.Button(quiz_frame, text="Next", command=next_question, **btn_style).pack(pady=10)
tk.Button(quiz_frame, text="Back", command=back_to_menu, **btn_style).pack()

# Result Page
result_frame = tk.Frame(root, bg="#e6f2ff")
result_label = tk.Label(result_frame, text="", font=("Arial", 16), bg="#e6f2ff")
result_label.pack(pady=20)
tk.Button(result_frame, text="Play Again", command=play_again, **btn_style).pack(pady=10)

# Start GUI
root.mainloop()
