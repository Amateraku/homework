def main():
    print(f"1) Make a code\n2) Decode a message\n3) Quit")
    primer = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    punctuations = (".", ",", "?", "!", ":", ";", "(", ")", " ")
    while True:
        user_choose = input("Enter your selection: ")
        if user_choose == "1":
            make_a_code(primer, punctuations)
        elif user_choose == "2":
            decode_a_message(primer, punctuations)
        elif user_choose == "3":
            quit_code()
        else:
            print("Enter correct selection.")


def make_a_code(primer, punctuations):
    message = input("Enter message: ")
    striped_message = [x for x in message]
    finished_message = []
    for letter in striped_message:
        if letter in punctuations:
            finished_message.append(letter)
            continue
        if letter in primer:
            if letter == primer[len(primer) - 1]:
                finished_message.append(primer[0])
            else:
                finished_message.append(primer[primer.index(letter) + 1])
        else:
            print(f"Symbol {letter} unsupported.")
    print("".join(finished_message))


def decode_a_message(primer, punctuations):
    message = input("Enter message: ")
    striped_message = [x for x in message]
    finished_message = []
    for letter in striped_message:
        if letter in punctuations:
            finished_message.append(letter)
            continue
        if letter in primer:
            if letter == primer[0]:
                finished_message.append(primer[len(primer) - 1])
            else:
                finished_message.append(primer[primer.index(letter) - 1])
        else:
            print(f"Symbol {letter} unsupported.")
    print("".join(finished_message))


def quit_code():
    quit()


if __name__ == '__main__':
    main()
