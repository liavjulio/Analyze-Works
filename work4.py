"""
Liav Huli 314917808
Yehuda Harush 324023332
Tamir Refael 208701805
Sagi Lidani 211451091
"""
import numpy as np

def linear_interpolation(points, x_value):
    """
    Performs linear interpolation between two points.

    Parameters:
    points (list of tuples): A list containing two tuples, each representing a point (x, y).
    x_value (float): The x value for which the y value is to be approximated.

    Returns:
    float: The interpolated y value corresponding to x_value.
    """
    (x1, y1), (x2, y2) = points
    return y1 + (y2 - y1) * (x_value - x1) / (x2 - x1)

def polynomial_interpolation(points, x_value):
    """
    Performs polynomial interpolation for three points using a second-degree polynomial.

    Parameters:
    points (list of tuples): A list containing three tuples, each representing a point (x, y).
    x_value (float): The x value for which the y value is to be approximated.

    Returns:
    float: The interpolated y value corresponding to x_value.
    """
    (x1, y1), (x2, y2), (x3, y3) = points
    coefficients = np.polyfit([x1, x2, x3], [y1, y2, y3], 2)
    polynomial = np.poly1d(coefficients)
    return polynomial(x_value)

def lagrange_interpolation(points, x_value):
    """
    Performs Lagrange interpolation for three points.

    Parameters:
    points (list of tuples): A list containing three tuples, each representing a point (x, y).
    x_value (float): The x value for which the y value is to be approximated.

    Returns:
    float: The interpolated y value corresponding to x_value.
    """
    (x1, y1), (x2, y2), (x3, y3) = points
    L1 = ((x_value - x2) * (x_value - x3)) / ((x1 - x2) * (x1 - x3))
    L2 = ((x_value - x1) * (x_value - x3)) / ((x2 - x1) * (x2 - x3))
    L3 = ((x_value - x1) * (x_value - x2)) / ((x3 - x1) * (x3 - x2))
    return y1 * L1 + y2 * L2 + y3 * L3

def main():
    """
    Main function to demonstrate interpolation methods.

    Prompts the user to enter an x value and select an interpolation method.
    Then it computes and prints the interpolated y value using the chosen method.
    """
    # Example points
    points = [(3, 7), (2, 9), (4, 5)]
    x_value = float(input("Enter the x value for which you want to find the approximate y value: "))
    
    print("Choose the interpolation method:")
    print("1: Linear Interpolation")
    print("2: Polynomial Interpolation (for 3 points)")
    print("3: Lagrange Interpolation (for 3 points)")
    
    choice = int(input("Enter the number corresponding to the method: "))
    
    if choice == 1:
        result = linear_interpolation(points[:2], x_value)
    elif choice == 2:
        result = polynomial_interpolation(points, x_value)
    elif choice == 3:
        result = lagrange_interpolation(points, x_value)
    else:
        print("Invalid choice.")
        return
    
    print(f"The approximate y value for x={x_value} is: {result}")

if __name__ == "__main__":
    main()