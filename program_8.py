
def calculate_statistics(*marks):
    # Check whether marks are provided
    if len(marks) == 0:
        return None

    total = sum(marks)
    average = total / len(marks)
    minimum = min(marks)
    maximum = max(marks)

    # Calculate grade
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, average, minimum, maximum, grade


def display_student(name, *marks, **details):
    print("\nStudent Name:", name)
    print("Marks:", marks)

    result = calculate_statistics(*marks)

    if result is None:
        print("No marks available.")
        return

    total, average, minimum, maximum, grade = result

    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Minimum Marks:", minimum)
    print("Maximum Marks:", maximum)
    print("Final Grade:", grade)

    # Display additional keyword information
    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(key, ":", value)


def main():
    display_student(
        "Naveen",
        95, 92, 88, 82, 78,
        course="BTech CSE",
        semester=3
    )

    display_student(
        "Muskan",
        85, 62, 90, 89,
        course="BTech CSE",
        semester=5
    )


if __name__ == "__main__":
    main()
