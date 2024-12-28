from random import randint

def guess_game(player_name, random_no):
    print(f"{player_name}'s turn to guess!")
    chances = 0
    while True:
        try:
            guessed_no = int(input("Please guess a number between 1-10: "))
            chances += 1
            if guessed_no > random_no:
                print("Your guessed number is larger. Guess a smaller number.")
            elif guessed_no < random_no:
                print("Your guessed number is smaller. Guess a larger number.")
            else:
                print("Yeah!! You guessed it correctly!")
                break
        except ValueError:
            print("Please enter a valid number!")
    return chances


    

print("Welcome to the 2-player guessing game!")

random_no = randint(1, 10)
player1=input("Enter first player name:")
player1_chances = guess_game(player1, random_no)
random_no = randint(1, 10)
player2=input("Enter second player name:")
player2_chances = guess_game(player2, random_no)

print(f"{player1} took {player1_chances} chances.")
print(f"{player2} took {player2_chances} chances.")

if player1_chances < player2_chances:
    print(f"{player1} is the winner!")
elif player1_chances > player2_chances:
    print(f"{player2} is the winner!")
else:
    print("It's a tie!")
