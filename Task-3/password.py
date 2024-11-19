import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user preferences."""
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    return ''.join(random.choice(character_pool) for _ in range(length))

def main():
    print("\n<<<---Welcome to the Password Generator!--->>>\n")

    try:
        # Get user input for password criteria
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4.")
            return

        use_letters = input("Include letters? (Y/N): ").strip().upper() == 'Y'
        use_numbers = input("Include numbers? (Y/N): ").strip().upper() == 'Y'
        use_symbols = input("Include symbols? (Y/N): ").strip().upper() == 'Y'

        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}\n")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
