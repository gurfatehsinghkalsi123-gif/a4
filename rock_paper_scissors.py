import random

def get_ai_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(player, ai):
    if player == ai:
        return "tie"
    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        return "player"
    else:
        return "ai"

def main():
    print("🎮 Rock Paper Scissors (Terminal Game)")
    print("Type: rock, paper, or scissors")
    print("Type: quit to exit\n")

    player_score = 0
    ai_score = 0

    while True:
        player_choice = input("Your choice: ").lower()

        if player_choice == "quit":
            print("\nGame Over!")
            print(f"Final Score → You: {player_score} | AI: {ai_score}")
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Try again.\n")
            continue

        ai_choice = get_ai_choice()
        print(f"AI chose: {ai_choice}")

        winner = decide_winner(player_choice, ai_choice)

        if winner == "tie":
            print("🤝 It's a tie!\n")
        elif winner == "player":
            print("✅ You win this round!\n")
            player_score += 1
        else:
            print("❌ AI wins this round!\n")
            ai_score += 1

        print(f"Score → You: {player_score} | AI: {ai_score}\n")

if __name__ == "__main__":
    main()
