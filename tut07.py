#lab6
def Upper(s):
    for i in s:
        if 'A' <= i <= 'Z':
            return 1
    return 0

def Lower(s):
    for i in s:
        if 'a' <= i <= 'z':
            return 1
    return 0

def Num(s):
    for i in s:
        if '0' <= i <= '9':
            return 1
    return 0

def SpChar(s):
    ct = 0
    for i in s:
        if i in ('!', '@', '#'):
            ct += 1
        elif 'A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9':
            continue
        else:
            return 'Falsechar'
    if ct > 0:
        return 'True'
    else:
        return 'NoSpChar'

def criteria(s, crit):
    invalid = 0
    print(s)
    for i in crit:
        if i == '1':
            if Upper(s) == 0:
                if invalid == 0:
                    print(" Invalid password")
                    invalid = 1
                print(" No uppercase in it")
        elif i == '2':
            if Lower(s) == 0:
                if invalid == 0:
                    print(" Invalid password")
                    invalid = 1
                print(" No lowercase in it")
        elif i == '3':
            if Num(s) == 0:
                if invalid == 0:
                    print(" Invalid password")
                    invalid = 1
                print(" No numbers in it")
        elif i == '4':
            sp_char_check = SpChar(s)
            if sp_char_check == 'Falsechar':
                if invalid == 0:
                    print(" Invalid password")
                    invalid = 1
                print(" False character in it")
            elif sp_char_check == 'NoSpChar':
                if invalid == 0:
                    print(" Invalid password")
                    invalid = 1
                print(" No Special characters in it")

    if invalid == 0:
        print(" Valid password")
        return 1
    else:
        print(" Invalid password")
        return 0

def main():
    print("Choose criteria req: ")
    print("1. UpperCase")
    print("2. LowerCase")
    print("3. Numbers")
    print("4. Special Characters (!, @, #)")
    crit = input("Enter criteria numbers (comma-separated): ").split(',')

    # Read passwords from the file
    valid_c = 0
    invalid_c = 0
    try:
        with open('pass.txt', 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print("The file 'pass.txt' was not found.")
        return

    for i in passwords:
        if len(i) < 8:
            print(i)
            print(" Invalid password")
            print(" Less than 8 characters")
            invalid_c += 1
        else:
            valid = criteria(i.strip(), crit)
            if valid == 1:
                valid_c += 1
            else:
                invalid_c += 1

    print(f"\nNumber of Valid passwords: {valid_c}")
    print(f"Number of Invalid passwords: {invalid_c}")

if __name__ == "__main__":
    main()



#part2
def is_valid_password(password):
    """
    Function to check if a password is valid.
    Rules:
    - Must be at least 8 characters long.
    - Must contain at least one uppercase letter.
    - Must contain at least one lowercase letter.
    - Must contain at least one digit.
    """
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


def validate_passwords_from_file(filename):
    """
    Reads passwords from the file and validates them.
    Skips passwords that start with 'skip_'.
    """
    try:
        with open(filename, 'r') as file:
            passwords = file.readlines()

        valid_count = 0
        invalid_count = 0

        for password in passwords:
            password = password.strip()  # Remove trailing whitespace and newline
            if password.startswith("skip_"):
                continue  # Skip the password if it starts with 'skip_'

            if is_valid_password(password):
                valid_count += 1
            else:
                invalid_count += 1

        print(f"Total valid passwords: {valid_count}")
        print(f"Total invalid passwords: {invalid_count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


# File to read passwords from
input_file = "input.txt"
validate_passwords_from_file(input_file)
