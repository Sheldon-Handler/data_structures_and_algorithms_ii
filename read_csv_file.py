#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import csv

import __init__
import address
import hash_table
import package


def init():
    """
    Initializes the data structures and variables for the program.

    Returns:
        None

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    __init__.addresses = get_addresses(
        __init__.address_csv_file
    )
    __init__.distances = get_distances(
        __init__.distance_csv_file
    )
    __init__.packages = get_packages(
        __init__.package_csv_file
    )


def get_addresses(
        file: str = __init__.address_csv_file,
) -> [address.Address]:
    """
    This function reads a csv file and returns a list of Address objects.

    Args:
       file (os.path.relpath): The file to read from.

    Returns:
        list: A list of Address objects.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    addresses = []

    # Open the csv file and read the rows into a list
    file_open = open(file)
    csv_reader = csv.reader(file_open)

    # Read the csv file and store the rows in a list
    for i in csv_reader:  # O(n) - for loop
        addresses.append(
            address.Address(
                id=int(i[0]), name=str(i[1]), address=str(i[2])
            ),
        )

    return addresses


def get_distances(
        file: str = __init__.distance_csv_file,
) -> [[float]]:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (str): The file to read from.

    Returns:
        [[float]]: List of sublists of distance data from csv file as a distance matrix.

    Notes:
        time complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)
        space complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)
    """
    distance_matrix = []
    csv_reader = csv.reader(open(file, "r"))

    # Read the csv file and store the rows in a list
    for row in csv_reader:  # O(n) - for loop
        distance_row = []
        # Convert the string values to float values
        for column in row:  # O(n) - for loop
            if column == "":
                # If the value is empty, add None to the distance matrix
                distance_row.append(None)
            else:
                # If the value is not empty, convert it to a float and add it to the distance matrix
                distance_row.append(float(column))
        # Add the row to the distance matrix
        distance_matrix.append(distance_row)

    # Fill in the missing values in the distance matrix
    for row in range(len(distance_matrix)):  # O(n) - for loop
        for column in range(len(distance_matrix[row])):  # O(n) - for loop
            if distance_matrix[row][column] is None:
                distance_matrix[row][column] = distance_matrix[column][row]

    return distance_matrix


def get_packages(
        file: str = __init__.package_csv_file,
) -> hash_table.HashTable:
    """
    This function reads a csv file and returns a list of Package objects.

    Args:
        file (str): The file to read from.

    Returns:
        list: A list of Package objects.

    Notes:
        time complexity:
            best case: O(n^2)
            worst case: O(n^2)
            average case: O(n^2)
        space complexity:
            best case: O(n)
            worst case: O(n)
            average case: O(n)
    """

    # Create an empty hash table to store the packages
    __hash_table__ = hash_table.HashTable()

    # Open the csv file and read the rows into a list
    csv_file = open(file, "r")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of Package objects
    for row in reader:  # O(n) - for loop

        matching_address = int
        for i in __init__.addresses:  # O(n) - for loop
            if i.address == row[1]:
                matching_address = i

        # Create a Package object
        new_package = package.Package(
            id=int(row[0]),
            address_id=matching_address.id,
            address_name=matching_address.name,
            address=matching_address.address,
            city=row[2],
            state=row[3],
            zip=row[4],
            delivery_deadline=(row[5]),
            weight_kilo=int(row[6]),
            special_notes=row[7],
        )

        # Add package to hash table
        __hash_table__.add(new_package.id, new_package)

    return __hash_table__
