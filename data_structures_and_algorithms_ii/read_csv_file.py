import csv

import data_structures_and_algorithms_ii


def get_packages(file) -> list:
    """
    This function reads a csv file and returns a list of Package objects.

    Args:
        file (str): The file to read from.

    Returns:
        list: A list of Package objects.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    packages = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of Package objects
    for row in reader:  # O(n) - for loop
        # Create a Package object and add it to the list of packages
        packages.append(data_structures_and_algorithms_ii.package.Package(*row))

    csv_file.close()

    return packages


def get_distances(file) -> list[list]:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (str): The file to read from.

    Returns:
        list[list]: List of distance data from csv file as a distance matrix.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    rows = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of lists representing the distance matrix
    for row in reader:  # O(n) - for loop
        # Add the row to the list of rows
        rows.append(row)

    return rows


def get_addresses(file) -> list:
    """
    This function reads a csv file and returns a list of Location objects.

    Args:
        file (): The file to read from.

    Returns:
        list: A list of Location objects.

    Notes:
        time complexity: O(n)
        space complexity: O(n)
    """
    addresses = []

    csv_file = open(file, mode="r", newline="")
    reader = csv.reader(csv_file)

    # Parse the csv file and create a list of Address objects
    for row in reader:  # O(n) - for loop
        # Create an Address object and add it to the list of addresses
        addresses.append(
            data_structures_and_algorithms_ii.address.Address(
                int(row[0]), row[1], row[2]
            )
        )

    csv_file.close()

    return addresses


if __name__ == "__main__":
    print(get_distances(data_structures_and_algorithms_ii.distance_csv_file))

    exit(0)
