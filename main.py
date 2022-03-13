print("Welcome to QUIZ game")

print("Are you ready to start the game? (yes/no)")
playing = input()

if playing.lower() == 'yes':

    score = 0

    answer = input('What is the color of rose? ')
    if answer.lower() == 'red':
        print('Correct')
        score += 1
    else:
        print('Wrong answer!')

    answer = input('What is the color of leaf? ')
    if answer.lower() == 'green':
        print('Correct')
        score += 1
    else:
        print('Wrong answer!')

    answer = input('What is the color of banana? ')
    if answer.lower() == 'yellow':
        print('Correct')
        score += 1
    else:
        print('Wrong answer!')

    answer = input('What is the color of sky? ')
    if answer.lower() == 'sky blue':
        print('Correct')
        score += 1
    else:
        print('Wrong answer!')

    answer = input('What is the color of light? ')
    if answer.lower() == 'dont know':
        print('Correct')
        score += 1
    else:
        print('Wrong answer!')

    print("Your score is: "+ str(score) +".")
    print("Your accouracy is: "+ str((score / 5) * 100) +"%.")

    if score >= 3:
        print("Good game.")
    else:
        print("You have to try Hard.")

else:
    print("Be ready.")