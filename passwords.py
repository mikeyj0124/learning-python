password = input("Enter your password: ")
uppercase_count = 0
lowercase_count = 0
digit_count = 0
symbol_count = 0


for value in password:
    if value.isupper():
        uppercase_count += 1
    elif value.islower():
        lowercase_count += 1
    elif value.isdigit():
        digit_count += 1
    else:
        symbol_count += 1

print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Symbols: {symbol_count}")
