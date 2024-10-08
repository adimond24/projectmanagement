# get a random dictionary from the array data
# compare the first random with a second random
# compare number of followers
# make a function that picks A or B for higher amount of followers
# If guess correct then add point and print you're right
# when the random are picked need to display the different aspects of the one it picked
# if correct then keep going until failed
#display you fail if you lose
#display art
#get random accounts to show up
#format the account data 
# user for a guess
#check user guess
# use if statement to check if user is correct.
# give user feedback on their guess.
#Make game repeatable and
#move the position B to position A
#keep scoring

from game_data import data
import random

score = 0
game_should_continue = True
account_b = random.choice(data)

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
        

while game_should_continue: 
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}. ")
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"you're right, current score: {score}")
    else:
        print(f"sorry, thats wrong final score: {score}")
        game_should_continue = False


