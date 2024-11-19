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
