from guess_number import GuessNumber

print("Please input your name")

user = input()

new_game = GuessNumber(username=user)

print(f'welcome {new_game.username}.I am thinking of a number between 1 and 20.')
print(f"----------------------------------------------------------------------------")
print("Please guess the number")

condition = True

counter = 0

while int(condition):
    num = input()
    counter += 1
    # check whether input value is integer
    try:
        num = int(num)
    except ValueError:
        print("Kindly enter a number of type int")
        break
    # check input value lies between one and twenty
    if num < 1 or num > 20:
        print(f'{num} is not a number between 1 and 20.Kindly guess a number that lies between 1 and 20')

    # when the guess is right
    if new_game.check_number(int(num)) is None:
        condition = False
        print(f'Congrats {new_game.username}, you got it right!!!')
    # check when number of guesses is five
    elif counter == 5:
        print(f"your chance is over,the number i was thinking for is {new_game.random_number}")
        break

    else:
        print(new_game.check_number(int(num)))
