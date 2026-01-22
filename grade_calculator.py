#Grade Calculator

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks entered")
else:
    if marks >= 90:
        print("Grade A – Distinction")
    elif marks >= 75:
        print("Grade B - Very Good")
    elif marks >= 60:
        print("Grade C - Good")
    elif marks >= 40:
        print("Grade D - Pass")
    else:
        print("Fail")
