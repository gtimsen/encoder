def encode(password):
    array_input = [int(char) for char in password]
    for i in range(len(array_input) - 1, -1, -1):
        new = array_input[i] + 3
        array_input[i] = new % 10
    result = "".join(map(str, array_input))

    return result


def console():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


running = 1
while running == 1:
    console()
    menu = int(input("Please enter an option: "))
    if menu > 3 or menu < 1:
        print("Wrong format try again")
    else:
        if menu == 1:
            user_pass = input("Please enter your password to encode: ")
            while len(user_pass) != 8:
                print("Wrong format try again")
                password = input("Please enter your password to encode: ")
            encoded_pass = encode(user_pass)
            print("Your password has been encoded and stored!")
        if menu == 2:
            print("n/a")
        if menu == 3:
            break


