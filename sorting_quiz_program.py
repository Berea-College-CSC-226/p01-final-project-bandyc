
import tkinter as tk
from turtle import Turtle, Screen

class Question:
    def __init__(self, text, options):
        """
        Initializes a Question with text and options.

        :param text: The question text to be displayed
        :param options: A dictionary where keys are option texts and values are corresponding house names
        """
        self.text = text  # The question text
        self.options = options  # Dictionary mapping options to houses

    def get_house_for_answer(self, answer):
        """
        Returns the house corresponding to the selected answer.

        :param answer: The answer selected by the user
        :return: The house name corresponding to the answer, or None if the answer is invalid
        """
        return self.options.get(answer, None)  # Get the corresponding house for the selected answer


class House:
    def __init__(self, name):
        """
        Initializes a House with a name and score.

        :param name: The name of the house
        """
        self.name = name  # Name of the house
        self.score = 0  # Initial score for the house is 0

    def add_score(self, points=1):
        """
        Adds points to the house's score.

        :param points: The number of points to add (default is 1)
        :return: None
        """
        self.score += points  # Add points to the house's score


class Quiz:
    def __init__(self, questions, houses):
        """
        Initializes a Quiz with a list of questions and a dictionary of houses.

        :param questions: A list of Question objects
        :param houses: A dictionary of House objects with house names as keys
        """
        self.questions = questions  # List of questions in the quiz
        self.houses = houses  # Dictionary of houses (keyed by house names)
        self.current_question_index = 0  # Track the current question being displayed

    def get_current_question(self):
        """
        Returns the current question based on the current question index.

        :return: The current Question object or None if there are no more questions
        """
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]  # Return the current question
        return None  # No more questions left

    def calculate_result(self):
        """
        Calculates the result of the quiz by finding the house with the highest score.

        :return: The name of the house with the highest score
        """
        # Sort houses based on score and return the house with the highest score
        return max(self.houses.values(), key=lambda house: house.score).name


class SortingHatGUI:
    def __init__(self, quiz):
        """
        Initializes the GUI for the Sorting Hat Quiz.

        :param quiz: The Quiz object containing the questions and houses
        """
        self.quiz = quiz  # Store the quiz object
        self.window = tk.Tk()  # Initialize the main window
        self.window.title("Sorting Hat Quiz")  # Set window title
        self.window.geometry("600x400")  # Set fixed window size
        self.window.resizable(False, False)  # Prevent window resizing
        self.window.configure(bg="#f5f5dc")  # Set background color to light beige

        self.current_question = None  # Placeholder for the current question
        self.selected_answer = tk.StringVar()  # Variable to store the selected answer

        self.create_widgets()  # Create widgets (buttons, labels, etc.)
        self.display_question()  # Display the first question

    def create_widgets(self):
        """
        Creates the widgets for the quiz interface, including labels, buttons, and radio buttons.

        :return: None
        """
        # Create the label to display the question
        self.question_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 16, "bold"),
            bg="#f5f5dc",
            fg="#333333",  # Dark gray text
            wraplength=550,  # Allow text to wrap at 550 pixels width
            justify="center"  # Center the text
        )
        self.question_label.pack(pady=20)  # Place the question label on the window

        self.options_frame = tk.Frame(self.window, bg="#f5f5dc")  # Frame to contain the options
        self.options_frame.pack(pady=10)  # Place options frame below the question label

        # Create the "Next" button to move to the next question
        self.next_button = tk.Button(
            self.window,
            text="Next",
            command=self.next_question,  # Call next_question() when clicked
            font=("Arial", 14),
            bg="#4CAF50",  # Green button
            fg="white",
            activebackground="#45a049",  # Darker green on click
            activeforeground="white",
            relief=tk.RAISED  # Raised button effect
        )
        self.next_button.pack(pady=20)  # Place the button below the options frame

    def display_question(self):
        """
        Displays the current question and its options.

        :return: None
        """
        self.clear_options()  # Clear any previously displayed options
        self.current_question = self.quiz.get_current_question()  # Get the current question

        if not self.current_question:
            self.show_result()  # If no more questions, show the result
            return

        self.question_label.config(text=self.current_question.text)  # Display the question text

        # Iterate through the options of the current question and create radio buttons for each option
        for option_text in self.current_question.options.keys():
            radio_button = tk.Radiobutton(
                self.options_frame,
                text=option_text,
                variable=self.selected_answer,  # Bind selected answer to this radio button
                value=option_text,  # Set the radio button's value to the option text
                font=("Arial", 12),
                bg="#f5f5dc",  # Light beige background
                fg="#333333",  # Dark gray text
                activebackground="#f5f5dc",  # Background color when active
                activeforeground="#000000",  # Text color when active
                anchor="w",  # Align text to the left
                padx=10,  # Add padding for spacing
                indicatoron=True  # Make it a typical radio button
            )
            radio_button.pack(anchor="w", pady=5)  # Pack the radio button with padding

    def clear_options(self):
        """
        Clears the currently displayed options and resets the selected answer.

        :return: None
        """
        for widget in self.options_frame.winfo_children():  # Loop through all widgets in options frame
            widget.destroy()  # Destroy each widget (radio button)
        self.selected_answer.set(None)  # Reset the selected answer

    def next_question(self):
        """
        Handles the event when the user selects an answer and moves to the next question.

        :return: None
        """
        selected_option = self.selected_answer.get()  # Get the selected option
        if selected_option:
            house_name = self.current_question.get_house_for_answer(selected_option)  # Get the corresponding house
            if house_name:
                self.quiz.houses[house_name].add_score()  # Add points to the corresponding house

            self.quiz.current_question_index += 1  # Move to the next question
            self.display_question()  # Display the next question

    def show_result(self):
        """
        Displays the result of the quiz, showing the user's assigned house.

        :return: None
        """
        self.clear_options()  # Clear the options
        self.question_label.pack_forget()  # Hide the question label
        self.next_button.pack_forget()  # Hide the next button

        # Calculate and display the house the user belongs to
        result_house = self.quiz.calculate_result()
        self.result_label = tk.Label(
            self.window,
            text=f"You belong to {result_house}!",
            font=("Arial", 20, "bold"),
            bg="#f5f5dc",  # Light beige background
            fg="#333333"  # Dark gray text
        )
        self.result_label.pack(pady=20)  # Place the result label on the window

        self.display_turtle_result(result_house)  # Display the result using Turtle graphics

    def display_turtle_result(self, house_name):
        """
        Displays the Sorting Hat result using Turtle graphics.

        :param house_name: The name of the house the user belongs to
        :return: None
        """
        screen = Screen()
        screen.setup(width=600, height=400)  # Set screen size
        screen.title("Sorting Hat Result")  # Set window title
        screen.bgcolor("lightgray")  # Set background color for Turtle window

        turtle = Turtle()  # Create a new Turtle object
        turtle.hideturtle()  # Hide the default turtle shape
        turtle.speed(3)  # Set the speed of the turtle

        # Define colors for each house
        colors = {
            "Gryffindor": "red",
            "Slytherin": "green",
            "Ravenclaw": "blue",
            "Hufflepuff": "yellow"
        }

        turtle.penup()  # Lift the pen to move without drawing
        turtle.goto(-290, 180)  # Move the turtle to the starting position
        turtle.pendown()  # Lower the pen to start drawing
        turtle.pensize(5)  # Set pen size for drawing
        turtle.color(colors.get(house_name, "black"))  # Set color based on house name

        # Draw a rectangle around the screen
        for _ in range(2):
            turtle.forward(580)
            turtle.right(90)
            turtle.forward(360)
            turtle.right(90)

        turtle.penup()  # Lift the pen to stop drawing
        turtle.goto(0, 100)  # Move to the position where the house name is displayed
        turtle.color(colors.get(house_name, "black"))  # Set the color for the text
        turtle.write(f"Welcome to {house_name}!", align="center", font=("Arial", 24, "bold"))

        # Display a message related to the house
        house_messages = {
            "Gryffindor": "Bravery, courage, and chivalry define you!",
            "Slytherin": "Ambition, cunning, and resourcefulness are your strengths!",
            "Ravenclaw": "Wit, wisdom, and learning are your greatest qualities!",
            "Hufflepuff": "Hard work, patience, and loyalty make you shine!"
        }
        message = house_messages.get(house_name, "You are unique and special!")

        # Split the message and display it in lines that fit within the screen width
        max_width = 40
        y_position = 40
        current_line = ""
        for word in message.split():  # Split the message into words and add them line by line
            if len(current_line) + len(word) + 1 > max_width:  # If the line exceeds max width
                turtle.goto(0, y_position)  # Move turtle to the new line
                turtle.write(current_line, align="center", font=("Arial", 18, "italic"))  # Write the line
                y_position -= 30  # Move down for the next line
                current_line = word  # Start a new line
            else:
                current_line += (" " if current_line else "") + word  # Add word to current line

        if current_line:  # If there is any leftover text
            turtle.goto(0, y_position)
            turtle.write(current_line, align="center", font=("Arial", 18, "italic"))

        screen.mainloop()  # Start the Turtle graphics loop


def main():
    """
    Initializes and starts the Sorting Hat quiz application.

    :return: None
    """
    # Create the houses
    houses = {
        "Gryffindor": House("Gryffindor"),
        "Slytherin": House("Slytherin"),
        "Ravenclaw": House("Ravenclaw"),
        "Hufflepuff": House("Hufflepuff"),
    }

    # Create the questions for the quiz
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

    # Initialize the quiz with questions and houses
    quiz = Quiz(questions, houses)

    # Start the GUI application
    SortingHatGUI(quiz)

    tk.mainloop()  # Start the Tkinter main loop


# Run the main function to start the quiz
main()
