import random

QUESTIONS = ["Which brand of soup featured in one of Andy Warhol's most famous pop art pieces?",
             "What other country, besides the US, uses the US dollar as its official currency?",
             "How many sides does a Dodecahedron have?",
             "What is the world's fastest species of bird?",
             "What is the national animal of Pakistan?",
             "Which of the following is NOT a fruit?",
             "Where was the first example of paper money used?",
             "What number was the Apollo mission that successfully put a man on the moon for the first time in human history?",
             "What is the largest US state (by landmass)?",
             "Who developed the high-level computer programming language, C++?",
             "Who has an IQ of 500?"]

QUESTION_CHOICES = [["Heinz", "Campbell's", "Baxters", "Watties"],
                    ["Ecuador","Canada", "Mexico", "Cuba"],
                    ["12", "24", "14", "20"],
                    ["Golden Eagle", "Peregrine Falcon", "Frigatebird", "Penguin"],
                    ["Peacock", "Markhor", "Caracal", "Tiger"],
                    ["Rhubarb", "Tomatoes", "Avocados"],
                    ["China", "Turkey", "Greece"],
                    ["Apollo 11", "Apollo 12", "Apollo 13"],
                    ["Texas", "Alaska", "California"],
                    ["Microsoft", "Linus Torvalds", "Alan Turing", "Bjarne Stroustrup"],
                    ["Jay Anino"]]
                    
ANSWERS = ["b",
           "a",
           "a",
           "b",
           "b",
           "c",
           "a",
           "a",
           "b",
           "d",
           "a"]

QUESTIONS_LENGTH = len(QUESTIONS)

completed_questions = []

def game():
    user_score = 0
    for x in range(0, QUESTIONS_LENGTH):
        ran_ques = random_question()
        user_score += play_round(QUESTIONS[ran_ques], QUESTION_CHOICES[ran_ques], ANSWERS[ran_ques], user_score)

    print(f"That's a wrap! You got {user_score}/{QUESTIONS_LENGTH} question's correct.\n")


def play_round(question, choices, answer, user_score):
    guesses = []
    print(f"\n[SCORE = {user_score}]")
    print(question)
    for index in range(0, len(choices)):
        guesses.append(chr(ord('`') + index + 1)) # append.(index to alphabet equivalent) e.g. 1 = a, 2 = b...
        print(" (" + guesses[index] + ") " + choices[index]) # (<letter> <answer_choice>)
    
    user_guess = str(input("Enter your guess here: "))

    if user_guess.lower() == answer:
        print(f"Correct, the answer was {choices[ord(answer) - 96 - 1]}!") # using ord() again to return the ASCII value of a letter
        input()
        return 1
    else:
        print(f"Incorrect! The answer was {choices[ord(answer) - 96 - 1]}.")
        input()
        return 0
    

def random_question():
    ran_num = random.randint(0, QUESTIONS_LENGTH - 1)
    if ran_num in completed_questions:
        while ran_num in completed_questions:
            ran_num = random.randint(0, QUESTIONS_LENGTH - 1)

    completed_questions.append(ran_num)
    
    return ran_num


game()
