import random

file_path = '/home/aaronluebbert/Personal Projects/External Project Files/balance.txt'

try:
    with open(file_path, 'r') as balanceFile:
        balance_str = balanceFile.read().strip()
        print("Your balance is:", repr(balance_str))  # Print the contents for debugging
        balance = int(balance_str) if balance_str else 0  # Set default balance to 0 if file is empty
except FileNotFoundError:
    balance = 0  # Set default balance to 0 if file doesn't exist

def write_balance(balance):
    with open(file_path, 'w') as balanceFile:
        balanceFile.write(str(balance))

balance = int(balance)

play_again = True
#Loop to allow player to play multiple times
while play_again == True:
    
# gets computers choice and converts it to rock, paper, or scissors

    computerChoice = random.choice(['Rock','Paper','Scissors'])

    bet = int(input('How much would you like to bet?'))
    playerChoice = input('Rock, Paper, or Scissors?')

# prints out results of the game

    if playerChoice == computerChoice:
        print(f"the computer chose {computerChoice}. It's a draw!")
    elif (playerChoice == 'Rock' and computerChoice == 'Scissors') or \
        (playerChoice == 'Paper' and computerChoice == 'Rock') or \
        (playerChoice == 'Scissors' and computerChoice == 'Paper'):
            print(f"The computer chose {computerChoice}. You win!")
            balance += bet
    else:
        print(f"The computer chose {computerChoice}. You lose!")
        balance -= bet

    print(f'Your new balance is: {balance}')
    write_balance(balance)

    playAgain = input('Play again? (y/n)')
    if playAgain == 'n':
        play_again = False
