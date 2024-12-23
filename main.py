import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Count satisfied criteria
    criteria_met = sum(
        [
            length_criteria,
            uppercase_criteria,
            lowercase_criteria,
            digit_criteria,
            special_char_criteria,
        ]
    )

    # Determine strength level
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one digit.")
    if not special_char_criteria:
        feedback.append("Include at least one special character (e.g., !@#$%^&*).")

    return strength, feedback

def main():
    print("Welcome to the Password Complexity Checker!")
    password = input("Enter a password to check its strength: ")

    strength, feedback = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

if __name__ == "__main__":
    main()
