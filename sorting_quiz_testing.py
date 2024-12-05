

import unittest
from sorting_quiz_program import Question, House, Quiz

class TestSortingHatQuiz(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        self.houses = {
            "Gryffindor": House("Gryffindor"),
            "Slytherin": House("Slytherin"),
            "Ravenclaw": House("Ravenclaw"),
            "Hufflepuff": House("Hufflepuff"),
        }

        self.questions = [
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
        ]

        self.quiz = Quiz(self.questions, self.houses)

    def test_house_initial_scores(self):
        """Test that all houses start with a score of 0."""
        for house in self.houses.values():
            self.assertEqual(house.score, 0)

    def test_add_score(self):
        """Test that scores are incremented correctly."""
        self.houses["Gryffindor"].add_score()
        self.assertEqual(self.houses["Gryffindor"].score, 1)
        self.houses["Gryffindor"].add_score(2)
        self.assertEqual(self.houses["Gryffindor"].score, 3)

    def test_get_current_question(self):
        """Test retrieving current question."""
        question = self.quiz.get_current_question()
        self.assertEqual(question.text, "What would you rather do?")

    def test_question_answer_mapping(self):
        """Test question answer mappings."""
        question = self.questions[0]
        self.assertEqual(question.get_house_for_answer("Lead a team"), "Gryffindor")
        self.assertIsNone(question.get_house_for_answer("Invalid answer"))

    def test_quiz_progression(self):
        """Test quiz progression and scoring."""
        question = self.quiz.get_current_question()
        answer = "Lead a team"  # Answer for Gryffindor
        house_name = question.get_house_for_answer(answer)
        self.houses[house_name].add_score()

        # Move to next question
        self.quiz.current_question_index += 1
        next_question = self.quiz.get_current_question()
        self.assertEqual(next_question.text, "How would your friends describe you?")
        self.assertEqual(self.houses["Gryffindor"].score, 1)

    def test_calculate_result(self):
        """Test result calculation."""
        self.houses["Gryffindor"].add_score(2)
        self.houses["Ravenclaw"].add_score(1)
        result = self.quiz.calculate_result()
        self.assertEqual(result, "Gryffindor")

if __name__ == "__main__":
    unittest.main()
