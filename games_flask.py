# Warsztat: Salon gier (*)

import random 
from flask import Flask, request

app = Flask(__name__)

legal_dice = [3, 4, 6, 8, 10, 12, 20, 100]

def human_roll(dice1, dice2):
    result = random.randint(1, int(dice1[1:])) + random.randint(1, int(dice2[1:]))
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


@app.route("/game", methods = ["GET", "POST"])
def play_2001():

    if request.method == "GET":
        return f"""
        <html>
            <body>
                <form action="" method="POST">
                    <p> Let's play a game! </p>
                    <p> Roll the dice </p>
                    <select id="dice1" name="dice1" >
                        <option value="d3">d3</option>
                        <option value="d4">d4</option>
                        <option value="d4">d4</option>
                        <option value="d8">d8</option>
                    </select>
                    <select id="dice2" name="dice2" >
                        <option value="d3">d3</option>
                        <option value="d4">d4</option>
                        <option value="d4">d4</option>
                        <option value="d8">d8</option>
                    </select>
                    <input type="submit" name="Roll!" >
                    <input type"numeric" name="player_total" value="0">
                    <input type"numeric" name="computer_total" value="0">
                    <input type"numeric" name="round" value="0">
                </form>
            </body>
        </html>
        """
    if request.method == "POST":

        round = int(request.form.get("round"))
        round += 1
        player_total = int(request.form.get("player_total"))
        computer_total = int(request.form.get("computer_total"))
        dice1 = request.form.get("dice1")
        dice2 = request.form.get("dice2")


        if round == 1:
            player_total = human_roll(dice1, dice2)
            computer_total = computer_roll()
            
        else:
            player_round_score = human_roll(dice1, dice2)
            computer_round_score = computer_roll()
            player_total = play_round(player_round_score, player_total)
            computer_total = play_round(computer_round_score, computer_total)

        return f"""
        <html>
            <body>
                <form action="" method="POST">
                    <p> Let's play a game! </p>
                    <p> Roll the dice </p>
                    <select id="dice1" name="dice1" >
                        <option value="d3">d3</option>
                        <option value="d4">d4</option>
                        <option value="d4">d4</option>
                        <option value="d8" selected>d8</option>
                    </select>
                    <select id="dice2" name="dice2" >
                        <option value="d3">d3</option>
                        <option value="d4">d4</option>
                        <option value="d4">d4</option>
                        <option value="d8" selected>d8</option>
                    </select>
                    <input type="submit" name="Roll!" >
                    <input type"numeric" name="player_total" value="{player_total}">
                    <input type"numeric" name="computer_total" value="{computer_total}">
                    <input type"numeric" name="round" value="{round}">
                </form>
            </body>
        </html>
        """

if __name__ == "__main__":
    app.run(debug=True)