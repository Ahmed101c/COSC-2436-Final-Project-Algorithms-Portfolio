def calculate_total_value(solution, items):
    """
    Calculate total value of a solution (list of item names).

    Args:
        solution: List of item names
        items: List of tuples (name, weight, value)

    Returns:
        Total value of the items in solution
    """
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total


def knapsack(items, capacity):
    """
    Solve the knapsack problem using dynamic programming.

    Args:
        items: List of tuples (name, weight, value)
        capacity: Maximum weight capacity

    Returns:
        2D grid containing optimal item combinations
    """
    n = len(items)
    # Create a 2D grid to store solutions
    # grid[i][w] will store the best items for first i items with capacity w
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    # TODO: Fill in the dynamic programming logic
    # Hint: For each item and each capacity, decide whether to include the item or not
    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            # TODO: Check if current item's weight exceeds current capacity
            if weight > w:
                # TODO: If item is too heavy, copy solution from previous row
                grid[i][w] = grid[i - 1][w][:]
            else:
                # TODO: Calculate value if we include current item
                # include_value = previous solution with reduced capacity + current item
                include_solution = grid[i - 1][w - weight][:] + [item_name]

                # TODO: Get value if we exclude current item
                exclude_solution = grid[i - 1][w][:]

                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                # TODO: Choose the better option (higher total value)
                # Compare sum of values and store the better solution
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


def display_grid(grid, items):
    """
    Display the dynamic programming grid in a formatted table.

    Args:
        grid: 2D list containing optimal solutions
        items: List of items used in the problem
    """
    n = len(items)
    cell_width = 12

    # TODO: Print header row with capacity numbers
    header = ""
    for i in range(1, len(grid[0])):
        # TODO: Format capacity numbers as column headers
        header += "{:>{width}}".format(str(i), width=cell_width)
    print(" " * cell_width + header)

    # TODO: Print each row with item name and solutions
    for i in range(1, n + 1):
        # TODO: Start row with item name
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)

        # TODO: For each capacity, show the optimal items and total value
        for cell in grid[i][1:]:
            if cell:  # If there are items in this cell
                # TODO: Create string showing items (first letters) and total value
                # Format: $value(items) e.g., "$3500(GS)"
                total_value = calculate_total_value(cell, items)
                letters = "".join(name[0] for name in cell)
                cell_text = "${}({})".format(total_value, letters)
                row += "{:>{width}}".format(cell_text, width=cell_width)
            else:
                # TODO: Add empty space for cells with no items
                row += " " * cell_width

        print(row)


# Test data - items with (name, weight, value)
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000)
]

capacity = 6

# TODO: Call the knapsack function and store the result
grid = knapsack(items, capacity)

# TODO: Display the grid
display_grid(grid, items)

print("Knapsack problem solver - fill in the TODOs to complete!")
