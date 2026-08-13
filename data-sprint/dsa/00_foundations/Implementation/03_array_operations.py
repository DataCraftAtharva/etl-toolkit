"""
03_array_operations.py

Topic:
    Arrays / Python Lists

Purpose:
    Learn how common array operations behave and why their
    time and space complexities differ.

Python's `list` behaves like a dynamic array.

The most important mental model is:

    Fast random access
        ↓
    Expensive shifting

This explains why:

    numbers[index]       -> O(1)
    numbers.append(x)    -> O(1) amortized
    numbers.insert(0,x)  -> O(n)
    numbers.pop(0)       -> O(n)

The goal of this file is not just to memorize these
complexities.

For every operation, ask:

    1. Does the program need to find something?
    2. Does it need to shift existing elements?
    3. Does it create a new collection?
    4. Does the amount of work grow with n?
"""


# ============================================================
# 1. ACCESS BY INDEX — O(1)
# ============================================================

def access_by_index(numbers, index):
    """
    Access an element directly using its index.

    Example:

        numbers = [10, 20, 30, 40]

        index = 2

        numbers[2]
        ↓
        30

    Why O(1)?
    ----------
    We are asking for a specific position.

    The list does not need to scan all previous elements.

    Complexity:

        Time  = O(1)
        Space = O(1)

    Interview connection:
    ---------------------
    If a problem repeatedly asks for values at known
    indices, an array/list is usually a good structure.
    """

    return numbers[index]


# ============================================================
# 2. UPDATE BY INDEX — O(1)
# ============================================================

def update_by_index(numbers, index, value):
    """
    Replace an element at a specific index.

    Example:

        [10, 20, 30, 40]

        update index 2 to 100

        [10, 20, 100, 40]

    Complexity:

        Time  = O(1)
        Space = O(1)

    We modify the existing array.
    No new array is required.
    """

    numbers[index] = value

    return numbers


# ============================================================
# 3. LINEAR SEARCH — O(n)
# ============================================================

def search_value(numbers, target):
    """
    Search for a value by scanning from left to right.

    Example:

        [10, 20, 30, 40]

        target = 30

        Check:
            10 -> no
            20 -> no
            30 -> yes

    Best case:
        target is first
        -> O(1)

    Worst case:
        target is last or missing
        -> O(n)

    Complexity:

        Time  = O(n) worst case
        Space = O(1)

    Important distinction:

        numbers[2]
        -> index access
        -> O(1)

        30 in numbers
        -> value search
        -> O(n)
    """

    for index, number in enumerate(numbers):

        if number == target:
            return index

    return -1


# ============================================================
# 4. APPEND — O(1) AMORTIZED
# ============================================================

def append_value(numbers, value):
    """
    Add an element to the end.

    Example:

        Before:
            [10, 20, 30]

        append 40

        After:
            [10, 20, 30, 40]

    Typical complexity:

        Time = O(1) amortized
        Space = O(1) auxiliary per operation,
                ignoring occasional internal resizing.

    Why "amortized"?
    -----------------
    A dynamic array sometimes needs to allocate a larger
    storage area and move existing elements.

    That individual resize is expensive.

    But across many append operations, the average cost
    remains O(1).

    For interview purposes:

        append -> O(1) amortized
    """

    numbers.append(value)

    return numbers


# ============================================================
# 5. INSERT AT BEGINNING — O(n)
# ============================================================

def insert_at_beginning(numbers, value):
    """
    Insert a value at index 0.

    Example:

        Before:
            [20, 30, 40]

        Insert 10:

            [10, 20, 30, 40]

    Why O(n)?
    ----------
    Existing elements may need to move to create space
    at the beginning.

    Conceptually:

        [20][30][40]
         ↓
        shift elements right
         ↓
        [10][20][30][40]

    The number of elements that may move grows with n.

    Complexity:

        Time  = O(n)
        Space = O(1) auxiliary
    """

    numbers.insert(0, value)

    return numbers


# ============================================================
# 6. INSERT IN MIDDLE — O(n)
# ============================================================

def insert_in_middle(numbers, index, value):
    """
    Insert a value at an arbitrary position.

    Example:

        [10, 20, 40, 50]

        insert 30 at index 2

        [10, 20, 30, 40, 50]

    Elements after the insertion position may need to shift.

    Worst case:

        inserting near the beginning

    Complexity:

        Time  = O(n)
        Space = O(1) auxiliary
    """

    numbers.insert(index, value)

    return numbers


# ============================================================
# 7. DELETE FROM END — O(1) AMORTIZED
# ============================================================

def remove_last(numbers):
    """
    Remove and return the final element.

    Example:

        [10, 20, 30, 40]
                   ↑
                remove

        [10, 20, 30]

    No shifting of all remaining elements is required.

    Complexity:

        Time  = O(1) amortized
        Space = O(1) auxiliary
    """

    return numbers.pop()


# ============================================================
# 8. DELETE FROM BEGINNING — O(n)
# ============================================================

def remove_first(numbers):
    """
    Remove the first element.

    Example:

        [10, 20, 30, 40]
         ↑

        remove 10

        [20, 30, 40]

    Why O(n)?
    ----------
    The remaining elements need to shift toward index 0.

    Complexity:

        Time  = O(n)
        Space = O(1) auxiliary
    """

    return numbers.pop(0)


# ============================================================
# 9. TRAVERSAL — O(n)
# ============================================================

def calculate_sum(numbers):
    """
    Visit every element and calculate the sum.

    If there are n elements:

        n elements
        ↓
        n iterations

    Complexity:

        Time  = O(n)
        Space = O(1)

    This is the basic pattern behind many array problems:

        scan
        inspect
        update state
    """

    total = 0

    for number in numbers:
        total += number

    return total


# ============================================================
# 10. FIND MAXIMUM — O(n) TIME / O(1) SPACE
# ============================================================

def find_max(numbers):
    """
    Find the maximum value using a single pass.

    Instead of sorting:

        sorted(numbers)
        -> O(n log n)

    we only need one scan.

    Maintain:

        current maximum

    and update it when a larger value appears.

    Complexity:

        Time  = O(n)
        Space = O(1)

    This is an important interview lesson:

        Do not use sorting if the problem only requires
        the maximum/minimum and a simple scan is enough.
    """

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


# ============================================================
# 11. IN-PLACE UPDATE — O(n) TIME / O(1) SPACE
# ============================================================

def double_values_in_place(numbers):
    """
    Double every value directly inside the existing list.

    Example:

        Before:
            [1, 2, 3, 4]

        After:
            [2, 4, 6, 8]

    We are NOT doing:

        new_numbers = []

    Instead, we modify:

        numbers[index]

    Therefore:

        Time  = O(n)
        Space = O(1)

    Interview connection:
    ---------------------
    When an interviewer says:

        "Do it in-place."

    they are usually asking you to avoid creating
    another data structure proportional to the input.
    """

    for index in range(len(numbers)):
        numbers[index] *= 2

    return numbers


# ============================================================
# 12. COPY — O(n) SPACE
# ============================================================

def copy_array(numbers):
    """
    Create a new list containing the same values.

    Example:

        numbers:
            [1, 2, 3]

        copy:
            [1, 2, 3]

    A second structure is created.

    If n elements exist in the input,
    the new list can also contain n elements.

    Complexity:

        Time  = O(n)
        Space = O(n)
    """

    copied_numbers = []

    for number in numbers:
        copied_numbers.append(number)

    return copied_numbers


# ============================================================
# 13. PRACTICE — PREDICT BEFORE RUNNING
# ============================================================

def practice_array_problem(numbers):
    """
    Find the first even number.

    STOP before reading the complexity.

    Ask yourself:

        How many elements can we inspect?
        Does the algorithm create extra storage?

    Important:
    ----------
    Best case and worst case are different.

        Best case:
            first element is even
            -> O(1)

        Worst case:
            last element is even
            or no even value exists
            -> O(n)

    Auxiliary space:
        O(1)
    """

    for number in numbers:

        if number % 2 == 0:
            return number

    return None


# ============================================================
# MAIN
# ============================================================

def main():
    """
    Run each array operation.

    While reading the output, think about the operation
    being performed and its complexity.
    """

    numbers = [10, 20, 30, 40, 50]

    print("=" * 60)
    print("1. Access by index")
    print("=" * 60)

    print("Element at index 2:", access_by_index(numbers, 2))

    print("\n" + "=" * 60)
    print("2. Update by index")
    print("=" * 60)

    updated = numbers.copy()

    print("Before:", updated)

    update_by_index(updated, 2, 100)

    print("After:", updated)

    print("\n" + "=" * 60)
    print("3. Linear search")
    print("=" * 60)

    print("Index of 40:", search_value(numbers, 40))

    print("\n" + "=" * 60)
    print("4. Append")
    print("=" * 60)

    appended = numbers.copy()

    append_value(appended, 60)

    print("After append:", appended)

    print("\n" + "=" * 60)
    print("5. Insert at beginning")
    print("=" * 60)

    beginning = numbers.copy()

    insert_at_beginning(beginning, 5)

    print("After insert:", beginning)

    print("\n" + "=" * 60)
    print("6. Insert in middle")
    print("=" * 60)

    middle = numbers.copy()

    insert_in_middle(middle, 2, 25)

    print("After insert:", middle)

    print("\n" + "=" * 60)
    print("7. Remove from end")
    print("=" * 60)

    end_removed = numbers.copy()

    removed = remove_last(end_removed)

    print("Removed:", removed)
    print("Remaining:", end_removed)

    print("\n" + "=" * 60)
    print("8. Remove from beginning")
    print("=" * 60)

    beginning_removed = numbers.copy()

    removed = remove_first(beginning_removed)

    print("Removed:", removed)
    print("Remaining:", beginning_removed)

    print("\n" + "=" * 60)
    print("9. Traversal")
    print("=" * 60)

    print("Sum:", calculate_sum(numbers))

    print("\n" + "=" * 60)
    print("10. Find maximum")
    print("=" * 60)

    print("Maximum:", find_max(numbers))

    print("\n" + "=" * 60)
    print("11. In-place update")
    print("=" * 60)

    in_place = [1, 2, 3, 4]

    print("Before:", in_place)

    double_values_in_place(in_place)

    print("After:", in_place)

    print("\n" + "=" * 60)
    print("12. Copy")
    print("=" * 60)

    original = [1, 2, 3]

    copied = copy_array(original)

    print("Original:", original)
    print("Copied:", copied)

    print("\n" + "=" * 60)
    print("13. Practice")
    print("=" * 60)

    print(
        "First even:",
        practice_array_problem(
            [1, 3, 7, 8, 11]
        )
    )


if __name__ == "__main__":
    main()