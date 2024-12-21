import random
import string

# Function to generate a random password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters  # Includes both lowercase and uppercase letters
    numbers = string.digits  # Includes digits 0-9
    symbols = string.punctuation  # Includes punctuation symbols like !@#$%^&*

    # Combine the character sets based on user preferences
    character_set = ""
    if use_letters:
        character_set += letters
    if use_numbers:
        character_set += numbers
    if use_symbols:
        character_set += symbols

    # Ensure there is at least one character to choose from
    if not character_set:
        raise ValueError("At least one character set must be selected (letters, numbers, or symbols).")

    # Generate the random password
    password = ''.join(random.choice(character_set) for _ in range(length))

    return password

# Main function to get user input and generate the password
def main():
    try:
        # Get user input for password length and character preferences
        length = int(input("Enter the desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 characters for better security.")
            return
        
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        # Display the generated password
        print(f"Your generated password is: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

# Run the main function
if __name__ == "__main__":
    main()
