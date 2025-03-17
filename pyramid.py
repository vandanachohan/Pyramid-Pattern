def draw_pyramid(height):
    for i in range(1, height + 1):
        # Calculate the number of spaces and stars for the current row
        spaces = " " * (height - i)  # Spaces to center-align the stars
        stars = "*" * (2 * i - 1)    # Stars for the current row
        # Print the row
        print(spaces + stars)

# Main program
if __name__ == "__main__":
    height = int(input("Enter the height of the pyramid: "))
    draw_pyramid(height)