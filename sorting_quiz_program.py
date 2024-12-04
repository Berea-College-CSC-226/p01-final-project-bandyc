#


import tkinter as tk
import turtle

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
        pass

    def display_question(self):
        pass

    def next_question(self):
        pass

    def show_result(self):
        pass

    def display_turtle_result(self, house_name):
        pass


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

main()