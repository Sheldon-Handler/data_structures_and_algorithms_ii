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

import dataclasses
import time

from truck import Truck
from delivery_status import DeliveryStatus
from location import Location


@dataclasses.dataclass
class Package:
    """This dataclass defines a package instance with its information.

    Attributes:
        id (int): The package id.
        location (Location): The package location.
        weight_kilo (int): The package weight in kilos.
        delivery_deadline (time): The package delivery deadline.
        special_notes (str): The package special notes.
        delivery_status (DeliveryStatus): The package delivery status.
        truck (truck): The package delivery truck.
        delivery_time (time): The package delivery time.

    Returns:
        Package: A Package class instance.
    """

    id: int
    location: Location
    weight_kilo: int
    delivery_deadline: time
    special_notes: str
    delivery_status: DeliveryStatus
    truck: Truck
    delivery_time: time
