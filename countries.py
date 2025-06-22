
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
    print("Rules: \n" \
          "1. Type 'hint' for a clue \n"
          "2. Press '1' to know your final score or to exit the game.\n"
          "3. +1 point for correct answers.\n" 
          "4. 0 points for wrong answers.\n"
          "5. A timer would also be started in the beginning. \n")
    


    start_time = time.time()    
    while True:
        global questions_attempted, correct_ans, wrong_ans, score
        questions_attempted +=1
        country, correct_capital = get_random_country()
        print(f"\nCountry: {country}")
        guess = input("Guess the capital: ").strip()

###########  score/exit  ##############
        
        if guess.lower() == '1':
          
          end_time = time.time()
          total_time = round(end_time - start_time, 2)
          print(f"The correct answer is {correct_capital.title()}.")  
          print(f"\n🏁 Game Over!")
          print(f"\n📈 Your final score: {score}/{questions_attempted}")
          print(f"\n⏱️ Time taken: {total_time} seconds")
          print(f"\n🎯 Questions attempted: {questions_attempted}")
          print(f"\n✅ Correct Answers: {correct_ans}")
          print(f"\n❌ Wrong Answers: {wrong_ans}")

          break 

############  correct or not ###########

        possible_answers = [
                    normalise_text(part.split('(')[0])
                    for part in correct_capital.split(',')
                ]
        user_input = normalise_text(guess)

        if user_input in possible_answers:
            score += 1
            correct_ans +=1
            print("✅ That is the correct answer.")

        elif guess.lower() == "hint":
            clean_hint = correct_capital.split(',')[0].split('(')[0].strip()
            print(f"Hint: Starts with {clean_hint[0]} and has {len(clean_hint)} letters")


            retry = input("Try again: ").strip()

            if normalise_text(retry) in possible_answers:
                score +=1
                correct_ans +=1
                print("✅ Great going, that's correct!")

            elif retry.lower() == "1":
                end_time = time.time()
                total_time = round(end_time - start_time, 2)

                print(f"\n🏁 Game Over!")
                print(f"\n📈 Your final score: {score}/{questions_attempted}")
                print(f"\n⏱️ Time taken: {total_time} seconds")
                print(f"\n🎯 Questions attempted: {questions_attempted}")
                print(f"\n✅ Correct Answers: {correct_ans}")
                print(f"\n❌ Wrong Answers: {wrong_ans}")

                break

            else: 
                wrong_ans +=1
                print(f"❌ That's the wrong answer. The correct answer is {correct_capital.title()}.")
        else: 
            wrong_ans +=1
            print(f"❌ That's the wrong answer. The correct answer is {correct_capital.title()}.")
                

##### file output run ######


if __name__ == "__main__":
    capitals_game()


## end ##
