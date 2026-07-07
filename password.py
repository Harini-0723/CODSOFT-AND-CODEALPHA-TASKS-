import random
import string

def generate_password(length):
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + numbers + symbols

    # Ensure password has at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the remaining length
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password
    random.shuffle(password)

    return "".join(password)


def main():
    print("=" * 45)
    print("        RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()