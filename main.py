def read_input_file(file_path):
    """
    Reads the input file and returns the array length and the array of numbers.

    Args:
    file_path (str): The path to the input file.

    Returns:
    Tuple[int, List[int]]: The size of the array and the array of numbers read from the input file.
    """
    with open(file_path, 'r') as file:
        # Read the first line for the size of the array
        array_length = int(file.readline().strip())
        # Read the second line for the numbers in the array
        numbers = list(map(int, file.readline().strip().split()))
        return array_length, numbers


def can_reach_end(numbers):
    """
    Determine if it's possible to reach the end of the list 'numbers'.

    The function simulates a jump game where each element in the array
    represents the maximum jump length from that position. The goal is to
    check if you can reach the last position starting from the first position.

    Parameters:
    numbers (list of int): A list where each element represents the maximum
                           jump length from that position.

    Returns:
    bool: True if the end of the list can be reached, False otherwise.
    """
    farthest = 0
    for i in range(len(numbers) - 1):
        farthest = max(farthest, i + numbers[i])
        # If we are stuck and can't move forward.
        if farthest <= i:
            return False
    return farthest >= len(numbers) - 1


def min_moves_to_reach_end(array_length, numbers):
    """
    Calculates the minimum number of moves to reach the end of the array.

    Args:
    array_length (int): The size of the array.
    numbers (List[int]): The array of numbers indicating the maximum length of a right move.

    Returns:
    int: The minimum number of moves to reach the end of the array or -1 if it's impossible.
    """

    # Check if it is impossible to move forward, e.g. for numbers = [2, 0, 1, 0, 4], we cannot reach the last index
    if not can_reach_end(numbers):
        return -1

    moves, current_max_reach, farthest_reach = 0, 0, 0

    for i in range(array_length - 1):
        farthest_reach = max(farthest_reach, i + numbers[i])

        # Make a move when reaching the current maximum reach
        if i == current_max_reach:
            moves += 1
            current_max_reach = farthest_reach

            # Check if the end of the array is reached or surpassed
            if current_max_reach >= array_length - 1:
                break

    return moves


def main():
    # Assuming the input file has been uploaded to the environment
    input_file_path = 'input.txt'
    numbers_size, numbers_from_file = read_input_file(input_file_path)
    minimum_moves = min_moves_to_reach_end(numbers_size, numbers_from_file)
    print("Minimum moves from the input file:", minimum_moves)


if __name__ == "__main__":
    main()
