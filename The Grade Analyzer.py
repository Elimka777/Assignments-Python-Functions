#The aim of this assignment is to analyze a set of grades and provide statistics.

#Task 1: Code a function to calculate the average grade.
#Task 2: Implement a function to find the highest and lowest grade.
#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
def calculate(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)

grades = [50, 95, 60, 88, 70]
average_grade = calculate(grades)
print("Average grade:", average_grade)

highest_grade = max(grades)
lowest_grade = min(grades)

print(f'The highest grade is {highest_grade}.')
print(f'The lowest grade is {lowest_grade}.')

def category(grades):
    letter_grades = {}  # Initialize the dictionary before the loop
    for grade in grades:
        if grade >= 90:
            letter_grades[grade] = 'A'
        elif grade >= 80:
            letter_grades[grade] = 'B'
        elif grade >= 70:
            letter_grades[grade] = 'C'
        elif grade >= 60:
            letter_grades[grade] = 'D'
        else:
            letter_grades[grade] = 'F'
    return letter_grades

letter_grades = category(grades)

for grade, letter_grade in letter_grades.items():
    print(f"{grade}\t{letter_grade}")