

"""
02_space_complexity_examples.py

Topic:
    Space Complexity

Purpose:
    Learn how to identify additional memory used by an algorithm.

The main question throughout this file is:

    "As input size grows, how much EXTRA memory does
     this algorithm create?"

Important distinction:
    Input space != Auxiliary space

The input already exists.

We usually analyze the memory created by the algorithm
in addition to that input.

Examples covered:
    1. O(1) auxiliary space
    2. O(n) auxiliary space
    3. In-place processing
    4. Hash Set trade-off
    5. Hash Map trade-off
    6. Recursive call-stack space
    7. Matrix-sized additional memory

Run this file and read the comments carefully.
The goal is to understand WHY each complexity occurs,
not simply memorize the final answer.
"""


# ============================================================
# 1. O(1) AUXILIARY SPACE
# ============================================================

def find_max(numbers):
    """
    Find the largest number without creating
    another data structure proportional to the input.

    Example:

        numbers = [10, 25, 7, 40, 15]

        maximum starts at 10

        25 > 10
        maximum = 25

        7 < 25
        maximum = 25

        40 > 25
        maximum = 40

        15 < 40
        maximum = 40

    Additional memory:
        We only keep a few variables:

            maximum
            number

        The number of variables does not grow with n.

    Complexity:

        Time  = O(n)
        Space = O(1)

    Important:
        The input list itself may contain n elements.
        That does NOT mean the algorithm uses O(n)
        auxiliary space.
    """

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


# ============================================================
# 2. O(1) AUXILIARY SPACE — COUNTING
# ============================================================

def count_positive_numbers(numbers):
    """
    Count how many values are positive.

    We scan the input once.

    But we only maintain one counter.

    Complexity:

        Time  = O(n)
        Space = O(1)

    This is a common pattern:

        Process each record
        +
        Maintain a small fixed amount of state
    """

    count = 0

    for number in numbers:
        if number > 0:
            count += 1

    return count


# ============================================================
# 3. O(n) AUXILIARY SPACE — COPYING
# ============================================================

def copy_array(numbers):
    """
    Create a new list containing the input values.

    Example:

        input:
            [10, 20, 30]

        result:
            [10, 20, 30]

    We create a SECOND list.

    If the input contains n elements,
    the new list can also contain n elements.

    Therefore:

        Time  = O(n)
        Space = O(n)

    This is one of the easiest ways to recognize
    O(n) auxiliary space:

        "Am I creating another collection that grows
         with the size of the input?"
    """

    result = []

    for number in numbers:
        result.append(number)

    return result


# ============================================================
# 4. O(n) AUXILIARY SPACE — HASH SET
# ============================================================

def find_duplicates(numbers):
    """
    Detect whether an array contains a duplicate.

    The important idea is:

        seen = set()

    The set remembers values we have already processed.

    Example:

        [10, 20, 30, 20]

        Process 10:
            seen = {10}

        Process 20:
            seen = {10, 20}

        Process 30:
            seen = {10, 20, 30}

        Process 20:
            20 is already present
            duplicate found

    Why the space is O(n)
    ----------------------
    In the worst case, all n values are unique before
    we discover a duplicate or finish the scan.

    The set can therefore contain n values.

    Complexity:

        Time  = O(n) expected
        Space = O(n)

    This demonstrates a classic time-space trade-off:

        More memory
            ↓
        Faster lookup
    """

    seen = set()

    for number in numbers:

        if number in seen:
            return True

        seen.add(number)

    return False


# ============================================================
# 5. O(n) AUXILIARY SPACE — FREQUENCY MAP
# ============================================================

def build_frequency_map(values):
    """
    Count how many times each value occurs.

    Example:

        ["A", "B", "A", "C", "B", "A"]

        frequency becomes:

        {
            "A": 3,
            "B": 2,
            "C": 1
        }

    The dictionary can contain up to n distinct keys.

    Therefore:

        Time  = O(n) expected
        Space = O(n)

    This pattern becomes extremely important
    when we study HASHING.
    """

    frequency = {}

    for value in values:
        frequency[value] = frequency.get(value, 0) + 1

    return frequency


# ============================================================
# 6. O(1) AUXILIARY SPACE — IN-PLACE REVERSAL
# ============================================================

def reverse_in_place(numbers):
    """
    Reverse an array by modifying the existing list.

    Example:

        Before:
            [10, 20, 30, 40]

        After:
            [40, 30, 20, 10]

    We use two pointers:

        left
        right

    and swap values directly inside the existing list.

    We do NOT create another list such as:

        reversed_numbers = []

    Therefore:

        Time  = O(n)
        Space = O(1)

    This is called an in-place transformation.

    Important:
        O(1) auxiliary space does not mean zero memory.
        We still use a few variables.
        It means the extra memory does not grow with n.
    """

    left = 0
    right = len(numbers) - 1

    while left < right:

        numbers[left], numbers[right] = (
            numbers[right],
            numbers[left],
        )

        left += 1
        right -= 1

    return numbers


# ============================================================
# 7. O(n) SPACE — RECURSION / CALL STACK
# ============================================================

def countdown(n):
    """
    Demonstrate recursive call-stack memory.

    Example:

        countdown(3)

        countdown(3)
            ↓
        countdown(2)
            ↓
        countdown(1)
            ↓
        countdown(0)

    Each unfinished function call remains on
    the call stack.

    Maximum number of active calls:

        O(n)

    Therefore:

        Time  = O(n)
        Space = O(n)

    Important:
        The O(n) space does not come from a list.

        It comes from the recursive call stack.
    """

    if n <= 0:
        return

    countdown(n - 1)


# ============================================================
# 8. O(n × m) AUXILIARY SPACE
# ============================================================

def create_matrix(rows, columns):
    """
    Create a new matrix.

    Example:

        rows = 3
        columns = 4

        Additional storage:

            3 × 4 = 12 cells

    If:

        n = rows
        m = columns

    then:

        Space = O(n × m)

    This becomes important with large matrices or
    multi-dimensional datasets.
    """

    matrix = []

    for _ in range(rows):

        row = [0] * columns

        matrix.append(row)

    return matrix


# ============================================================
# 9. PRACTICE EXAMPLE
# ============================================================

def practice_example(numbers):
    """
    Analyze this function before reading the answer.

    Questions:

        1. What is the time complexity?
        2. What is the auxiliary space?
        3. Why?

    Hint:

        Look carefully at the list `result`.

    Think first.
    Then check your reasoning against the structure of
    the function.
    """

    result = []

    for number in numbers:

        if number > 0:
            result.append(number)

    return result


# ============================================================
# 10. PRACTICE EXAMPLE — IN-PLACE
# ============================================================

def practice_in_place(numbers):
    """
    Analyze before running.

    Questions:

        Time?
        Auxiliary space?

    Hint:

        No new list is created.

        Only a few variables are maintained.
    """

    for index in range(len(numbers)):

        numbers[index] *= 2

    return numbers


# ============================================================
# MAIN
# ============================================================

def main():
    """
    Run each example.

    While reading the output, focus on the relationship:

        Code
          ↓
        Memory created
          ↓
        How does it grow with n?
          ↓
        Space complexity
    """

    numbers = [10, 25, 7, 40, 15]

    print("=" * 60)
    print("1. O(1) auxiliary space")
    print("=" * 60)

    print("Maximum:", find_max(numbers))

    print("\nPositive count:", count_positive_numbers(numbers))

    print("\n" + "=" * 60)
    print("2. O(n) auxiliary space")
    print("=" * 60)

    copied = copy_array(numbers)

    print("Original:", numbers)
    print("Copy:", copied)

    print("\nDuplicates:", find_duplicates(numbers))

    values = ["A", "B", "A", "C", "B", "A"]

    print("\nFrequency map:")
    print(build_frequency_map(values))

    print("\n" + "=" * 60)
    print("3. In-place transformation")
    print("=" * 60)

    values_to_reverse = [10, 20, 30, 40]

    print("Before:", values_to_reverse)

    reverse_in_place(values_to_reverse)

    print("After:", values_to_reverse)

    print("\n" + "=" * 60)
    print("4. Recursive call-stack example")
    print("=" * 60)

    countdown(3)
    print("Countdown completed.")

    print("\n" + "=" * 60)
    print("5. O(n × m) matrix")
    print("=" * 60)

    matrix = create_matrix(3, 4)

    for row in matrix:
        print(row)

    print("\n" + "=" * 60)
    print("6. Practice examples")
    print("=" * 60)

    practice_input = [-2, 5, -1, 8, 3]

    print(
        "Practice 1:",
        practice_example(practice_input)
    )

    print(
        "Practice 2:",
        practice_in_place(practice_input.copy())
    )


if __name__ == "__main__":
    main()