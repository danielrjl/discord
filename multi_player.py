import nAnB_game

class Players:
    def __init__(self):
        self.__players = []
        self.__number_player = 0

    def add_player(self):
        self.__number_player += 1
        self.__players.append(self.__number_player)
        return self.__number_player
    
    def has_player(self, user_id):
        return user_id in self.__players
    
    def remove_player(self, user_id):
        if user_id in self.__players:
            self.__players.remove(user_id)
            return True
        return False

def parse_input(input_str, players):
    if input_str == "start":
        user_id = players.add_player()
        new_game = nAnB_game.start_new_game(user_id=user_id)
        print(f"Game started for player {user_id}. The secret number is: {new_game}")
    
    elif " " in input_str:
        input_str = input_str.split(" ")
        
        try:
            user_id = int(input_str[0])
        except:
            print("Invalid user ID.")
            return
        
        if not players.has_player(user_id):
            print("Player not found.")
            return
        
        if not nAnB_game.validate_input(input_str[1]):
            print("Invalid input. Please enter a 4-digit number.")
            return
        
        is_correct, result = nAnB_game.check_guess(user_id=user_id, guess=int(input_str[1]))
        if is_correct:
            players.remove_player(user_id)
            print(f"Player {user_id} guessed correctly! Result: {result}")
        else:
            print(f"Player {user_id} guessed: {result}")

def main():
    players = Players()

    while True:
        incoming_msg = input("> ")
        parse_input(incoming_msg, players)

if __name__ == "__main__":
    print("Welcome to the N An B game!")
    print("Type 'start' to start a new game.")
    print("Type '<user_id> <guess>' to make a guess.")
    print("For example: '1 1234' means user 1 guesses 1234.")
    main()