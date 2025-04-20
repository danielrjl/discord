import random

active_games = {}


#choose the secret number
def start_new_game(user_id):
    secret_number_list = []
    for i in range(0, 4):
        n = random.randint(0,9)
        while n in secret_number_list:
            n = random.randint(0,9)
        secret_number_list.append(n)
    active_games[user_id] = secret_number_list
    print(secret_number_list)
    return secret_number_list



def is_correct_response(guess):
    if len(guess) != 4:
        return False
    for char in guess:
        if not char.isdigit():
            return False
    return True

#create the list of answered numbers
def check_guess(user_id, guess):

    if user_id not in active_games:
        return False, "no game"
    
    if is_correct_response == False:
        return "wrong response"
    
    answer_list = []
    for j in range(0, 4):
        answer_list.append(int(guess)/pow(10, 3-j))
        guess -= answer_list[j]*pow(10, 3-j)
    print(f"user {user_id} guessed {answer_list}")

    secret_number_list = active_games[user_id]
    a = 0
    b = 0
    for k in range(0, 4):
        if answer_list[k] == secret_number_list[k]:
            a += 1
        elif answer_list[k] in secret_number_list:
            b += 1
    
    if a == 4:
        del active_games[user_id]
        return True, f"{a}A{b}B"
    else:
        return False, f"{a}A{b}B"


#code for testing the game
def validate_input(guess):
    if len(guess) != 4:
        return False
    for char in guess:
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    _ = start_new_game(user_id=1)

    while True:
        guess = input("請輸入你的猜測：")
        if not validate_input(guess):
            print("請輸入四位數字")
            continue
        is_correct, check = check_guess(1, int(guess))
        print(f"[bot]: {check}")
        if is_correct:
            print("恭喜你！猜對了！")
            break