# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Dec. 9, 2022
# This program calculates the area of a triangle with Heron's formula
# and also calculates the interior angles with cosine law

# math is needed for square root and cosine
import math

# calculates the area of a triangle using heron's formula
def calc_area(side_a, side_b, side_c):
    # variable called 's' to conserve space but it represents half the perimeter
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    return area


# calculates one angle using cosine law
def calc_angle(side_a, side_b, side_c):
    angle_a = math.acos(
        (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
    )
    return angle_a * (180 / math.pi)


def main():
    try:
        # gets user input for the units and the side lengths then casts them
        units = input("Please enter the units you are using: ")
        user_side_a = float(input("Please enter the first side of your triangle: "))
        user_side_b = float(input("Please enter the second side of your triangle: "))
        user_side_c = float(input("Please enter the third side of your triangle: "))
    except:
        print("Please enter a valid side length.")
        # restart program after error
        main()
    else:
        # check if any side lengths are zero
        if (user_side_a == 0) | (user_side_b == 0) | (user_side_c == 0):
            print("You can not have a side length of zero.")
            # restart program after error
            main()
        # check if any side lengths are negative
        elif (user_side_a < 0) | (user_side_b < 0) | (user_side_c < 0):
            print("You can not have a negative side length.")
            # restart program after error
            main()
        # check if the triangle is real
        # by ensuring the two smaller sides are greater than the largest side
        elif (
            ((user_side_a + user_side_b) < user_side_c)
            | ((user_side_b + user_side_c) < user_side_a)
            | ((user_side_a + user_side_c) < user_side_b)
        ):
            print(
                "Invalid triangle! The two smaller sides should add to more than the longest side"
            )
            # restart program after error
            main()

        else:
            # call calc_area to get the area of the triangle
            final_area = calc_area(user_side_a, user_side_b, user_side_c)

            # call calc_angle 3 times to get all interior angles
            first_angle = calc_angle(user_side_a, user_side_b, user_side_c)
            second_angle = calc_angle(user_side_b, user_side_c, user_side_a)
            third_angle = calc_angle(user_side_c, user_side_a, user_side_b)

            # display the area of the triangle
            print(f"The area of your triangle is {final_area}{units}²\n")

            # display the interior angles of the triangle
            print("The corresponding (opposite) angles to your sides are:")
            print(f"first side  | {first_angle}°")
            print(f"second side | {second_angle}°")
            print(f"third side  | {third_angle}°")


if __name__ == "__main__":
    main()
