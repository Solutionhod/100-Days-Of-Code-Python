from data import QuestionData
from question_model import Question
from quiz_brain import QuizBrain


def quiz_game():
    game_on = True
    while game_on:
        print(Question.LOGO)
        data = QuestionData()
        question_bank = []
        for question in data.question_data:
            text = question["question"]
            answer = question["answer"]
            new_question = Question(text, answer)
            question_bank.append(new_question)
        if question_bank != []:
            quiz = QuizBrain(question_bank)
            while quiz.still_have_questions():
                question = quiz.next_question()
            print("You have completed the quiz.")
            print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}.")
        if input("Do you want to play again?: Type 'yes' to continue or 'no' to quit. ").lower() == "yes":
            game_on
        else:
            print("Goodbye...")
            game_on = False


quiz_game()
