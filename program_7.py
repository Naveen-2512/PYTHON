
def transform_matrix(matrix):
    # Multiply each element by 2 using map()
    result = list(map(lambda row: list(map(lambda x: x * 2, row)), matrix))
    return result


def filter_negative(matrix):
    # Remove negative numbers from each row
    result = list(map(
        lambda row: list(filter(lambda x: x >= 0, row)),
        matrix
    ))
    return result


def sort_data(data):
    # Sort data using the absolute value of each number
    return sorted(data, key=lambda x: abs(x))


def display_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    matrix = [
        [1, -4, 3],
        [-8, 5, 7],
        [-6, 4, 9]
    ]

    print("Original Matrix:")
    display_matrix(matrix)

    print("\nTransformed Matrix (Each Element * 2):")
    display_matrix(transform_matrix(matrix))

    print("\nMatrix After Removing Negative Values:")
    display_matrix(filter_negative(matrix))

    data = [5, -2, 8, -1, 3, -7]

    print("\nOriginal Data:", data)
    print("Sorted Data by Absolute Value:", sort_data(data))


if __name__ == "__main__":
    main()
