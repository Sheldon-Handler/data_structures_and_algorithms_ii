"""This module provides the Package class to store package information."""

#  MIT License
#
#  Copyright (c) 2023 Sheldon Handler
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
import delivery_status
import truck


# Package class to store information about a package.
class Package:
    """This class represents a package for and stores its information.

    Attributes:
        id (int): The package id.
        address (str): The package address.
        city (str): The package city.
        state (str): The package state.
        zip (str): The package zip code.
        weight_kilo (int): The package weight in kilos.
        delivery_deadline (time): The package delivery deadline.
        special_notes (str): The package special notes.
        delivery_status (delivery_status.DeliveryStatus): The package delivery status.
        truck (truck): The package delivery truck.
        delivery_time (time): The package delivery time.

    Returns:
        Package: A Package class instance.

    Examples:
        >>> new_package = Package(
        ...     id=1,
        ...     address="123 Main Street",
        ...     city="Salt Lake City",
        ...     state="UT",
        ...     zip="84111",
        ...     weight_kilo=10,
        ...     delivery_deadline="EOD",
        ...     special_notes="Some note",
        ...     delivery_status=delivery_status.DeliveryStatus.AT_HUB,
        ...     truck=None,
        ...     delivery_time=None,
        ... )
        >>> new_package.delivery_status
        1
        >>> new_package.delivery_status = delivery_status.DeliveryStatus.DELIVERED
        >>> new_package.delivery_status
        3
    """

    def __init__(
        self,
        id: int,
        address: str,
        city: str,
        state: str,
        zip: str,
        weight_kilo: int,
        delivery_deadline: time,
        special_notes: str,
        delivery_status: delivery_status.DeliveryStatus,
        truck: truck.Truck,
        delivery_time: time,
    ):
        """Initialize a Package object.

        Args:
            self (Package): The Package object.
            id (int): The ID of the package
            address (str): The address to delivery the package to.
            city (str): The city to delivery the package to.
            state (str): The state to delivery the package to.
            zip (str): The zip code to delivery the package to.
            weight_kilo (int): The weight of the package in KILO's.
            delivery_deadline (time): The deadline to deliver the package.
            special_notes (str): The special notes for the package delivery.
            delivery_status (delivery_status.DeliveryStatus): The delivery status of the package.
            truck (truck.Truck): The truck assigned to deliver the package
            delivery_time (time): The time that the package was delivered.

        Returns:
            Package: A Package class instance.
        """

        # Setting the attribute values of the package
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight_kilo = weight_kilo
        self.delivery_deadline = delivery_deadline
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.truck = truck
        self.delivery_time = delivery_time

    def to_list(self):
        """Method to return a list of the package attributes.

        Returns:
            list: The package attributes as a list.
        """
        return [
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.weight_kilo,
            self.delivery_deadline,
            self.special_notes,
            self.delivery_status,
            self.truck,
            self.delivery_time,
        ]


if __name__ == "__main__":
    new_package = Package(
        id=1,
        address="123 Main Street",
        city="Salt Lake City",
        state="UT",
        zip="84111",
        weight_kilo=10,
        delivery_deadline="EOD",
        special_notes="Some note",
        delivery_status=delivery_status.DeliveryStatus.AT_HUB,
        truck=None,
        delivery_time=None,
    )
    print(new_package)
    new_package.delivery_status = delivery_status.DeliveryStatus.DELIVERED
    print(new_package)