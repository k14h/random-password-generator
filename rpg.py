import random
import string

def generate_password(length, has_letters, has_numbers, has_symbols):
    password = ''
    char_set = ''

    if has_letters:
        char_set += string.ascii_letters
    if has_numbers:
        char_set += string.digits
    if has_symbols:
        char_set += string.punctuation

    for _ in range(length):
        password += random.choice(char_set)

    return password

def main():
    print("Random Password Generator")
    print("------------------------")

    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    has_letters = input("Include letters? (y/n): ").lower() == 'y'
    has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    has_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    if not has_letters and not has_numbers and not has_symbols:
        print("You must select at least one character type.")
        return

    password = generate_password(length, has_letters, has_numbers, has_symbols)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
