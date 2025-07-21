import random


images = {
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    "paper": '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
    "scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}


input_map = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def print_result(user, computer, winner):
    print(f"\n🧍 You chose: {user.upper()}")
    print(images[user])
    
    print(f"💻 Computer chose: {computer.upper()}")
    print(images[computer])

    if winner == 'tie':
        print("🤝 It's a tie!")
    elif winner == 'user':
        print("🎉 You win! 👑")
    else:
        print("😞 Computer wins! 👑")

def main():
    user_score = 0
    computer_score = 0
    print("=== Rock, Paper, Scissors Game ===")
    print("Enter your move: [r]ock, [p]aper, [s]cissors")

    while True:
        user_input = input("Your move (r/p/s): ").lower().strip()
        if user_input not in input_map:
            print("❌ Invalid input. Use 'r', 'p', or 's'.")
            continue

        user_choice = input_map[user_input]
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\n🏆 Score: You {user_score} - {computer_score} Computer")

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("\n👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
