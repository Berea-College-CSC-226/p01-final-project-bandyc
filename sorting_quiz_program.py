


import tkinter as tk
import turtle

class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options

    def get_house_for_answer(self, answer):
        pass


class House:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points=1):
        pass


class Quiz:
    def __init__(self, questions, houses):
        self.questions = questions
        self.houses = houses
        self.current_question_index = 0

    def get_current_question(self):
        pass

    def calculate_result(self):
        pass


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