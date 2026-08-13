"""
01_big_o_examples.py

DAY 1 — DSA FOUNDATIONS
Topic: Big-O Complexity

Purpose
-------
This file teaches Big-O by running small Python examples.

The goal is NOT to measure exact execution time.

The goal is to learn how to look at code and answer:

    1. How many times can this code execute?
    2. How does that change when input size grows?
    3. What is the time complexity?
    4. Does the algorithm create additional memory?
    5. What trade-off are we making?

Important idea
--------------
Big-O describes how resource usage grows with input size.

For example:

    O(1)  -> work stays approximately constant
    O(n)  -> work grows with input size
    O(n²) -> work grows roughly with the square of input size

Read this file from top to bottom and try to predict the
complexity BEFORE reading the explanation below each example.
"""


# ============================================================
# 1. O(1) — CONSTANT TIME
# ============================================================

def get_first(numbers):
    """
    Return the first element of the list.

    Example:
        numbers = [10, 20, 30, 40]

        numbers[0]
        ↓
        10

    Why O(1)?
    ----------
    We access an element directly using its index.

    It does NOT matter whether the list contains:

        10 elements
        1,000 elements
        1,000,000 elements

    We still perform one direct lookup.

    Therefore:

        Time  = O(1)
        Space = O(1)

    Important:
    ----------
    O(1) does not necessarily mean "exactly one CPU instruction".

    It means the amount of work does not grow with n.
    """

    return numbers[0]


# ============================================================
# 2. O(n) — LINEAR TIME
# ============================================================

def calculate_sum(numbers):
    """
    Add every value in the list.

    Example:

        [10, 20, 30, 40]

        10
        + 20
        + 30
        + 40

    Why O(n)?
    ----------
    If the list contains n elements, we must visit n elements.

    n = 10
        -> approximately 10 iterations

    n = 1,000
        -> approximately 1,000 iterations

    n = 1,000,000
        -> approximately 1,000,000 iterations

    The work grows linearly with input size.

    Therefore:

        Time  = O(n)
        Space = O(1)

    Why O(1) space?
    ----------------
    We only maintain the variable `total`.

    We are NOT creating another data structure containing n items.
    """

    total = 0

    for number in numbers:
        total += number

    return total


# ============================================================
# 3. O(n) — LINEAR SEARCH
# ============================================================

def linear_search(numbers, target):
    """
    Find the position of target using a left-to-right scan.

    Example:

        numbers = [10, 20, 30, 40]
        target  = 30

        Check 10 -> no
        Check 20 -> no
        Check 30 -> yes

    Time Complexity
    ----------------
    Best case:

        target is the first element
        -> O(1)

    Worst case:

        target is the last element
        OR
        target does not exist

        -> O(n)

    Average case:

        We may inspect a significant portion of the array.
        -> O(n)

    For interview discussions, always be clear about
    which case you are describing.

    Space Complexity
    ----------------
    We only use the variables `index` and `number`.

        Extra space = O(1)
    """

    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1


# ============================================================
# 4. O(n²) — NESTED LOOPS
# ============================================================

def count_all_pairs(numbers):
    """
    Count how many combinations are produced by two full loops.

    Example with n = 3:

        Outer loop:
            1
            2
            3

        For EACH outer iteration,
        the inner loop runs 3 times.

        Total:

            3 × 3
            = 9 operations

    General case:

        n × n
        = n²

    Therefore:

        Time  = O(n²)
        Space = O(1)

    Why this matters in interviews
    --------------------------------
    O(n²) can be acceptable for small input sizes.

    But consider:

        n = 100
        -> 10,000 operations

        n = 100,000
        -> 10,000,000,000 operations

    This is why input constraints matter.

    Common interview pattern
    -------------------------
    "Compare every pair."

    When you see that requirement,
    O(n²) brute force is often the first solution.

    Then we ask:

        Can hashing reduce repeated searches?
        Can sorting help?
        Can two pointers help?
    """

    count = 0

    for _ in numbers:

        for _ in numbers:
            count += 1

    return count


# ============================================================
# 5. O(n + m) — TWO INDEPENDENT INPUTS
# ============================================================

def process_two_inputs(first, second):
    """
    Process two different collections sequentially.

    Example:

        first  -> n elements
        second -> m elements

    Work performed:

        n + m

    Therefore:

        Time = O(n + m)

    IMPORTANT:
    ----------
    Do not automatically simplify this to O(n).

    Why?

    Because n and m may be completely independent.

    Example:

        first  = 100 elements
        second = 10,000,000 elements

    The second input still matters.

    Space:

        O(1)
    """

    total = 0

    for value in first:
        total += value

    for value in second:
        total += value

    return total


# ============================================================
# 6. O(n × m) — NESTED INDEPENDENT INPUTS
# ============================================================

def compare_two_inputs(first, second):
    """
    Compare every element from `first`
    with every element from `second`.

    Let:

        n = len(first)
        m = len(second)

    Outer loop:
        n iterations

    Inner loop:
        m iterations for each outer iteration

    Total:

        n × m

    Therefore:

        Time  = O(n × m)
        Space = O(1)

    Data-engineering connection
    ---------------------------
    This pattern is important because it resembles
    naive pairwise comparison between two datasets.

    For example:

        customers × transactions

    A naive nested comparison can become extremely expensive.

    This is one reason data systems use:

        hashing
        indexing
        joins
        partitioning

    instead of comparing every possible pair.
    """

    count = 0

    for first_value in first:

        for second_value in second:

            if first_value == second_value:
                count += 1

    return count


# ============================================================
# 7. O(log n) — REPEATEDLY REDUCING THE PROBLEM
# ============================================================

def count_halvings(n):
    """
    Repeatedly divide n by 2.

    Example:

        n = 32

        32
        16
        8
        4
        2
        1

    Number of iterations is much smaller than n.

    This gives:

        Time  = O(log n)
        Space = O(1)

    Key recognition signal
    ----------------------
    When the problem size repeatedly becomes:

        n
        n / 2
        n / 4
        n / 8
        ...

    think:

        O(log n)

    Classic example:

        Binary Search
    """

    steps = 0

    while n > 1:
        n //= 2
        steps += 1

    return steps


# ============================================================
# 8. O(n log n)
# ============================================================

def sort_and_sum(numbers):
    """
    Sort the input and then scan it.

    Step 1:
        sorted(numbers)

        approximately O(n log n)

    Step 2:
        scan the sorted list

        O(n)

    Combined:

        O(n log n) + O(n)

    The dominant term is:

        O(n log n)

    Therefore:

        Time = O(n log n)

    This pattern is common in algorithms such as:

        Merge Sort
        Heap Sort
        efficient comparison-based sorting

    Important interview habit
    --------------------------
    When combining different operations,
    identify the dominant growth term.
    """

    sorted_numbers = sorted(numbers)

    total = 0

    for number in sorted_numbers:
        total += number

    return total


# ============================================================
# 9. O(n) TIME + O(n) SPACE
# ============================================================

def build_seen_set(numbers):
    """
    Store every value in a set.

    Example:

        numbers = [10, 20, 30]

        seen = {10, 20, 30}

    We scan the input once:

        Time = O(n)

    But the set may contain n elements:

        Space = O(n)

    This is one of the most important DSA trade-offs:

        Use additional memory
        to improve lookup speed.

    This pattern will appear immediately
    when we study HASHING.
    """

    seen = set()

    for number in numbers:
        seen.add(number)

    return seen


# ============================================================
# 10. O(n) TIME + O(1) SPACE
# ============================================================

def find_max(numbers):
    """
    Find the maximum value while scanning the input once.

    Example:

        [10, 25, 7, 40, 15]

        maximum starts as 10

        25 > 10
        maximum = 25

        7 < 25
        maximum = 25

        40 > 25
        maximum = 40

        15 < 40
        maximum = 40

    We visit every element:

        Time = O(n)

    But we only maintain one variable:

        maximum

    Therefore:

        Auxiliary Space = O(1)

    This is an important distinction:

        O(n) input
        does NOT automatically mean
        O(n) extra space.
    """

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


# ============================================================
# 11. GROWTH VISUALIZATION THROUGH NUMBERS
# ============================================================

def show_growth(n):
    """
    Compare how common complexity classes grow.

    IMPORTANT:
    ----------
    These are mathematical operation counts.

    They are NOT actual execution times.

    Example:

        n = 10

        O(1)
            1

        O(log n)
            roughly 3-4

        O(n)
            10

        O(n²)
            100

    As n becomes larger, the gap between these
    complexity classes becomes enormous.
    """

    print(f"\nInput size n = {n}")

    print("O(1):", 1)

    # bit_length gives an approximate logarithmic measure.
    print("O(log n) approximately:", n.bit_length())

    print("O(n):", n)

    print("O(n²):", n * n)


# ============================================================
# 12. PRACTICE — PREDICT BEFORE RUNNING
# ============================================================

def practice_example(numbers):
    """
    DO NOT immediately look at the answer.

    First ask yourself:

        What is the time complexity?
        What is the space complexity?

    Then inspect the code.

    Hint:

        The outer loop runs n times.
        The inner operation does NOT necessarily
        run n times.

    This is intentionally included to prevent
    the common mistake:

        "Nested loop = automatically O(n²)"
    """

    count = 0

    for number in numbers:

        value = 1

        while value < len(numbers):
            value *= 2
            count += number

    return count


# ============================================================
# MAIN
# ============================================================

def main():
    """
    Run the examples.

    While learning, don't just look at the output.

    For each function ask:

        1. How many times does the main operation execute?
        2. Does input size affect the number of iterations?
        3. Is additional memory created?
        4. What is the final Big-O?
    """

    numbers = [10, 20, 30, 40, 50]

    print("1. O(1) example")
    print("First value:", get_first(numbers))

    print("\n2. O(n) example")
    print("Sum:", calculate_sum(numbers))

    print("\n3. O(n) linear search")
    print("Index of 30:", linear_search(numbers, 30))

    print("\n4. O(n²) example")
    print("Total pair operations:", count_all_pairs(numbers))

    print("\n5. O(n + m) example")
    print(
        process_two_inputs(
            [1, 2, 3],
            [4, 5]
        )
    )

    print("\n6. O(n × m) example")
    print(
        "Matches:",
        compare_two_inputs(
            [1, 2, 3],
            [2, 3]
        )
    )

    print("\n7. O(log n) example")
    print(
        "Halving steps:",
        count_halvings(1_000_000)
    )

    print("\n8. O(n log n) example")
    print(
        "Sorted sum:",
        sort_and_sum(numbers)
    )

    print("\n9. O(n) time + O(n) space")
    print(
        "Seen values:",
        build_seen_set(numbers)
    )

    print("\n10. O(n) time + O(1) space")
    print(
        "Maximum:",
        find_max(numbers)
    )

    print("\n11. Growth comparison")
    show_growth(10)
    show_growth(100)

    print("\n12. Practice example")
    print(practice_example(numbers))


if __name__ == "__main__":
    main()