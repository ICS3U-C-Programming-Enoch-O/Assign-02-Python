# !/usr/bin/env python3
# Created by: Enoch O
# Created on: March 4 2025
# This program asks the user for the length, Height and radius of the Oblique cylinder
# It then Calculates and Displays the Volume and Surface area using tau.
import math


def main():
    # get the length, height, radius
    length = float(input)("What is the length of your oblique cylinder?")
    height = float(input)("What is the height of oblique cylinder?")
    radius = float(input)("What is the radius of your oblique cylinder?")

    # process
    volume = (
        math.pi * radius**2 * height
    )  # Volume of an oblique cylinder is the same as a right cylinder.
    surface_area = (
        2 * math.pi * radius * (length + radius)
    )  # surface area of an oblique cylinder

    # output
    print(f"The volume of the oblique cylinder is: {volume:.2f}")
    print(f"The surface area of the oblique cylinder is: {surface_area:.2f}")


if __name__ == "__main__":
    main()
