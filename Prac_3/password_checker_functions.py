def main():
    password = get_password()
    print_password(password)


def print_password(password):
    for char in password:
        print("*", end=" ")


def get_password():
    password = input("Please enter your password: ")
    return password


main()
