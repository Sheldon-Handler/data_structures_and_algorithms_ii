"""This Python module defines a Truck class to represent a truck and its
information."""
import this

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Import status package
import truck_status


# Truck class
class Truck:
    """This class represents a truck object and its information.

    Attributes:
        truck_id (int): The ID of the truck.
        truck_status (TruckStatus): The status of the truck.
        packages_assigned (list): The list of packages assigned for the truck to deliver.
        packages_loaded (list): The list of packages currently loaded onto the truck.
        packages_delivered (list): The list of packages delivered by the truck.

    Returns:
        Truck: A Truck class instance.

    Examples:
        >>> new_truck = Truck(
        ...     truck_id=1,
        ...     truck_status=truck_status.TruckStatus.AT_HUB,
        ...     packages_assigned=[],
        ...     packages_loaded=[],
        ...     packages_delivered=[],
        ... )
        >>> new_truck.truck_status
        TruckStatus.AT_HUB
        >>> new_truck.truck_status = truck_status.TruckStatus.EN_ROUTE
        >>> new_truck.truck_status
        TruckStatus.EN_ROUTE
    """

    # Constructor
    def __init__(
            self,
            truck_id: int,
            truck_status: truck_status.TruckStatus,
            packages_assigned: list,
            packages_loaded: list,
            packages_delivered: list,
    ):
        """Initialize the truck instance and sets the truck attributes with the given values.

        Args:
            truck_id (int): The ID of the truck.
            truck_status (TruckStatus): The status of the truck.
            packages_assigned (list): The list of packages assigned for the truck to deliver.
            packages_loaded (list): The list of packages currently loaded onto the truck.
            packages_delivered (list): The list of packages delivered by the truck.

        Returns:
            Truck: A Truck class instance.
        """

        self.truck_id = truck_id
        self.truck_status = truck_status
        self.packages_assigned = packages_assigned
        self.packages_loaded = packages_loaded
        self.packages_delivered = packages_delivered

    def to_list(self):
        """
        Method to return a list of the truck attributes.

        Returns:
            list: A list of the truck attributes.
        """

        return [self.truck_id, self.truck_status, self.packages_assigned, self.packages_loaded, self.packages_delivered]
