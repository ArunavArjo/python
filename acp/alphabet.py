char_input = input("Enter a character: ")

if len(char_input) == 1:
    if 'a' <= char_input <= 'z' or 'A' <= char_input <= 'Z':
        print(f"'{char_input}' is an alphabet.")
    else:
        print(f"'{char_input}' is not an alphabet.")
else:
    print("Please enter only one character.")