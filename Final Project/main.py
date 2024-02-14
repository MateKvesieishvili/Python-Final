import time
from functions import play_game, display_leaderboard, update_leaderboard

def main_menu():
    print("\n\033[1;32;40mCountry Game Quiz!\033[0m")
    print("\033[1;32;40m1. Start Game\033[0m")
    print("\033[1;34;40m2. Leaderboard\033[0m")
    print("\033[1;31;40m3. Quit Game\033[0m")
    choice = input("Enter your choice: ")
    return choice

def loading_screen(secret=False): #!:)
    print("\033[1;33;40mLoading...\033[0m")
    time.sleep(2)
    if secret:
        print("\033[1;31;40mis this real?\033[0m")
    else:
        print("\033[1;32;40mLoading complete!\033[0m")

def main():
    leaderboard = [] 
    while True:
        choice = main_menu()
        if choice == "1":
            loading_screen()
            start_time = time.time()
            gamertag, score = play_game()
            end_time = time.time()  
            time_taken = round(end_time - start_time, 2)
            print("\n\033[1;32;40mTime taken:", time_taken, "seconds\033[0m")
            update_leaderboard(leaderboard, gamertag, score, time_taken)
        elif choice == "2":
            display_leaderboard(leaderboard)
        elif choice == "3":
            print("\n\033[1;31;40mThank you for playing!\033[0m")
            break
        else:
            print("\n\033[1;31;40mInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    main()
