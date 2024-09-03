import os
import time
import itertools
import sys

# Colors for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    MAGENTA = '\033[35m'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the main header with an animation effect."""
    header = Colors.CYAN + Colors.BOLD + """
  _____ _            _                 _             
 / ____| |          | |               | |            
| (___ | |_   _  ___| |_ __ _ _ __ ___| |_ ___  _ __ 
 \___ \| | | | |/ __| __/ _` | '__/ _ \ __/ _ \| '__|
 ____) | | |_| | (__| || (_| | | |  __/ || (_) | |   
|_____/|_|\__,_|\___|\__\__,_|_|  \___|\__\___/|_|   
                                               
""" + Colors.ENDC
    print(header)
    time.sleep(0.5)

def animate_text(text, delay=0.1):
    """Animate text by printing it character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_table(content):
    """Print content in a table format with borders."""
    border = "+" + "-"*50 + "+"
    print(Colors.MAGENTA + border + Colors.ENDC)
    for line in content:
        print(Colors.MAGENTA + "| " + line.ljust(48) + " |" + Colors.ENDC)
    print(Colors.MAGENTA + border + Colors.ENDC)

def generate_combinations(first_name, last_name, pet_name, birthday, color, number, hobby):
    """Generate a wide variety of password combinations."""
    components = [first_name, last_name, pet_name, birthday[:2], birthday[-2:], birthday[:4], birthday[-4:], birthday, color, number, hobby]
    passwords = set()

    # Generate all combinations with different lengths
    for r in range(2, len(components) + 1):
        for combo in itertools.permutations(components, r):
            passwords.add(''.join(combo))

    # Adding variations with special characters and numbers
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    for password in list(passwords):
        for char in special_chars:
            passwords.add(password + char)
            passwords.add(char + password)
            passwords.add(password + char + char)
            passwords.add(char + char + password)

    # Capitalization variations
    for password in list(passwords):
        passwords.add(password.capitalize())
        passwords.add(password.lower())
        passwords.add(password.upper())

    # Add variations with numbers and special chars mixed in
    for password in list(passwords):
        for i in range(0, 100):
            passwords.add(password + str(i))
            passwords.add(str(i) + password)
            passwords.add(password + str(i) + '!')
            passwords.add('!' + password + str(i))

    return list(passwords)

def generate_combinations_fast(first_name, last_name, pet_name, birthday, color, number, hobby):
    """Generate a simplified set of password combinations quickly."""
    components = [first_name, last_name, pet_name, birthday[:2], birthday[-2:], color, number]
    passwords = set()

    # Generate combinations with fewer permutations
    for r in range(2, len(components) + 1):
        for combo in itertools.permutations(components, r):
            passwords.add(''.join(combo))

    # Add some basic variations
    for password in list(passwords):
        passwords.add(password.capitalize())
        passwords.add(password.lower())
        passwords.add(password.upper())
        passwords.add(password + '!')
        passwords.add('!' + password)

    return list(passwords)

def save_passwords_to_file(passwords, first_name):
    """Save generated passwords to a text file."""
    if not os.path.exists('results'):
        os.makedirs('results')

    file_path = f'results/{first_name}.txt'
    with open(file_path, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

    return file_path, len(passwords)

def create_password(slow=True):
    print(Colors.YELLOW + "\nLet's create a custom password based on your input...\n" + Colors.ENDC)
    
    first_name = input(Colors.BLUE + "What is the person's first name? " + Colors.ENDC).strip()
    last_name = input(Colors.BLUE + "What is the person's last name? " + Colors.ENDC).strip()
    
    pet_name = input(Colors.BLUE + "Does the person have a pet? What's its name? (type 'no' if they don't have one): " + Colors.ENDC).strip()
    pet_name = '' if pet_name.lower() == 'no' else pet_name.strip()
    
    birthday = input(Colors.BLUE + "What is the person's birthday? (Example: 01012001): " + Colors.ENDC).strip()
    
    color = input(Colors.BLUE + "What is the person's favorite color? (type 'no' if unknown): " + Colors.ENDC).strip()
    color = '' if color.lower() == 'no' else color.strip()
    
    number = input(Colors.BLUE + "What is the person's favorite number? (type 'no' if unknown): " + Colors.ENDC).strip()
    number = '' if number.lower() == 'no' else number.strip()
    
    hobby = input(Colors.BLUE + "What is the person's favorite hobby? (type 'no' if unknown): " + Colors.ENDC).strip()
    hobby = '' if hobby.lower() == 'no' else hobby.strip()
    
    print(Colors.GREEN + "\nCreating the custom password based on the information..." + Colors.ENDC)
    time.sleep(1)  # Simulate processing time
    
    # Generate passwords based on the selected mode
    if slow:
        passwords = generate_combinations(first_name, last_name, pet_name, birthday, color, number, hobby)
    else:
        passwords = generate_combinations_fast(first_name, last_name, pet_name, birthday, color, number, hobby)
    
    # Save passwords to file and get summary
    file_path, num_passwords = save_passwords_to_file(passwords, first_name)
    
    # Print summary
    print(Colors.GREEN + f"\n{num_passwords} Passwords saved to: {file_path}" + Colors.ENDC)

def main_menu():
    clear_screen()
    print_header()
    
    # Main menu with border and table format
    menu_content = [
        "[1] Password Creator",
        "[2] Password Custom (Fast)"
    ]
    print_table(menu_content)
    
    print()
    
    choice = input(Colors.YELLOW + "Pick one: " + Colors.ENDC).strip()
    
    if choice == "1":
        animate_text("Loading Password Creator...", delay=0.05)
        create_password(slow=True)
    elif choice == "2":
        animate_text("Loading Password Custom (Fast)...", delay=0.05)
        create_password(slow=False)
    else:
        print(Colors.RED + "\nInvalid choice. Please select a valid option.\n" + Colors.ENDC)

if __name__ == "__main__":
    while True:
        main_menu()
        continue_choice = input(Colors.YELLOW + "Do you want to create another payload? (yes/no): " + Colors.ENDC).strip().lower()
        if continue_choice != "yes":
            print(Colors.RED + "Exiting the program. Goodbye!" + Colors.ENDC)
            break
