from games import jog_dream, love_score

def main():
    print("Welcome to Rudy's Word Games!")
    print("Choose a game:")
    print("1. Jogging Dream")
    print("2. Love Score")
    choice = input("Enter the number of the game: ")

    if choice == "1":
        jog_dream.play()
    elif choice == "2":
        love_score.play()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
