# quiz_game

print("Do you want to play? Enter 'yes' to play and 'no' to quit the game:\n")
choice=input()


while True:
    if choice.lower()=="yes":
        print("Welcome! Let's start the game:")
        break
    elif choice.lower()=="no":
        quit()
    else:
        print("Please enter either 'yes' or 'no':")
        choice=input()


def quiz():
    if que.lower()==answer:
        return "correct!"
    else:
        return "incorrect!"


score_correct=0
score_incorrect=0

que=input("Question 1: Full form of CPU is?\n")
answer="central processing unit"
if quiz()=="correct!":
    print("correct!")
    score_correct+=1
else:
    print("incorrect!")
    score_incorrect+=1


que=input("Question 2: Full form of GUI is?\n")
answer="graphic user interface"
if quiz()=="correct!":
    print("correct!")
    score_correct+=1
else:
    print("incorrect!")
    score_incorrect+=1


que=input("Question 3: Full form of RAM is?\n")
answer="random access memory"
if quiz()=="correct!":
    print("correct!")
    score_correct+=1
else:
    print("incorrect!")
    score_incorrect+=1


print("""you have given {0} correct and {1} incorrect answers 
and you have given {2:2.2f} % correct answer."""
      .format(score_correct,score_incorrect,(score_correct/(score_correct+score_incorrect))*100))
