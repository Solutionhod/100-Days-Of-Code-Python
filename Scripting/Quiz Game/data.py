import requests


class QuestionData:
    URL = {
        "General": {
            "easy":
            "https://opentdb.com/api.php?amount=20&category=9&difficulty=easy&type=boolean",
            "medium":
            "https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=boolean",
            "hard":
            "https://opentdb.com/api.php?amount=20&category=9&difficulty=hard&type=boolean"
        },
        "History": {
            "easy":
            "https://opentdb.com/api.php?amount=20&category=23&difficulty=easy&type=boolean",
            "medium":
            "https://opentdb.com/api.php?amount=20&category=23&difficulty=medium&type=boolean",
            "hard":
            "https://opentdb.com/api.php?amount=20&category=23&difficulty=hard&type=boolean"
        },
        "Animals": {
            "easy":
            "https://opentdb.com/api.php?amount=20&category=27&difficulty=easy&type=boolean",
            "medium":
            "https://opentdb.com/api.php?amount=20&category=27&difficulty=medium&type=boolean",
            "hard":
            "https://opentdb.com/api.php?amount=20&category=27&difficulty=hard&type=boolean"
        },
    }

    def __init__(self):
        self.question_data = []
        self.url = ""
        self.request_data()

    def options(self):
        category_options = [cat for cat in self.URL]
        difficulty_options = ["easy", "medium", "hard"]
        category = input(f"Select a category: {category_options}. ").title()
        difficulty = input(f"Select difficulty: {difficulty_options}. ").lower()
        if category in category_options and difficulty in difficulty_options:
            self.url = self.URL[category][difficulty]
            return self.url
        else:
            print("You selected a wrong option.")

    def request_data(self):
        self.options()
        if self.url == "":
            return None
        else:
            response = requests.get(self.url)
            response_data = response.json()
            for item in response_data["results"]:
                category = item["category"]
                difficulty = item["difficulty"]
                question = item["question"]
                answer = item["correct_answer"]
                data = {
                    "category": category,
                    "difficulty": difficulty,
                    "question": question,
                    "answer": answer
                }
                self.question_data.append(data)
