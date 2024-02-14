import random
import os

from data import countries_data

def display_score(score):
    print(f"Your score: {score}")

def display_correct_answer(country):
    print(f"The correct answer is: {country}")

def display_question(country, capital):
    print(f"What is the capital of {country}?")

def get_user_input():
    return input("Enter your guess: ")

def get_gamertag():
    return input("Enter your gamertag: ")

def check_user_input(user_input, country, capital):
    if user_input.lower() == capital.lower():
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def play_game():
    countries = list(countries_data.keys())
    random.shuffle(countries)

    gamertag = get_gamertag()
    score = 0
    max_attempts = 3
    attempts = 0

    for country in countries:
        capital = countries_data[country]
        display_question(country, capital)

        user_input = get_user_input()

        if check_user_input(user_input, country, capital):
            score += 1
        else:
            attempts += 1
            if attempts == max_attempts:
                print("You've reached the maximum number of attempts. Game over!")
                break
            display_correct_answer(country)

    display_score(score)
    return gamertag, score

def update_leaderboard(leaderboard, gamertag, score, time_taken):
    leaderboard.append({"gamertag": gamertag, "score": score, "time_taken": time_taken})

def display_leaderboard(leaderboard):
    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        print("\n\033[1;34;40m===== Leaderboard =====\033[0m")
        sorted_leaderboard = sorted(leaderboard, key=lambda x: (x["score"], -x["time_taken"]), reverse=True)
        for i, entry in enumerate(sorted_leaderboard[:10], 1):
            medal = ""
            if i == 1:
                medal = "🥇"
                color = "\033[1;33;40m"  # Golden
            elif i == 2:
                medal = "🥈"
                color = "\033[1;37;40m"  # Silver
            elif i == 3:
                medal = "🥉"
                color = "\033[0;33;40m"  # Copper
            else:
                color = "\033[1;37;40m"  # Regular color

            print(f"{medal}{color}{i}. Gamertag: {entry['gamertag']}, Score: {entry['score']}, Time Taken: {entry['time_taken']}s\033[0m")
