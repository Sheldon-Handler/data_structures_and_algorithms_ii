def calculate_package_loading_groups(
    distance_matrix: list[list], starting_location: int, truck_capacity: int
) -> list[list]:
    """
    Calculates groups of packages based on proximity to each other for multi-truck package delivery.

    Args:
        distance_matrix (list[list]): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location.
        truck_capacity (int): The maximum number of packages that a truck can carry.

    Returns:
        list[list]: A list of lists, where each inner list represents a group of packages to be delivered together.
    """

    # Sort unvisited locations based on their distance from the starting location
    unvisited_locations = list(range(len(distance_matrix)))
    sorted_locations = sorted(
        unvisited_locations,
        key=lambda location: distance_matrix[starting_location][location],
    )

    # Create groups of packages based on proximity
    package_groups = []
    current_group = []

    for location in sorted_locations:
        # Check if the current group has capacity for more packages
        if len(current_group) < truck_capacity:
            current_group.append(location)
        else:
            # If the current group is full, add it to the list of groups and start a new group
            package_groups.append(current_group.copy())
            current_group.clear()
            current_group.append(location)

    # Add the last group if it's not empty
    if current_group:
        package_groups.append(current_group.copy())

    return package_groups


def calculate_truck_route(
    distance_matrix: list[list], starting_location: int, package_group: list
):
    """
    Calculates the route for a truck given a group of packages to deliver.

    Args:
        distance_matrix (list[list]): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location.
        package_group (list): A list of package locations to be delivered by the truck.

    Returns:
        dict: A dictionary containing the truck's route and total distance traveled.
    """

    # Create a new truck with an empty route and distance
    current_truck = {"route": [], "distance": 0}

    # Deliver the packages in the group
    for location in package_group:
        current_truck["route"].append(location)
        current_truck["distance"] += distance_matrix[current_location][
            starting_location
        ]

        # Update the current location for the next delivery
        current_location = location

    # Add a return trip to the starting location
    current_truck["distance"] += distance_matrix[current_location][starting_location]

    return current_truck


def multi_truck_greedy_package_delivery_with_grouping(
    distance_matrix, starting_location, truck_capacity
):
    """
    Calculates the total distance traveled for package delivery using a greedy algorithm with package grouping.

    Args:
        distance_matrix (list of lists): A matrix representing the distances between delivery locations.
        starting_location (int): The index of the initial delivery location.
        truck_capacity (int): The maximum number of packages that a truck can carry.

    Returns:
        tuple: A tuple containing the total distance traveled and a list of truck routes.
    """

    total_distance = 0
    trucks = []

    # Calculate package loading groups
    package_groups = calculate_package_loading_groups(
        distance_matrix, starting_location, truck_capacity
    )

    # Calculate truck routes for each package group
    for package_group in package_groups:
        truck = calculate_truck_route(distance_matrix, starting_location, package_group)
        trucks.append(truck)

    # Update the total distance traveled by all trucks
    for truck in trucks:
        total_distance += truck["distance"]

    return total_distance, trucks
