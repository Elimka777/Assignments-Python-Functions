#The aim of this assignment is to create a quiz game that asks questions and checks answers.

#Task 1: Develop a list of questions and answers.
#Task 2: Write a function that quizzes the user and takes their answers.
#Task 3: Score the quiz and give the user feedback on their performance.

questions = [
    'What is the freezing point of water in Celsius?',
    'Is George Washington the first President of the United States? (True/False)',
    'Who is the CEO of Tesla?',
    'What is 2 divided by 5?'
]

def quiz():
    global questions
    correct_answers = [0, True, 'Elon Musk', 0.4]
    answer_types = [int, bool, str, float]
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i] + ' ')
        try:
            if answer_types[i] == bool:
                converted_answer = user_answer.lower() in ['true', '1', 'yes', 'y']
            else:
                converted_answer = answer_types[i](user_answer)
                
            if converted_answer == correct_answers[i]:
                print("Correct")
                score += 1
            else:
                print('Wrong Answer')
        except ValueError:
            print('Wrong Answer')
    print(f"Your final score is {score}/{len(questions)}")

quiz()