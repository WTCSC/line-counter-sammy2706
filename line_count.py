def line_count():
    # Opens file.txt as read only and saves it to the variable file
    with open("file.txt", "r") as file:
    # Declare and define lines
        lines = 0
    # For every line in file it adds 1 to the total number of lines
        for _ in file:
            lines += 1
    # Returns results
    return lines