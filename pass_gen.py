import random
import string
import re
import pyperclip

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def check_strength(password):
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^\w\s]", password))
    length = len(password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "🟢 Strong"
    elif length >= 8 and score >= 3:
        return "🟡 Moderate"
    else:
        return "🔴 Weak"

def main():
    print("🔐 Password Generator 🔐")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            strength = check_strength(password)
            print(f"\nGenerated Password: {password}")
            print(f"Password Strength: {strength}")

            choice = input("📋 Do you want to copy this password to clipboard? (yes/no): ").lower()
            if choice in ["yes", "y"]:
                pyperclip.copy(password)
                print("✅ Password copied to clipboard!")
            else:
                print("Password not copied.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
