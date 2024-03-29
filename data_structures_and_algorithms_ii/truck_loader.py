#  MIT License
#
#  Copyright (c) 2024 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import data_structures_and_algorithms_ii
import datetime


def load_truck(
    truck,
    packages,
    load_time=datetime.datetime.now().time(),
):
    """
    Loads packages onto trucks for delivery.

    Args:
        truck (Truck): The truck to load.
        packages (list[Package]): The packages to load onto the truck.
        load_time (datetime.time): The time to load the packages. Defaults to current time.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(n^2)
        space complexity: O(1)
    """

    for package in packages:
        if (
            package.special_notes_attribute_key == "Can only be on truck"
            and package.special_notes_attribute_value != truck.id
            and check_if_package_can_be_loaded(package, truck) is True
        ):
            package.truck_id = truck.id
            package.delivery_time = load_time
            package.delivery_status = "En Route"
            data_structures_and_algorithms_ii.packages.append(package.id)


def check_if_package_can_be_loaded(
    package,
    truck,
    load_time=datetime.datetime.now().time(),
) -> bool:
    """
    Checks if the given package can be loaded onto the given truck.

    Args:
        package (Package): The package to load.
        truck (Truck): The truck to load the package onto.
        load_time (datetime.time): The time to load the package. Defaults to current time.

    Returns:
        list: A list of Truck objects, each containing a list of packages to be delivered.

    Notes:
        time complexity: O(1)
        space complexity: O(1)
    """

    if (
        package.special_notes_attribute_key == "Can only be on truck"
        and package.special_notes_attribute_value != truck.id
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck.id} at {package.delivery_time}."
            f" It can only be loaded onto Truck {package.special_notes_attribute_value}."
        )
        return False
    elif (
        package.special_notes_attribute_key
        == "Delayed on flight---will not arrive to depot until"
        and load_time < package.special_notes_attribute_value
    ):
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck.id} at {package.delivery_time}."
            f" It will not arrive to the depot until {package.special_notes_attribute_value}."
        )
        return False
    elif package.special_notes_attribute_key == "Wrong address listed":
        print(
            f"Package {package.id} cannot be loaded onto Truck {truck.id} because the wrong address is assigned."
        )
        return False
    elif package.delivery_status == "Not Available":
        print(
            f"Package {package.id} is Not Available. Cannot load onto truck {truck.id}"
        )
        return False
    elif package.delivery_status == "En Route":
        print(
            f"Package {package.id} is currently En Route on Truck {package.truck_id}."
        )
        return False
    elif package.delivery_status == "Delivered":
        print(
            f"Package {package.id} has already been delivered from Truck {package.truck_id} at {package.delivery_time}."
        )
        return False
    elif package.delivery_status == "At Hub" and package.truck_id != (truck.id or None):
        print(f"Package {package.id} is already loaded onto Truck {package.truck_id}.")
        return False
    elif (
        len(data_structures_and_algorithms_ii.packages)
        >= data_structures_and_algorithms_ii.truck_capacity
    ):
        print(
            f"Truck {truck.id} is currently full. Cannot load package {package.id} onto it."
        )
        return False
    elif truck.truck_status == "Not Available" and truck.id != package.truck_id:
        print(
            f"Truck {truck.id} is Not Available. Cannot load package {package.id} onto it."
        )
        return False
    elif truck.truck_status == "En Route" and truck.id != package.truck_id:
        print(f"Truck {truck.id} En Route. Cannot load package {package.id} onto it.")
        return False
    elif truck.truck_status == "Returning" and truck.id != package.truck_id:
        print(
            f"Truck {truck.id} is not available. Cannot load package {package.id} onto it."
        )
        return False
    else:
        return True
