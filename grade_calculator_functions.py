# John Rey Bulfa
# ITELEC2
# Laboratory #19 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

# Function to get the student's score
def get_student_score():
    score = input("Enter your score: ")
    try:
        score = float(score)
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return get_student_score()
    return score

# Function to calculate the grade
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main program flow
def main():
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")

if __name__ == "__main__":
    main()