# Warsztat: Salon gier (*)

import random

legal_dice = [3, 4, 6, 8, 10, 12, 20, 100]

def human_roll():

    while True:
        dice1 = input("Pick your 1st dice. ")
        dice1 = int(dice1[1:])
        
        if dice1 in legal_dice:
            break
        else:
            print("Pick a legal dice.")

    while True:
        dice2 = input("Pick your 2nd dice. ")
        dice2 = int(dice2[1:])
        
        if dice2 in legal_dice:
            break
        else:
            print("Pick a legal dice.")

    result = random.randint(1, dice1) + random.randint(1, dice2)
    return result

def computer_roll():
    random.shuffle(legal_dice)
    dice1 = legal_dice[0]
    random.shuffle(legal_dice)
    dice2 = legal_dice[0]
    result = random.randint(1, dice1) + random.randint(1, dice2)
    return result


def play_round(score, total):
    if score == 7:
        new_total = int(total / 7)
    elif score == 11:
        new_total = total * 11
    else:
        new_total = total + score
    return new_total

def play_2001():

    player_total = 0
    computer_total = 0
    turn = 0

    while player_total < 2001 and computer_total < 2001:
        turn += 1
        if turn == 1:
            player_total = human_roll()
            computer_total = computer_roll()
            print(f"Round: {turn}")
            print(f"You rolled: {player_total}")
            print(f"Computer rolled: {computer_total}")
        else:
            player_round_score = human_roll()
            computer_round_score = computer_roll()
            player_total = play_round(player_round_score, player_total)
            computer_total = play_round(computer_round_score, computer_total)
            print(f"Round: {turn}")
            print(f"You rolled: {player_roll}, your total score is: {player_total}")
            print(f"Computer rolled: {computer_roll}, computer's total score is: {computer_total}")
        
    if player_total < computer_total:
        print("You lost.")
    elif player_total > computer_total:
        print("You win.")
    elif player_total == computer_total:
        print("It's a draw.")

play_2001()