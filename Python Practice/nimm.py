"""
File: nimm.py
-------------------------
The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""
ONE = 1
TWO = 2
TOTAL = 20


def main():

    print("There are" + " " + str(TOTAL) + " stones left")
    while True:
        alternate_players()
        get_stones()
        one_two_stones()


def alternate_players():
    """Keep track of of whose turn it is between 2 players
                   Tell the user whose turn it is. Each time someone picks
                    up stones, change the player number."""
    player = 2
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

    return player


def get_stones():

    count_stone = int(
        input("Player " + str(alternate_players().player) + " would you like to remove" + " " + str(
            ONE) + " " + "or" + " " + str(TWO) + " " + "stones? "))
    return count_stone


def one_two_stones():
    count = 20
    # ensures only one or two  stones are removed
    if get_stones().count_stone == ONE or get_stones().count_stone:
        count = count - get_stones().count_stone

        print("There are" + " " + str(count) + " stones left")

    else:
        too_many_stones()

    if count <= 1:
        if alternate_players().player % 2 == 0:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")


def too_many_stones():
    while get_stones().count_stone != ONE or get_stones().count_stone != TWO:
        count = int(input("Please enter 1 or 2: "))
        new_count = count - one_two_stones().count
    one_two_stones()


# This provided line is required at the end of a Python file
# to call the main() function.


if __name__ == '__main__':
    main()
