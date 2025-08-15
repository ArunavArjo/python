def process_squares(start, end):
    """
    Calculates the square of numbers within a given range,
    then filters and prints odd and even square values.

    Args:
        start (int): The beginning of the number range (inclusive).
        end (int): The end of the number range (inclusive).
    """

    odd_squares = []
    even_squares = []

    for num in range(start, end + 1):
        square = num ** 2
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print(f"Odd Square Values: {odd_squares}")
    print(f"Even Square Values: {even_squares}")

  