def calculate_grade(score):
    if score >= 9:
        return 'A'
    elif score >= 8:
        return 'B'
    elif score >= 7:
        return 'C'
    elif score >= 6:
        return 'D'
    elif score >= 5:
        return 'E'
    else:
        return 'F'

def main():
    scores = []
    while True:
        user_input = input("Enter a score out of 10 (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            score = float(user_input)
            if 0 <= score <= 10:
                scores.append(score)
            else:
                print("Please enter a score between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for score in scores:
        grade = calculate_grade(score)
        print(f"Score: {score}, Grade: 
