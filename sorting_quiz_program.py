#


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
        self.current_question = None
        self.selected_answer = tk.StringVar()
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        self.next_button = tk.Button(self.window, text="Next", command=self.next_question)
        self.next_button.pack()

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
            )
            radio_button.pack()

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
        self.result_label = tk.Label(self.window, text=f"You belong to {result_house}!")
        self.result_label.pack()

        self.display_turtle_result(result_house)

    def display_turtle_result(self, house_name):
        screen = Screen()
        screen.title("Sorting Hat Result")
        turtle = Turtle()
        turtle.hideturtle()
        turtle.speed(1)
        turtle.color("black")
        turtle.write(f"Welcome to {house_name}!")
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
            "What would you rather do?",
            {"Lead a team": "Gryffindor", "Plan a strategy": "Ravenclaw",
             "Work behind the scenes": "Hufflepuff", "Achieve greatness": "Slytherin"}
        ),
        Question(
            "How would your friends describe you?",
            {"Brave": "Gryffindor", "Clever": "Ravenclaw",
             "Loyal": "Hufflepuff", "Ambitious": "Slytherin"}
        ),
        Question(
            "What is your favorite subject?",
            {"Defense Against the Dark Arts": "Gryffindor", "Potions": "Slytherin",
             "Charms": "Ravenclaw", "Herbology": "Hufflepuff"}
        ),
        Question(
            "What would you do in a duel?",
            {"Stand your ground": "Gryffindor", "Outsmart your opponent": "Ravenclaw",
             "Help others to safety": "Hufflepuff", "Strike first": "Slytherin"}
        ),
    ]

    quiz = Quiz(questions, houses)

    SortingHatGUI(quiz)

    tk.mainloop()

main()