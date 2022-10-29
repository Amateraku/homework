import random


def main():
    colours = ["b", "r", "g", "y"]
    colours_to_find = ["", "", "", ""]
    for colour in range(0, 4):
        colours_to_find[colour] = colours[random.randint(0, 3)]
    print("Tip: enter 4 first letters of colours (blue, red, green, yellow)(X X X X)")
    guessing(colours_to_find)


def guessing(colours_to_find):
    while True:
        number_of_positions = 0
        number_of_right_colours = 0
        player_guess = input("Guess colours: ")
        list_guess_colours = player_guess.split(" ")
        for colour in range(0, 4):
            if colours_to_find[colour] == list_guess_colours[colour]:
                number_of_right_colours += 1
            else:
                for colour2 in range(0, 4):
                    if list_guess_colours[colour] == colours_to_find[colour2]:
                        number_of_positions += 1
                        break
        if number_of_right_colours == 4:
            print("You guess!!!")
            break
        print(f"Rights colours: {number_of_right_colours}")
        print(f"False positions: {number_of_positions}")


if __name__ == '__main__':
    main()
