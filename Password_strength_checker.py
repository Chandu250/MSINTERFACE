import re

def assess_password_strength(password):
    # Check if password is a string
    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Feedback list
    feedback = []
    
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")
    
    # Strength assessment
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong", "Extremely Strong"]
    
    strength = strength_levels[strength_score]
    
    return {
        "strength": strength,
        "score": strength_score,
        "feedback": feedback
    }

# Main program
def main():
    try:
        password = input("Enter your password: ")
        result = assess_password_strength(password)
        print("Password Strength:", result["strength"])
        print("Score:", result["score"])
        print("Feedback:", result["feedback"])
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
