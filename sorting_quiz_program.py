

import tkinter as tk
from turtle import Turtle, Screen

class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def get_house_for_answer(self, answer):
        return self.options.get(answer, None)


class House:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points=1):
        self.score += points


class Quiz:
    def __init__(self, questions, houses):
        self.questions = questions
        self.houses = houses
        self.current_question_index = 0

    def get_current_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        return None

    def calculate_result(self):
        def get_house_score(house):
            return house.score

        return max(self.houses.values(), key=get_house_score).name


class SortingHatGUI:
    def __init__(self, quiz):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("Sorting Hat Quiz")
        self.window.geometry("600x400")  # Fixed window size
        self.window.resizable(False, False)
        self.window.configure(bg="#f5f5dc")  # Light beige background

        self.current_question = None
        self.selected_answer = tk.StringVar()

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 16, "bold"),
            bg="#f5f5dc",
            fg="#333333",  # Dark gray text
            wraplength=550,
            justify="center"
        )
        self.question_label.pack(pady=20)
        self.options_frame = tk.Frame(self.window, bg="#f5f5dc")
        self.options_frame.pack(pady=10)
        self.next_button = tk.Button(
            self.window,
            text="Next",
            command=self.next_question,
            font=("Arial", 14),
            bg="#4CAF50",  # Green button
            fg="white",
            activebackground="#45a049",  # Darker green on click
            activeforeground="white",
            relief=tk.RAISED
        )
        self.next_button.pack(pady=20)

    def display_question(self):
        self.clear_options()
        self.current_question = self.quiz.get_current_question()
        if not self.current_question:
            self.show_result()
            return

        self.question_label.config(text=self.current_question.text)

        for option_text in self.current_question.options.keys():
            radio_button = tk.Radiobutton(
                self.options_frame,
                text=option_text,
                variable=self.selected_answer,
                value=option_text,
                font=("Arial", 12),
                bg="#f5f5dc",
                fg="#333333",
                activebackground="#f5f5dc",
                activeforeground="#000000",
                anchor="w",
                padx=10,
                indicatoron=True
            )
            radio_button.pack(anchor="w", pady=5)

    def clear_options(self):
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        self.selected_answer.set(None)

    def next_question(self):
        selected_option = self.selected_answer.get()
        if selected_option:
            house_name = self.current_question.get_house_for_answer(selected_option)
            if house_name:
                self.quiz.houses[house_name].add_score()

            self.quiz.current_question_index += 1
            self.display_question()

    def show_result(self):
        self.clear_options()
        self.question_label.pack_forget()
        self.next_button.pack_forget()

        result_house = self.quiz.calculate_result()
        self.result_label = tk.Label(
            self.window,
            text=f"You belong to {result_house}!",
            font=("Arial", 20, "bold"),
            bg="#f5f5dc",
            fg="#333333"
        )
        self.result_label.pack(pady=20)

        self.display_turtle_result(result_house)

    def display_turtle_result(self, house_name):
        screen = Screen()
        screen.setup(width=600, height=400)
        screen.title("Sorting Hat Result")
        screen.bgcolor("lightgray")

        turtle = Turtle()
        turtle.hideturtle()
        turtle.speed(3)

        colors = {
            "Gryffindor": "red",
            "Slytherin": "green",
            "Ravenclaw": "blue",
            "Hufflepuff": "yellow"
        }

        turtle.penup()
        turtle.goto(-290, 180)
        turtle.pendown()
        turtle.pensize(5)
        turtle.color(colors.get(house_name, "black"))
        for _ in range(2):
            turtle.forward(580)
            turtle.right(90)
            turtle.forward(360)
            turtle.right(90)

        turtle.penup()
        turtle.goto(0, 100)
        turtle.color(colors.get(house_name, "black"))
        turtle.write(f"Welcome to {house_name}!", align="center", font=("Arial", 24, "bold"))

        house_messages = {
            "Gryffindor": "Bravery, courage, and chivalry define you!",
            "Slytherin": "Ambition, cunning, and resourcefulness are your strengths!",
            "Ravenclaw": "Wit, wisdom, and learning are your greatest qualities!",
            "Hufflepuff": "Hard work, patience, and loyalty make you shine!"
        }
        message = house_messages.get(house_name, "You are unique and special!")

        max_width = 40
        y_position = 40
        current_line = ""
        for word in message.split():
            if len(current_line) + len(word) + 1 > max_width:
                turtle.goto(0, y_position)
                turtle.write(current_line, align="center", font=("Arial", 18, "italic"))
                y_position -= 30
                current_line = word
            else:
                current_line += (" " if current_line else "") + word

        if current_line:
            turtle.goto(0, y_position)
            turtle.write(current_line, align="center", font=("Arial", 18, "italic"))

        screen.mainloop()


def main():
    houses = {
        "Gryffindor": House("Gryffindor"),
        "Slytherin": House("Slytherin"),
        "Ravenclaw": House("Ravenclaw"),
        "Hufflepuff": House("Hufflepuff"),
    }

    questions = [
        Question(
            "What quality do you value most in yourself?",
            {"Courage": "Gryffindor", "Intelligence": "Ravenclaw",
             "Kindness": "Hufflepuff", "Ambition": "Slytherin"}
        ),
        Question(
            "What would you do if you found a lost magical artifact?",
            {"Turn it in to the authorities": "Ravenclaw", "Use it for a noble cause": "Gryffindor",
             "Keep it safe for others": "Hufflepuff", "Study its potential power": "Slytherin"}
        ),
        Question(
            "Which of these activities appeals to you most?",
            {"Exploring unknown places": "Gryffindor", "Solving a tricky puzzle": "Ravenclaw",
             "Gardening or nurturing others": "Hufflepuff", "Planning a bold strategy": "Slytherin"}
        ),
        Question(
            "How do you handle conflict?",
            {"Face it head-on": "Gryffindor", "Think your way around it": "Ravenclaw",
             "Seek a peaceful resolution": "Hufflepuff", "Find a way to gain the upper hand": "Slytherin"}
        ),
        Question(
            "What kind of pet would you want as a magical companion?",
            {"Phoenix": "Gryffindor", "Owl": "Ravenclaw",
             "Niffler": "Hufflepuff", "Snake": "Slytherin"}
        ),
        Question(
            "What kind of friend are you?",
            {"The protector": "Gryffindor", "The strategist": "Slytherin",
             "The supporter": "Hufflepuff", "The thinker": "Ravenclaw"}
        ),
        Question(
            "If you could master one magical skill, what would it be?",
            {"Dueling": "Gryffindor", "Transfiguration": "Ravenclaw",
             "Healing spells": "Hufflepuff", "Dark arts": "Slytherin"}
        ),
        Question(
            "What do you seek most in life?",
            {"Adventure": "Gryffindor", "Wisdom": "Ravenclaw",
             "Harmony": "Hufflepuff", "Power": "Slytherin"}
        ),
        Question(
            "What is your greatest fear?",
            {"Failure": "Slytherin", "Betrayal": "Hufflepuff",
             "Ignorance": "Ravenclaw", "Being seen as cowardly": "Gryffindor"}
        ),
        Question(
            "If you were at Hogwarts, which class would you look forward to the most?",
            {"Defense Against the Dark Arts": "Gryffindor", "Ancient Runes": "Ravenclaw",
             "Care of Magical Creatures": "Hufflepuff", "Potions": "Slytherin"}
        ),
    ]

    quiz = Quiz(questions, houses)

    SortingHatGUI(quiz)

    tk.mainloop()

main()