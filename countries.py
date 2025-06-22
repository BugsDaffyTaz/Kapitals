import random
import time
from country_data import country_capital

score = 0
questions_attempted = 0
correct_ans = 0
wrong_ans = 0


def get_random_country():
    country = random.choice(list(country_capital.keys()))
    capital = country_capital[country]
    return country, capital

def normalise_text(guess):
    return guess.lower().strip().replace("'", "").replace(".", "")

def capitals_game():
    print("Let's guess the capitals of some countries")
    print("Try guessing the capital of each country, your score will be shown at the end.")
    print("Rules: " \
          "Type 'hint' for a clue \n"
          "Press '1' to know your final score or to exit the game.\n"
            "+1 point for correct answers.\n" \
            "0 points for wrong answers.\n"
            "A timer would also be started in the beginning. \n")
    


    start_time = time.time()    
    while True:
        global questions_attempted, correct_ans, wrong_ans, score, total_time
        questions_attempted +=1
        country, correct_capital = get_random_country()
        print(f"\nCountry: {country}")
        guess = input("Guess the capital: ").strip()

###########score/exit
        if guess.lower() == '1':
          
          end_time = time.time()
          total_time = round(end_time - start_time, 2)
          
          print(f"\nYour final score: {score}/{questions_attempted}")
          print(f"\nTime taken: {total_time} seconds")
          print(f"\nQuestions attempted: {questions_attempted}")
          print(f"\nCorrect Answers: {correct_ans}")
          print(f"\nWrong Answers: {wrong_ans}")

          break 

##################correct

        possible_answers = [
                    normalise_text(part.split('(')[0])
                    for part in correct_capital.split(',')
                ]
        user_input = normalise_text(guess)

        if user_input in possible_answers:
            score += 1
            correct_ans +=1
            print("That is the correct answer.")

        elif guess.lower() == "hint":
            print(f"Hint: Starts with {correct_capital[0]} and has {len(correct_capital)} letters")

            retry = input("Try again: ").strip()

            if normalise_text(retry) in possible_answers:
                score +=1
                correct_ans +=1
                print("Great going, that's correct!")

            elif retry.lower() == "1":
                print(f"\nYour final score: {score}/{questions_attempted}")
                print(f"\nTime taken: ", {total_time})
                print(f"\nQuestions attempted: {questions_attempted}")
                print(f"\nCorrect Answers: {correct_ans}")
                print(f"\nWrong Answers: {wrong_ans}")
                break

            else: 
                wrong_ans +=1
                print(f"That's the wrong answer. The correct answer is {correct_capital.title()}.")
        else: 
            wrong_ans +=1
            print("That's the wrong answer.")
                




if __name__ == "__main__":
    capitals_game()


