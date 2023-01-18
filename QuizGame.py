#-------------------------------------
def new_game():
    guesses =[]
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A, B, C, D):")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

    
#-------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong!")
        return 0
#-------------------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------------------")
    print("Results")
    print("-------------------------------------")
    
    print("Answer:" , end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses:" , end=" ")
    for i in guesses:
        print(i , end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your socre is :" + str(score)+ "%")
    
#-------------------------------------
def play_again():

    response = input("Do you wanna play this game again? (yes or no):")
    response = response.upper()

    if response == "YES" :
        return True
    else:
        return False
#-------------------------------------


questions = {"who created python?:" : "A",
            "what year was python created?:" : "B",
            "python is tributed to which comedy group?:" : "C",
            "Is the Earth round?: " : "A"
            }

options = [["A. Guido can Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh" , "C. Monty Python", "D. SNL"],
          ["A. True", "B. False", "C. sometimes", "D. What's Earth"]]

new_game()

while play_again():
    new_game()

print("Byeee")

