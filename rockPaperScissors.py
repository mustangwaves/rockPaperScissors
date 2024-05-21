import random

computerChoice = random.randint(1,3)

print(computerChoice)

if computerChoice == 1:
    computerChoice = 'Rock'
elif computerChoice == 2:
    computerChoice = 'Paper'
elif computerChoice == 3:
    computerChoice = 'Scissors'

playerChoice = input('Rock, Paper, or Scissors?')

if playerChoice == 'Rock' and computerChoice == 'Rock':
    print("The computer chose Rock. It's a draw!")
elif playerChoice == 'Rock' and computerChoice == 'Paper':
    print("The computer chose Paper. You lose.")
elif playerChoice == 'Rock' and computerChoice == 'Scissors':
    print("The computer chose Scissors. You win!")
elif playerChoice == 'Paper' and computerChoice == 'Rock':
    print("The computer chose Rock. You win!")
elif playerChoice == 'Paper' and computerChoice == 'Paper':
    print("The computer chose Paper. It's a draw!")
elif playerChoice == 'Paper' and computerChoice == 'Scissors':
    print("The computer chose Scissors. You lose.")
elif playerChoice == 'Scissors' and computerChoice == 'Rock':
    print("The computer chose Rock. You lose.")
elif playerChoice == 'Scissors' and computerChoice == 'Paper':
    print("The computer chose Paper. You win!")
elif playerChoice == 'Scissors' and computerChoice == 'Scissors':
    print("The computer chose Scissors. It's a draw!")
