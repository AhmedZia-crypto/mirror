def print_mirrored_right_triangle(rows, character):
    """
    Prints a mirrored right-angled triangle pattern.

    Args:
        rows (int): The total number of rows for the triangle.
        character (str): The character to use for printing the triangle.
    """
    if not isinstance(rows, int) or rows <= 0:
        print("Error: Number of rows must be a positive integer.")
        return
    if not isinstance(character, str) or len(character) != 1:
        print("Error: Character must be a single character string.")
        return

    print("Mirrored Right Triangle Pattern:")
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(1, rows - i + 1):
            print(" ", end=" ")
        # Print characters
        for k in range(1, i + 1):
            print(character, end=" ")
        print() # Move to the next line

