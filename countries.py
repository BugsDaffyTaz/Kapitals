import random
from country_data import country_capital

score = 0
questions_attempted = 0
correct_ans = 0
wrong_ans = 0


def get_random_country():
    country = random.choice(list(country_capital.keys()))
    capital = country_capital[country]
    return country, capital

def capitals_game():
    print("Let's guess the capitals of some countries")
    print("Try guessing the capital of each country, your score will be shown at the end.")
    print("Rules: " \
          "Type 'hint' for a clue \n"
          "Press '1' to know your final score or to exit the game."
            "+2 points for getting an answer right without hints" \
            "+1 point for getting an answer right with a hint" \
            "0 points for wrong answers")

    score = 0
    while True:
        global questions_attempted, correct_ans, wrong_ans
        questions_attempted +=1
        country, correct_capital = get_random_country()
        print(f"\nCountry: {country}")
        guess = input("Guess the capital: ").strip()

###########score/exit
        if guess.lower() == '1':
          print(f"\nYour final score: {score}")
          print(f"Questions attempted: {questions_attempted}")
          print(f"Correct Answers: {correct_ans}")
          print(f"Wrong Answers: {wrong_ans}")

          break

##################correct
        if guess.lower() == correct_capital.lower():
            score += 2
            correct_ans +=1
            print("That is the correct answer.")

        elif guess.lower() == "hint":
            print(f"Hint: Starts with {correct_capital[0]} and has {len(correct_capital)} letters")
            retry = input("Try again: ").strip()
            if retry.lower() == correct_capital.lower():
                score +=1
                correct_ans +=1
                print("Great going, that's correct!")
            else: 
                wrong_ans +=1
                print("That's the wrong answer.")
        else: 
            wrong_ans +=1
            print("That's the wrong answer.")
                
    



if __name__ == "__main__":
    capitals_game()


